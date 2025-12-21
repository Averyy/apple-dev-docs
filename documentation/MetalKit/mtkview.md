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

The [`MTKView`](mtkview.md) class provides a default implementation of a Metal-aware view that you can use to render graphics using Metal and display them onscreen. When asked, the view provides a [`MTLRenderPassDescriptor`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor) object that points at a texture for you to render new contents into. Optionally, an [`MTKView`](mtkview.md) can create depth and stencil textures for you and any intermediate textures needed for antialiasing. The view uses a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) to manage the Metal drawable objects.

The view requires a [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) object to manage the Metal objects it creates for you. You must set the [`device`](mtkview/device.md) property and, optionally, modify the view’s drawable properties before drawing.

##### Configuring the Drawing Behavior

The MTKView class supports three drawing modes:

- Timed updates: The view redraws its contents based on an internal timer. In this case, which is the default behavior, both [`isPaused`](mtkview/ispaused.md) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) are set to [`false`](https://developer.apple.com/documentation/Swift/false). Use this mode for games and other animated content that’s regularly updated.
- Draw notifications: The view redraws itself when something invalidates its contents, usually because of a call to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()) or some other view-related behavior. In this case, set [`isPaused`](mtkview/ispaused.md) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) to [`true`](https://developer.apple.com/documentation/Swift/true). Use this mode for apps with a more traditional workflow, where updates happen when data changes, but not on a regular timed interval.
- Explicit drawing: The view redraws its contents only when you explicitly call the [`draw()`](mtkview/draw().md) method. In this case, set [`isPaused`](mtkview/ispaused.md) to [`true`](https://developer.apple.com/documentation/Swift/true) and [`enableSetNeedsDisplay`](mtkview/enablesetneedsdisplay.md) to [`false`](https://developer.apple.com/documentation/Swift/false). Use this mode to create your own custom workflow.

##### Drawing the Views Contents

Regardless of drawing mode, when the view needs to update its contents, it calls the [`draw(_:)`](https://developer.apple.com/documentation/AppKit/NSView/draw(_:)) method when that method has been overridden by a subclass, or [`draw(in:)`](mtkviewdelegate/draw(in:).md) on the view’s delegate if the subclass doesn’t override it. You should either subclass [`MTKView`](mtkview.md) or provide a delegate, but not both.

In your drawing method, you obtain a render pass descriptor from the view, render into it, and then present the associated drawable.

##### Obtaining a Drawable From a Metalkit View

Each [`MTKView`](mtkview.md) is backed by a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer). In your renderer, implement the [`MTKViewDelegate`](mtkviewdelegate.md) protocol to interact with a MetalKit view. Call the MetalKit view’s [`currentRenderPassDescriptor`](mtkview/currentrenderpassdescriptor.md) property to obtain a render pass descriptor configured for the current frame:

When you read this property, Core Animation implicitly obtains a drawable for the current frame and stores it in the [`currentDrawable`](mtkview/currentdrawable.md) property. It then configures a render pass descriptor to draw into that drawable, including any depth, stencil, and antialiasing textures as necessary. The view configures this render pass using the default store and load actions. You can adjust the descriptor further before using it to create a [`MTLRenderCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLRenderCommandEncoder).

Obtain drawables as late as possible; preferably, immediately before encoding your onscreen render pass.

##### Registering the Drawables Presentation

After rendering the contents, you must present the drawable to update the view’s contents. The most convenient way to present the content is to call the [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) method on the command buffer. Then, call the [`commit()`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/commit()) method to submit the command buffer to a GPU:

When a command queue schedules a command buffer for execution, the drawable tracks all render or write requests on itself in that command buffer. The operating system doesn’t present the drawable onscreen until the commands have finished executing. By asking the command buffer to present the drawable, you guarantee that presentation happens after the command queue has scheduled this command buffer. Don’t wait for the command buffer to finish executing before registering the drawable’s presentation.

> 💡 **Tip**:  For better performance, only retrieve the render pass descriptor when you’re ready to render the contents, and hold onto it and the related drawable object as little as possible. Release it as soon as you finish with it. For more information, see [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer#Keeping-References-to-Drawables).

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
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()).
- [func draw()](mtkview/draw.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](mtkview/presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.
### Releasing Memory
- [func releaseDrawables()](mtkview/releasedrawables.md)
  Releases the [`depthStencilTexture`](mtkview/depthstenciltexture.md) and [`multisampleColorTexture`](mtkview/multisamplecolortexture.md) objects.
### Instance Properties
- [var currentMTL4RenderPassDescriptor: MTL4RenderPassDescriptor?](mtkview/currentmtl4renderpassdescriptor.md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [protocol MTKViewDelegate](mtkviewdelegate.md)
  Methods for responding to a MetalKit view’s drawing and resizing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview)*