# layers

**Framework**: RealityKit  
**Kind**: property

The layers of entities that cast shadows from this light.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var layers: RenderLayer.Set? { get set }
```

#### Discussion

An entity casts a shadow into this light’s shadow map when the layers of its [`RenderLayerComponent`](renderlayercomponent.md) intersect with this set.

Set this property to:

- `nil` (the default) to inherit [`layers`](spotlightcomponent/layers.md), so any entity the light illuminates can also cast a shadow from it.
- An empty set to disable shadow casting from this light entirely.

Shadow casting can be restricted by layer on devices with Apple6 GPU family feature support.

## See Also

- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
- [init(layers: RenderLayer.Set?)](spotlightcomponent/shadow/init(layers:).md)
  Creates a spot light shadow that accepts shadow casters from the specified layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/layers)*