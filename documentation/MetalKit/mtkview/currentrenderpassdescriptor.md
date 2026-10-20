# currentRenderPassDescriptor

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

A render pass descriptor to draw into the current drawable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentRenderPassDescriptor: MTLRenderPassDescriptor? { get }
```

```objc
@property (nonatomic, readonly, nullable) MTLRenderPassDescriptor * currentRenderPassDescriptor;
```

#### Discussion

Reading this property creates and returns a new render pass descriptor to render into the current drawable’s texture. [`MTKView`](../mtkview.md) doesn’t use this descriptor, and there’s no requirement for your application to use it.

This property is `nil` if the view’s [`device`](./device.md) property isn’t set or if [`currentDrawable`](./currentdrawable.md) is `nil`. Your app should check that [`currentRenderPassDescriptor`](./currentrenderpassdescriptor.md) isn’t `nil` before attempting to use it.

The view configures the render pass as follows:

- If multisampling isn’t enabled—The color attachment at index 0 of the render pass descriptor points to the texture assigned to the current drawable, with a load action of [`MTLLoadAction.clear`](../../Metal/mtlloadaction/clear.md) and a store action of [`MTLStoreAction.store`](../../Metal/mtlstoreaction/store.md).
- If you’ve enabled multisampling—The color attachment at index 0 of the render pass descriptor points to the multisample texture, the resolve texture points to the texture assigned to the current drawable, and the attachment has a load action of [`MTLLoadAction.clear`](../../Metal/mtlloadaction/clear.md) and a store action of [`MTLStoreAction.multisampleResolve`](../../Metal/mtlstoreaction/multisampleresolve.md).
- If you’ve specified a depth or stencil target—The render pass configures the appropriate targets, with a load action of [`MTLLoadAction.clear`](../../Metal/mtlloadaction/clear.md) and a store action of [`MTLStoreAction.dontCare`](../../Metal/mtlstoreaction/dontcare.md).

## See Also

### Retrieving Render Target Information
- [var currentDrawable: (any CAMetalDrawable)?](./currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilTexture: (any MTLTexture)?](./depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](./depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.
- [var multisampleColorTexture: (any MTLTexture)?](./multisamplecolortexture.md)
  The multisample color sample texture to render into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/currentrenderpassdescriptor)*