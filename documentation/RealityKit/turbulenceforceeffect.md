# TurbulenceForceEffect

**Framework**: RealityKit  
**Kind**: struct

A force effect that applies random forces with magnitudes proportional to each body’s velocity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct TurbulenceForceEffect
```

## Topics

### Initializers
- [init(strength: Double, smoothness: Double, speed: Double)](turbulenceforceeffect/init(strength:smoothness:speed:).md)
  Creates a turbulence force effect.
### Instance Properties
- [var forceMode: ForceMode](turbulenceforceeffect/forcemode.md)
  The type of force this effect applies.
- [var parameterTypes: PhysicsBodyParameterTypes](turbulenceforceeffect/parametertypes.md)
  The input rigid body parameters.
- [let smoothness: Float](turbulenceforceeffect/smoothness.md)
  A smoothing factor that applies to the force, reducing randomness.
- [let speed: Float](turbulenceforceeffect/speed.md)
  The effect’s variation over time.
- [let strength: Float](turbulenceforceeffect/strength.md)
  The magnitude of the force.
### Instance Methods
- [func update(parameters: inout ForceEffectParameters)](turbulenceforceeffect/update(parameters:).md)
  Calculates the turbulence forces for rigid bodies from the force effect.

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
- [struct VortexForceEffect](vortexforceeffect.md)
  A force effect whose forces circulate around an axis centered at the origin of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/turbulenceforceeffect)*