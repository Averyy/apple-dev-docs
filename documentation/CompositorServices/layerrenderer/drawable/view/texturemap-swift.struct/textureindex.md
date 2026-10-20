# textureIndex

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The index of the view’s textures in the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var textureIndex: Int { get }
```

```c
size_t cp_view_texture_map_get_texture_index(cp_view_texture_map_t view_texture_map);
```

#### Discussion

Compositor Services places the color and depth textures for this view at same index number in the drawable. Use the returned index to the [`colorTextures`](../../colortextures.md) or [`depthTextures`](../../depthtextures.md) properties to retrieve the appropriate texture.

Compositor Services places the color and depth textures for this view at same index number in the drawable. In Swift, the index applies to the [`colorTextures`](../../colortextures.md)and [`depthTextures`](../../depthtextures.md) properties. In ObjectiveC, the index applies to the [`cp_drawable_get_color_texture`](../../../../cp_drawable_get_color_texture.md) and [`cp_drawable_get_depth_texture`](../../../../cp_drawable_get_depth_texture.md) functions.

> **Note**:  If you draw with array-based textures, retrieve and apply the index from [`sliceIndex`](./sliceindex.md) instead.

## See Also

### Getting the view’s texture map
- [var textureMap: LayerRenderer.Drawable.View.TextureMap](../texturemap-swift.property.md)
  The texture map for a view.
- [var sliceIndex: Int](./sliceindex.md)
  The index of the view’s texture in an array-based texture type.
- [var viewport: MTLViewport](./viewport.md)
  The portion of the texture that the view uses to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/textureindex)*