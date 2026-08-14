# MTKView

**Framework**: MetalKit  
**Kind**: class

A specialized view that creates, configures, and displays Metal objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MTKView
```

#### Overview

The [`MTKView`](mtkview.md) class provides a default implementation of a Metal-aware view that you can use to render graphics using Metal and display them onscreen. When asked, the view provides a [`MTLRenderPassDescriptor`](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) object that points at a texture for you to render new contents into. Optionally, an [`MTKView`](mtkview.md) can create depth and stencil textures for you and any intermediate textures needed for antialiasing. The view uses a [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer) to manage the Metal drawable objects.

The view requires a [`MTLDevice`](https://developer.apple.com/documentation/metal/mtldevice) object to manage the Metal objects it creates for you. You must set the [`device`](mtkview/device.md) property and, optionally, modify the view’s drawable properties before drawing.

##### Configuring the Drawing Behavior

The MTKView class supports three drawing modes:

- Timed updates: The view redraws its contents based on an internal timer. In this case, which is the default behavior, both [`isPaused`](mtkview/ispaused.md) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) are set to [`false`](https://developer.apple.com/documentation/swift/false). Use this mode for games and other animated content that’s regularly updated.
- Draw notifications: The view redraws itself when something invalidates its contents, usually because of a call to [`setNeedsDisplay()`](https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay()) or some other view-related behavior. In this case, set [`isPaused`](mtkview/ispaused.md) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) to [`true`](https://developer.apple.com/documentation/swift/true). Use this mode for apps with a more traditional workflow, where updates happen when data changes, but not on a regular timed interval.
- Explicit drawing: The view redraws its contents only when you explicitly call the [`draw()`](mtkview/draw().md) method. In this case, set [`isPaused`](mtkview/ispaused.md) to [`true`](https://developer.apple.com/documentation/swift/true) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) to [`false`](https://developer.apple.com/documentation/swift/false). Use this mode to create your own custom workflow.

##### Drawing the Views Contents

Regardless of drawing mode, when the view needs to update its contents, it calls the [`draw(_:)`](https://developer.apple.com/documentation/appkit/nsview/draw(_:)) method when that method has been overridden by a subclass, or [`draw(in:)`](mtkviewdelegate/draw(in:).md) on the view’s delegate if the subclass doesn’t override it. You should either subclass [`MTKView`](mtkview.md) or provide a delegate, but not both.

In your drawing method, you obtain a render pass descriptor from the view, render into it, and then present the associated drawable.

##### Obtaining a Drawable From a Metalkit View

Each [`MTKView`](mtkview.md) is backed by a [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer). In your renderer, implement the [`MTKViewDelegate`](mtkviewdelegate.md) protocol to interact with a MetalKit view. Call the MetalKit view’s [`currentRenderPassDescriptor`](mtkview/currentrenderpassdescriptor.md) property to obtain a render pass descriptor configured for the current frame:

**Swift**:

```swift
// BEGIN encoding your onscreen render pass.
// Obtain a render pass descriptor generated from the drawable's texture.
// (`currentRenderPassDescriptor` implicitly obtains the current drawable.)
// If there's a valid render pass descriptor, use it to render to the current drawable.
if let onscreenDescriptor = view.currentRenderPassDescriptor
```

**Objective-C**:

```objc
// BEGIN encoding your onscreen render pass.
// Obtain a render pass descriptor generated from the drawable's texture.
// (`currentRenderPassDescriptor` implicitly obtains the current drawable.)
MTLRenderPassDescriptor* onscreenDescriptor = view.currentRenderPassDescriptor;
```

When you read this property, Core Animation implicitly obtains a drawable for the current frame and stores it in the [`currentDrawable`](mtkview/currentdrawable.md) property. It then configures a render pass descriptor to draw into that drawable, including any depth, stencil, and antialiasing textures as necessary. The view configures this render pass using the default store and load actions. You can adjust the descriptor further before using it to create a [`MTLRenderCommandEncoder`](https://developer.apple.com/documentation/metal/mtlrendercommandencoder).

Obtain drawables as late as possible; preferably, immediately before encoding your onscreen render pass.

##### Registering the Drawables Presentation

After rendering the contents, you must present the drawable to update the view’s contents. The most convenient way to present the content is to call the [`present(_:)`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:)) method on the command buffer. Then, call the [`commit()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/commit()) method to submit the command buffer to a GPU:

**Swift**:

```swift
if let onscreenDescriptor = view.currentRenderPassDescriptor,
let onscreenCommandEncoder = onscreenCommandBuffer.makeRenderCommandEncoder(descriptor: onscreenDescriptor) {
    /* Set render state and resources.
       ...
     */
    /* Issue draw calls.
       ...
     */
    onscreenCommandEncoder.endEncoding()
    // END encoding your onscreen render pass.
    
    // Register the drawable's presentation.
    if let currentDrawable = view.currentDrawable {
        onscreenCommandBuffer.present(currentDrawable)
    }
}

// Finalize your onscreen CPU work and commit the command buffer to a GPU.
onscreenCommandBuffer.commit()
```

**Objective-C**:

```objc
// If there's a valid render pass descriptor, use it to render to the current drawable.
if(onscreenDescriptor != nil) {
    id<MTLRenderCommandEncoder> onscreenCommandEncoder = [onscreenCommandBuffer renderCommandEncoderWithDescriptor:onscreenDescriptor];
    /* Set render state and resources.
       ...
     */
    /* Issue draw calls.
       ...
     */
    [onscreenCommandEncoder endEncoding];
    // END encoding your onscreen render pass.

    // Register the drawable's presentation.
    [onscreenCommandBuffer presentDrawable:view.currentDrawable];
}

// Finalize your onscreen CPU work and commit the command buffer to a GPU.
[onscreenCommandBuffer commit];
```

When a command queue schedules a command buffer for execution, the drawable tracks all render or write requests on itself in that command buffer. The operating system doesn’t present the drawable onscreen until the commands have finished executing. By asking the command buffer to present the drawable, you guarantee that presentation happens after the command queue has scheduled this command buffer. Don’t wait for the command buffer to finish executing before registering the drawable’s presentation.

> 💡 **Tip**:  For better performance, only retrieve the render pass descriptor when you’re ready to render the contents, and hold onto it and the related drawable object as little as possible. Release it as soon as you finish with it. For more information, see [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer).

## Topics

### Creating a View
- [init(coder: NSCoder)](mtkview/init(coder:).md)
  Initializes a view from data in a given unarchiver.
- [init(frame: CGRect, device: (any MTLDevice)?)](mtkview/init(frame:device:).md)
  Initializes a view with the specified frame rectangle and Metal device.
### Configuring the Delegate
- [var delegate: (any MTKViewDelegate)?](mtkview/delegate.md)
  The view’s delegate.
### Configuring the Metal Device
- [var device: (any MTLDevice)?](mtkview/device.md)
  The device object the view uses to create its Metal objects.
- [var preferredDevice: (any MTLDevice)?](mtkview/preferreddevice.md)
  The device object that the system recommends using for this view.
### Configuring the Color Render Target
- [var colorPixelFormat: MTLPixelFormat](mtkview/colorpixelformat.md)
  The color pixel format for the current drawable’s texture.
- [var colorspace: CGColorSpace?](mtkview/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](mtkview/framebufferonly.md)
  A Boolean value that determines whether the drawable’s textures are used only for rendering.
- [var drawableSize: CGSize](mtkview/drawablesize.md)
  The current size of drawable textures.
- [var preferredDrawableSize: CGSize](mtkview/preferreddrawablesize.md)
  The recommended dimensions of the drawable.
- [var autoResizeDrawable: Bool](mtkview/autoresizedrawable.md)
  A Boolean value that controls whether to resize the drawable as the view changes size.
- [var clearColor: MTLClearColor](mtkview/clearcolor.md)
  The color to use to clear the color target when creating a render pass descriptor.
### Configuring the Render Target Properties
- [var depthStencilPixelFormat: MTLPixelFormat](mtkview/depthstencilpixelformat.md)
  The format used to generate the [`depthStencilTexture`](mtkview/depthstenciltexture.md) object.
- [var depthStencilAttachmentTextureUsage: MTLTextureUsage](mtkview/depthstencilattachmenttextureusage.md)
  The texture usage characteristics that the view uses when creating the depth and stencil textures.
- [var clearDepth: Double](mtkview/cleardepth.md)
  The depth value to use to clear the depth target when creating a render pass descriptor.
- [var clearStencil: UInt32](mtkview/clearstencil.md)
  The stencil value to use to clear the stencil target when creating a render pass descriptor.
### Configuring Multisampling
- [var sampleCount: Int](mtkview/samplecount.md)
  The sample count used to generate the [`multisampleColorTexture`](mtkview/multisamplecolortexture.md) object.
- [var multisampleColorAttachmentTextureUsage: MTLTextureUsage](mtkview/multisamplecolorattachmenttextureusage.md)
  The texture usage characteristics that the view uses when creating multisample textures.
### Retrieving Render Target Information
- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](mtkview/currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var currentDrawable: (any CAMetalDrawable)?](mtkview/currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilTexture: (any MTLTexture)?](mtkview/depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](mtkview/depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.
- [var multisampleColorTexture: (any MTLTexture)?](mtkview/multisamplecolortexture.md)
  The multisample color sample texture to render into.
### Configuring Drawing Behavior
- [var preferredFramesPerSecond: Int](mtkview/preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](mtkview/ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [var enableSetNeedsDisplay: Bool](mtkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay()).
- [func draw()](mtkview/draw.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](mtkview/presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.
### Releasing Memory
- [func releaseDrawables()](mtkview/releasedrawables.md)
  Releases the [`depthStencilTexture`](mtkview/depthstenciltexture.md) and [`multisampleColorTexture`](mtkview/multisamplecolortexture.md) objects.
### Instance Properties
- [var currentMTL4RenderPassDescriptor: MTL4RenderPassDescriptor?](mtkview/currentmtl4renderpassdescriptor.md)
- [var residencySet: any MTLResidencySet](mtkview/residencyset.md)

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [protocol MTKViewDelegate](mtkviewdelegate.md)
  Methods for responding to a MetalKit view’s drawing and resizing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview)*