# defaultLayer

**Framework**: RealityKit  
**Kind**: property

A render layer component that contains only [`defaultLayer`](renderlayer/defaultlayer.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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