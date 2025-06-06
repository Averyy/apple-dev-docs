# ForceEffectBase

**Framework**: RealityKit  
**Kind**: protocol

The base protocol for the wrapping force effect structure containing common parameters for all force-effects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol ForceEffectBase
```

#### Overview

Don’t implement this protocol yourself. Create force effects by calling methods on [`ForceEffect`](forceeffect.md).

## Topics

### Associated Types
- [associatedtype ForceEffectType : ForceEffectProtocol](forceeffectbase/forceeffecttype.md)
  A type that represents the kind of force effect.
### Instance Properties
- [var effect: Self.ForceEffectType](forceeffectbase/effect.md)
  Custom force effect parameters.
- [var mask: CollisionGroup](forceeffectbase/mask.md)
  Controls which collision groups will be affected by this force effect.
- [var orientation: simd_quatf](forceeffectbase/orientation.md)
  Rotation of the force effect relative to the effect’s transform component.
- [var position: SIMD3<Float>](forceeffectbase/position.md)
  Position of the force effect relative to the effect’s transform component.
- [var spatialFalloff: SpatialForceFalloff?](forceeffectbase/spatialfalloff.md)
  Optional strength falloff based on the spatial bounds of the effect.
- [var strengthScale: Float](forceeffectbase/strengthscale.md)
  A multiplier that scales the strength of the effect.
- [var timedFalloff: TimedForceFalloff?](forceeffectbase/timedfalloff.md)
  Optional strength falloff based on the duration of the effect.

## Relationships

### Conforming Types
- [ForceEffect](forceeffect.md)

## See Also

- [protocol ForceEffectProtocol](forceeffectprotocol.md)
  A protocol that defines a custom force effect.
- [enum ForceMode](forcemode.md)
  The options that control how physics system applies the forces.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectbase)*