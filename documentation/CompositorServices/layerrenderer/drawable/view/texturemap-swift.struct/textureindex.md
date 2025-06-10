# textureIndex

**Framework**: Compositor Services  
**Kind**: property

The index of the view’s textures in the drawable.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var textureIndex: Int { get }
```

#### Discussion

Compositor Services places the color and depth textures for this view at same index number in the drawable. Use the returned index to the [`colorTextures`](layerrenderer/drawable/colortextures.md) or [`depthTextures`](layerrenderer/drawable/depthtextures.md) properties to retrieve the appropriate texture.

Compositor Services places the color and depth textures for this view at same index number in the drawable. In Swift, the index applies to the [`colorTextures`](layerrenderer/drawable/colortextures.md)and [`depthTextures`](layerrenderer/drawable/depthtextures.md) properties. In ObjectiveC, the index applies to the [`cp_drawable_get_color_texture`](cp_drawable_get_color_texture.md) and [`cp_drawable_get_depth_texture`](cp_drawable_get_depth_texture.md) functions.

> **Note**:  If you draw with array-based textures, retrieve and apply the index from [`sliceIndex`](layerrenderer/drawable/view/texturemap-swift.struct/sliceindex.md) instead.

## See Also

- [var textureMap: LayerRenderer.Drawable.View.TextureMap](layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [var sliceIndex: Int](layerrenderer/drawable/view/texturemap-swift.struct/sliceindex.md)
  The index of the view’s texture in an array-based texture type.
- [var viewport: MTLViewport](layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/textureindex)*