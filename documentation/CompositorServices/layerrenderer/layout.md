# LayerRenderer.Layout

**Framework**: Compositor Services  
**Kind**: enum

Constants that specify the organization of the textures you use for drawing.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Layout
```

## Topics

### Getting the texture layouts
- [LayerRenderer.Layout.dedicated](layerrenderer/layout/dedicated.md)
  A layout that assigns a separate texture to each rendered view.
- [LayerRenderer.Layout.shared](layerrenderer/layout/shared.md)
  A layout that uses a single texture to store the content for all rendered views.
- [LayerRenderer.Layout.layered](layerrenderer/layout/layered.md)
  A layout that specifies each view’s content as a slice of a single texture.
### Initializers
- [init?(rawValue: UInt32)](layerrenderer/layout/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var layout: LayerRenderer.Layout](layerrenderer/configuration-swift.struct/layout.md)
  The layout being used by the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout)*