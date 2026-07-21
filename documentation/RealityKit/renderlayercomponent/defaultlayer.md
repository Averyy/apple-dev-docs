# defaultLayer

**Framework**: RealityKit  
**Kind**: property

A render layer component that contains only [`defaultLayer`](renderlayer/defaultlayer.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let defaultLayer: RenderLayerComponent
```

#### Discussion

RealityKit treats entities without an explicit [`RenderLayerComponent`](renderlayercomponent.md) as if they had this component.

## See Also

- [var layers: RenderLayer.Set](renderlayercomponent/layers.md)
  The layers this entity participates in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayercomponent/defaultlayer)*