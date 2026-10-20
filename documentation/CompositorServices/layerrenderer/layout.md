# LayerRenderer.Layout

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the organization of the textures you use for drawing.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum Layout
```

```c
enum cp_layer_renderer_layout : uint32_t;
```

## Topics

### Getting the texture layouts
- [LayerRenderer.Layout.dedicated](./layout/dedicated.md)
  A layout that assigns a separate texture to each rendered view.
- [LayerRenderer.Layout.shared](./layout/shared.md)
  A layout that uses a single texture to store the content for all rendered views.
- [LayerRenderer.Layout.layered](./layout/layered.md)
  A layout that specifies each view’s content as a slice of a single texture.
### Initializers
- [init?(rawValue: UInt32)](./layout/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the texture layout
- [var layout: LayerRenderer.Layout](./configuration-swift.struct/layout.md)
  The layout being used by the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/layout)*