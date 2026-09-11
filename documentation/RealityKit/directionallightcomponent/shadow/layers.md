# layers

**Framework**: RealityKit  
**Kind**: property

The layers of entities that cast shadows from this light.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var layers: RenderLayer.Set? { get set }
```

#### Discussion

An entity casts a shadow into this light’s shadow map when the layers of its [`RenderLayerComponent`](renderlayercomponent.md) intersect with this set.

Set this property to:

- `nil` (the default) to inherit [`layers`](directionallightcomponent/layers.md), so any entity the light illuminates can also cast a shadow from it.
- An empty set to disable shadow casting from this light entirely.

Shadow casting can be restricted by layer on devices with Apple6 GPU family feature support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/layers)*