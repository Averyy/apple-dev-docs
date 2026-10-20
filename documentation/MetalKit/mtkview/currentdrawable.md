# currentDrawable

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The drawable to use for the current frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentDrawable: (any CAMetalDrawable)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<CAMetalDrawable> currentDrawable;
```

#### Discussion

If all drawable objects are in use, the value of this property is `nil`. Your app should check that [`currentDrawable`](./currentdrawable.md) isn’t `nil` before attempting to draw. The view changes the value of this property only after returning from a drawing function, either [`draw(_:)`](../../UIKit/uiview/draw%28_%29.md) from a subclassed instance of the view, or [`draw(in:)`](../mtkviewdelegate/draw%28in%29.md) from the view’s delegate.

Use a [`MTLRenderCommandEncoder`](../../Metal/mtlrendercommandencoder.md) object to render into the drawable’s texture and present it for display (typically registered using the [`present(_:)`](../../Metal/mtlcommandbuffer/present%28_%29.md) method of a command buffer). Try to minimize the time between when you fetch the drawable and when you submit the command buffer that uses it. For more information, see [`CAMetalLayer`](../../QuartzCore/cametallayer.md).

## See Also

### Retrieving Render Target Information
- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](./currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var depthStencilTexture: (any MTLTexture)?](./depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](./depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.
- [var multisampleColorTexture: (any MTLTexture)?](./multisamplecolortexture.md)
  The multisample color sample texture to render into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/currentdrawable)*