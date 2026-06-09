# layers

**Framework**: RealityKit  
**Kind**: property

The layers this entity participates in.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var layers: RenderLayer.Set
```

#### Discussion

Layers can be either named custom layers or the default layer. Common conventions include:

- `.defaultLayer` for general entities
- `RenderLayer("com.myapp.hero")` for main character objects
- `RenderLayer("com.myapp.background")` for background elements
- `RenderLayer("com.myapp.props")` for scene props

## See Also

- [static let defaultLayer: RenderLayerComponent](renderlayercomponent/defaultlayer.md)
  The default layer used when no `RenderLayerComponent` is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayercomponent/layers)*