# textureMap

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The texture map for a view.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var textureMap: LayerRenderer.Drawable.View.TextureMap { get }
```

```c
cp_view_texture_map_tcp_view_get_view_texture_map(cp_view_t view);
```

## Discussion

Use the texture map to fetch additional information you need to draw your content. For example, use it to fetch the rectangle that defines the view’s content area.

## See Also

### Getting the view’s texture map
- [LayerRenderer.Drawable.View.TextureMap](./texturemap-swift.struct.md)
  A type that provides details about the textures associated with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view/texturemap-swift.property)*