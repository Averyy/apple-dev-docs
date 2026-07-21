# layers

**Framework**: RealityKit  
**Kind**: property

The layers this light illuminates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var layers: RenderLayer.Set { get set }
```

#### Discussion

A spotlight illuminates an entity when the layers of the entity’s [`RenderLayerComponent`](renderlayercomponent.md) intersect with this set. Entities without a [`RenderLayerComponent`](renderlayercomponent.md) belong to [`defaultLayer`](renderlayer/defaultlayer.md), which is the only member of `layers` by default.

For an example of layer-based light linking, see [`layers`](directionallightcomponent/layers.md).

Lights can be restricted by layer on devices with Apple6 GPU family feature support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/layers)*