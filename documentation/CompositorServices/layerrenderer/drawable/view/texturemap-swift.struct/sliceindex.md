# sliceIndex

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The index of the view’s texture in an array-based texture type.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var sliceIndex: Int { get }
```

```c
size_t cp_view_texture_map_get_slice_index(cp_view_texture_map_t view_texture_map);
```

#### Discussion

Use the returned index to retrieve the view’s texture when the texture type is [`MTLTextureType.type2DArray`](../../../../../Metal/mtltexturetype/type2darray.md). When configuring your render pass descriptor, specify the index in the [`slice`](../../../../../Metal/mtlrenderpassattachmentdescriptor/slice.md) property of the descriptor’s color and depth attachments.

If you don’t use array-based textures for drawing, fetch the index using [`textureIndex`](./textureindex.md) instead.

## See Also

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](../texturemap-swift.property.md)
  The texture map for a view.
- [var textureIndex: Int](./textureindex.md)
  The index of the view’s textures in the drawable.
- [var viewport: MTLViewport](./viewport.md)
  The portion of the texture that the view uses to draw its content.
- [cp_view_texture_map_t](../../../../cp_view_texture_map_t.md)
  A type that provides details about the textures associated with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/sliceindex)*