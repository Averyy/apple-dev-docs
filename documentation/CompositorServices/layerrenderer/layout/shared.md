# LayerRenderer.Layout.shared

**Framework**: Compositor Services  
**Kind**: case

A layout that uses a single texture to store the content for all rendered views.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case shared
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

When a layer contains multiple views, the texture stores the images for those views side-by-side. The texture map for each view contains a viewport that defines the boundaries of that view’s content. The type of each texture is [`MTLTextureType.type2D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2D).

## See Also

- [LayerRenderer.Layout.dedicated](layerrenderer/layout/dedicated.md)
  A layout that assigns a separate texture to each rendered view.
- [LayerRenderer.Layout.layered](layerrenderer/layout/layered.md)
  A layout that specifies each view’s content as a slice of a single texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout/shared)*