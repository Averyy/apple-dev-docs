# VortexForceEffect

**Framework**: RealityKit  
**Kind**: struct

A force effect whose forces circulate around an axis centered at the origin of the effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct VortexForceEffect
```

## Topics

### Initializers
- [init(strength: Double, axis: SIMD3<Float>)](vortexforceeffect/init(strength:axis:).md)
  Creates a vortex force effect.
### Instance Properties
- [let axis: SIMD3<Float>](vortexforceeffect/axis.md)
  The vortex’s rotational axis centered at the origin of the effect.
- [var forceMode: ForceMode](vortexforceeffect/forcemode.md)
  The type of force this effect applies.
- [var parameterTypes: PhysicsBodyParameterTypes](vortexforceeffect/parametertypes.md)
  The input rigid body parameters.
- [let strength: Float](vortexforceeffect/strength.md)
  The magnitude of the force.
### Instance Methods
- [func update(parameters: inout ForceEffectParameters)](vortexforceeffect/update(parameters:).md)
  Calculates the vortex forces for rigid bodies from the force effect.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [ForceEffectProtocol](forceeffectprotocol.md)

## See Also

- [struct ConstantForceEffect](constantforceeffect.md)
  A force effect that exerts a constant force in a direction relative to the effect’s transform.
- [struct ConstantRadialForceEffect](constantradialforceeffect.md)
  A force effect that pulls objects toward its center with a constant strength.
- [struct DragForceEffect](dragforceeffect.md)
  A force effect that slows bodies within its area of effect with a force proportional to the body’s velocity.
- [struct RadialForceEffect](radialforceeffect.md)
  A force effect that pulls objects toward its center with a spring-like (distance dependent) force.
- [struct TurbulenceForceEffect](turbulenceforceeffect.md)
  A force effect that applies random forces with magnitudes proportional to each body’s velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/vortexforceeffect)*