# CAMetalLayer

**Framework**: Quartzcore  
**Kind**: class

A Core Animation layer that Metal can render into, typically displayed onscreen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAMetalLayer
```

#### Overview

Use a [`CAMetalLayer`](cametallayer.md) when you want to use Metal to render a layer’s contents; for example, to render into a view. Consider using [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) instead, because this class automatically wraps a [`CAMetalLayer`](cametallayer.md) object and provides a higher-level abstraction.

If you’re using UIKit, to create a view that uses a [`CAMetalLayer`](cametallayer.md), create a subclass of [`UIView`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) and override its [`layerClass`](https://developer.apple.com/documentation/UIKit/UIView/layerClass) class method to return a [`CAMetalLayer`](cametallayer.md):

```objc
+ (Class) layerClass
{
    return [CAMetalLayer class];
}
```

If you’re using AppKit, configure an [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object to use a backing layer and assign a [`CAMetalLayer`](cametallayer.md) object to the view:

```objc
myView.wantsLayer = YES;
myView.layer = [CAMetalLayer layer];
```

Adjust the layer’s properties to configure its underlying pixel format and other display behaviors.

##### Rendering the Layers Contents

A [`CAMetalLayer`](cametallayer.md) creates a pool of Metal drawable objects ([`CAMetalDrawable`](cametaldrawable.md)). At any given time, one of these drawable objects contains the contents of the layer. To change the layer’s contents, ask the layer for a drawable object, render into it, and then update the layer’s contents to point to the new drawable.

Call the layer’s [`nextDrawable()`](cametallayer/nextdrawable().md) method to obtain a drawable object. Get the drawable object’s texture and create a render pass that renders to that texture, as shown in the code below:

```objc
CAMetalLayer *metalLayer = (CAMetalLayer*)self.layer;
id<CAMetalDrawable> *drawable = [metalLayer nextDrawable];

MTLRenderPassDescriptor *renderPassDescriptor
                               = [MTLRenderPassDescriptor renderPassDescriptor];

renderPassDescriptor.colorAttachments[0].texture = drawable.texture;
renderPassDescriptor.colorAttachments[0].loadAction = MTLLoadActionClear;
renderPassDescriptor.colorAttachments[0].clearColor = MTLClearColorMake(0.0,0.0,0.0,1.0);
...
```

To change the layer’s contents to the new drawable, call the [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) method (or one of its variants) on the command buffer containing the encoded render pass, passing in the drawable object to present.

```objc
[commandBuffer presentDrawable:drawable];
```

##### Keeping References to Drawables

The layer reuses a drawable only if it isn’t onscreen and there are no strong references to it. Further, if a drawable isn’t available when you call [`nextDrawable()`](cametallayer/nextdrawable().md), the system waits for one to become available. To avoid stalls in your app, request a new drawable only when you need it, and release any references to it as quickly as possible after you’re done with it.

For example, before retrieving a new drawable, you might perform other work on the CPU or submit commands to the GPU that don’t require the drawable. Then, obtain the drawable and encode a command buffer to render into it, as described above. After you commit this command buffer, release all strong references to the drawable. If you don’t release drawables correctly, the layer runs out of drawables, and future calls to [`nextDrawable()`](cametallayer/nextdrawable().md) return `nil`.

##### Releasing the Drawable

Don’t release the drawable explicitly; instead, embed your render loop within an autorelease pool block:

This block releases drawables promptly and avoids possible deadlock situations with multiple drawables. Release drawables as soon as possible after committing your onscreen render pass.

> **Note**:  As of iOS 10 and tvOS 10, you can safely retain a drawable to query its properties, such as [`drawableID`](https://developer.apple.com/documentation/Metal/MTLDrawable/drawableID) and [`presentedTime`](https://developer.apple.com/documentation/Metal/MTLDrawable/presentedTime), after the system has presented it. If you don’t need to query these properties, release the drawable when you no longer need it.

## Topics

### Configuring the Metal Device
- [var device: (any MTLDevice)?](cametallayer/device.md)
  The Metal device responsible for the layer’s drawable resources.
- [var preferredDevice: (any MTLDevice)?](cametallayer/preferreddevice.md)
  The device object that the system recommends using for this layer.
### Configuring the Layer’s Drawable Objects
- [var pixelFormat: MTLPixelFormat](cametallayer/pixelformat.md)
  The pixel format of the layer’s textures.
- [var colorspace: CGColorSpace?](cametallayer/colorspace.md)
  The color space of the rendered content.
- [var framebufferOnly: Bool](cametallayer/framebufferonly.md)
  A Boolean value that determines whether the layer’s textures are used only for rendering.
- [var drawableSize: CGSize](cametallayer/drawablesize.md)
  The size, in pixels, of textures for rendering layer content.
### Configuring Presentation Behavior
- [var presentsWithTransaction: Bool](cametallayer/presentswithtransaction.md)
  A Boolean value that determines whether the layer presents its content using a Core Animation transaction.
- [var displaySyncEnabled: Bool](cametallayer/displaysyncenabled.md)
  A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.
### Configuring Extended Dynamic Range Behavior
- [var wantsExtendedDynamicRangeContent: Bool](cametallayer/wantsextendeddynamicrangecontent.md)
  Enables extended dynamic range values onscreen.
- [var edrMetadata: CAEDRMetadata?](cametallayer/edrmetadata.md)
  Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.
### Obtaining a Metal Drawable
- [func nextDrawable() -> (any CAMetalDrawable)?](cametallayer/nextdrawable.md)
  Waits until a Metal drawable is available, and then returns it.
- [var maximumDrawableCount: Int](cametallayer/maximumdrawablecount.md)
  The number of Metal drawables in the resource pool managed by Core Animation.
- [var allowsNextDrawableTimeout: Bool](cametallayer/allowsnextdrawabletimeout.md)
  A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.
### Configuring the Metal Performance HUD
- [var developerHUDProperties: [AnyHashable : Any]?](cametallayer/developerhudproperties.md)
  The properties of the Metal performance heads-up display.

## Relationships

### Inherits From
- [CALayer](calayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol CAMetalDrawable](cametaldrawable.md)
  A Metal drawable associated with a Core Animation layer.
- [class CAEAGLLayer](caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAEDRMetadata](caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CAOpenGLLayer](caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.
- [class CARenderer](carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuartzCore/cametallayer)*