# init(configuration:renderer:)

**Framework**: Compositor Services  
**Kind**: init

Creates a [`CompositorLayer`](compositorlayer.md) instance.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
nonisolated
init(configuration: any CompositorLayerConfiguration = .default, renderer: @escaping @MainActor (LayerRenderer) -> Void)
```

## Parameters

- `configuration`: The configuration to use when creating the LayerRenderer.
- `renderer`: A closure that receives the layer to use when rendering   the content for the immersive space


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/compositorlayer/init(configuration:renderer:)-2uxn7)*