# cp_view_texture_map_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that provides details about the textures associated with a view.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef struct cp_view_texture_map * cp_view_texture_map_t;
```

#### Discussion

A texture map helps you locate the content for a specific view within a texture. Texture maps are especially important when a layer uses a single texture to manage multiple views. For example, a head-mounted display might store the images for both the left and right eyes in a single texture. Pass this type to other functions to get specific details about the current texture, such as its view bounds or its index into a texture array.

## Topics

### Getting the viewport
- [var viewport: MTLViewport](./layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.
### Getting the texture indices
- [var sliceIndex: Int](./layerrenderer/drawable/view/texturemap-swift.struct/sliceindex.md)
  The index of the view’s texture in an array-based texture type.
- [var textureIndex: Int](./layerrenderer/drawable/view/texturemap-swift.struct/textureindex.md)
  The index of the view’s textures in the drawable.

## See Also

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](./layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [var textureIndex: Int](./layerrenderer/drawable/view/texturemap-swift.struct/textureindex.md)
  The index of the view’s textures in the drawable.
- [var sliceIndex: Int](./layerrenderer/drawable/view/texturemap-swift.struct/sliceindex.md)
  The index of the view’s texture in an array-based texture type.
- [var viewport: MTLViewport](./layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_view_texture_map_t)*