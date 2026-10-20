# viewport

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The portion of the texture that the view uses to draw its content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var viewport: MTLViewport { get }
```

```c
MTLViewport cp_view_texture_map_get_viewport(cp_view_texture_map_t view_texture_map);
```

#### Discussion

This retrieves the size of the view and its location within the texture. If the layer dedicates a separate texture to each view, the texture bounds and view bounds match. However, if the layer uses a shared or layered texture, the view’s location or other slice index might differ.

## See Also

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](../texturemap-swift.property.md)
  The texture map for a view.
- [var textureIndex: Int](./textureindex.md)
  The index of the view’s textures in the drawable.
- [var sliceIndex: Int](./sliceindex.md)
  The index of the view’s texture in an array-based texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/viewport)*