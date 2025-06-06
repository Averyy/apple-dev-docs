# ForceEffect

**Framework**: RealityKit  
**Kind**: struct

Defines a force effect’s system, and type specific properties.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ForceEffect<ForceEffectType> where ForceEffectType : ForceEffectProtocol
```

#### Overview

This struct wraps your custom force effect that conforms to [`ForceEffectProtocol`](forceeffectprotocol.md) and provides properties that are common to all force effects.

## Topics

### Initializers
- [init(effect: ForceEffectType, strengthScale: Double, spatialFalloff: SpatialForceFalloff?, timedFalloff: TimedForceFalloff?, position: SIMD3<Float>, orientation: simd_quatf, mask: CollisionGroup)](forceeffect/init(effect:strengthscale:spatialfalloff:timedfalloff:position:orientation:mask:).md)
  Creates a ForceEffect struct.
### Instance Properties
- [var effect: ForceEffectType](forceeffect/effect.md)
  Parameters that can vary for different types.
- [var mask: CollisionGroup](forceeffect/mask.md)
  Controls which collision groups will be affected by this force effect.
- [var orientation: simd_quatf](forceeffect/orientation.md)
  Rotation of the force effect relative to the effect’s transform component.
- [var position: SIMD3<Float>](forceeffect/position.md)
  Position of the force effect relative to the effect’s transform component.
- [var spatialFalloff: SpatialForceFalloff?](forceeffect/spatialfalloff.md)
  Optional strength falloff based on the spatial bounds of the effect.
- [var strengthScale: Float](forceeffect/strengthscale.md)
  A multiplier that scales the strength of the effect.
- [var timedFalloff: TimedForceFalloff?](forceeffect/timedfalloff.md)
  Optional strength falloff based on the duration of the effect.

## Relationships

### Conforms To
- [ForceEffectBase](forceeffectbase.md)

## See Also

- [struct ForceEffectComponent](forceeffectcomponent.md)
  A component that defines the forces that affect an entity, including custom forces that you define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffect)*