# currentDrawable

**Framework**: MetalKit  
**Kind**: property

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
@MainActor
var currentDrawable: (any CAMetalDrawable)? { get }
```

#### Discussion

If all drawable objects are in use, the value of this property is `nil`. Your app should check that [`currentDrawable`](mtkview/currentdrawable.md) isn’t `nil` before attempting to draw. The view changes the value of this property only after returning from a drawing function, either [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) from a subclassed instance of the view, or [`draw(in:)`](mtkviewdelegate/draw(in:).md) from the view’s delegate.

Use a [`MTLRenderCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLRenderCommandEncoder) object to render into the drawable’s texture and present it for display (typically registered using the [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) method of a command buffer). Try to minimize the time between when you fetch the drawable and when you submit the command buffer that uses it. For more information, see [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer#3385893).

## See Also

- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](mtkview/currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var depthStencilTexture: (any MTLTexture)?](mtkview/depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](mtkview/depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.
- [var multisampleColorTexture: (any MTLTexture)?](mtkview/multisamplecolortexture.md)
  The multisample color sample texture to render into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/currentdrawable)*