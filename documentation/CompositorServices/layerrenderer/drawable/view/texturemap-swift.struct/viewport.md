# viewport

**Framework**: Compositor Services  
**Kind**: property

The portion of the texture that the view uses to draw its content.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var viewport: MTLViewport { get }
```

#### Discussion

This retrieves the size of the view and its location within the texture. If the layer dedicates a separate texture to each view, the texture bounds and view bounds match. However, if the layer uses a shared or layered texture, the view’s location or other slice index might differ.

## See Also

- [var textureMap: LayerRenderer.Drawable.View.TextureMap](layerrenderer/drawable/view/texturemap-swift.property.md)
  The texture map for a view.
- [var textureIndex: Int](layerrenderer/drawable/view/texturemap-swift.struct/textureindex.md)
  The index of the view’s textures in the drawable.
- [var sliceIndex: Int](layerrenderer/drawable/view/texturemap-swift.struct/sliceindex.md)
  The index of the view’s texture in an array-based texture type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.struct/viewport)*