# sliceIndex

**Framework**: Compositor Services  
**Kind**: property

The index of the view’s texture in an array-based texture type.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var sliceIndex: Int { get }
```

#### Discussion

Use the returned index to retrieve the view’s texture when the texture type is [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray). When configuring your render pass descriptor, specify the index in the [`slice`](https://developer.apple.com/documentation/Metal/MTLRenderPassAttachmentDescriptor/slice) property of the descriptor’s color and depth attachments.

If you don’t use array-based textures for drawing, fetch the index using [`textureIndex`](layerrenderer/drawable/view/texturemap-swift.struct/textureindex.md) instead.

## See Also

- [var textureMap: LayerRenderer.Drawable.View.TextureMap](layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [var textureIndex: Int](layerrenderer/drawable/view/texturemap-swift.struct/textureindex.md)
  The index of the view’s textures in the drawable.
- [var viewport: MTLViewport](layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/sliceindex)*