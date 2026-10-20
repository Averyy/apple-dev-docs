# init(configuration:renderer:)

**Framework**: Compositor Services  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
init(configuration: any CompositorLayerConfiguration = .default, renderer: @escaping @MainActor (LayerRenderer, NWEndpoint?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/compositorlayer/init(configuration:renderer:)-81vbz)*