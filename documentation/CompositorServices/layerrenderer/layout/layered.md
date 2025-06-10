# LayerRenderer.Layout.layered

**Framework**: Compositor Services  
**Kind**: case

A layout that specifies each view’s content as a slice of a single texture.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case layered
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

The layout uses a single texture to store the content for all rendered views. The type of the texture is [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray). The texture map’s slice index indicates which array slot contains each view’s content.

## See Also

- [LayerRenderer.Layout.dedicated](layerrenderer/layout/dedicated.md)
  A layout that assigns a separate texture to each rendered view.
- [LayerRenderer.Layout.shared](layerrenderer/layout/shared.md)
  A layout that uses a single texture to store the content for all rendered views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout/layered)*