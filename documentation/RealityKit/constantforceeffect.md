# ConstantForceEffect

**Framework**: RealityKit  
**Kind**: struct

A force effect that exerts a constant force in a direction relative to the effect’s transform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ConstantForceEffect
```

## Topics

### Initializers
- [init(from: any Decoder) throws](constantforceeffect/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(strength: Double, direction: SIMD3<Float>)](constantforceeffect/init(strength:direction:).md)
  Creates a constant force effect.
### Instance Properties
- [let direction: SIMD3<Float>](constantforceeffect/direction.md)
  The direction of the force relative to the effect’s transform.
- [var forceMode: ForceMode](constantforceeffect/forcemode.md)
  The type of force this effect applies.
- [var parameterTypes: PhysicsBodyParameterTypes](constantforceeffect/parametertypes.md)
  The input rigid body parameters.
- [let strength: Float](constantforceeffect/strength.md)
  The magnitude of the force.
### Instance Methods
- [func encode(to: any Encoder) throws](constantforceeffect/encode(to:).md)
  Encodes this value into the given encoder.
- [func update(parameters: inout ForceEffectParameters)](constantforceeffect/update(parameters:).md)
  Calculates the constant forces for rigid bodies from the force effect.
### Default Implementations
- [ForceEffectProtocol Implementations](constantforceeffect/forceeffectprotocol-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [ForceEffectProtocol](forceeffectprotocol.md)

## See Also

- [struct ConstantRadialForceEffect](constantradialforceeffect.md)
  A force effect that pulls objects toward its center with a constant strength.
- [struct DragForceEffect](dragforceeffect.md)
  A force effect that slows bodies within its area of effect with a force proportional to the body’s velocity.
- [struct RadialForceEffect](radialforceeffect.md)
  A force effect that pulls objects toward its center with a spring-like (distance dependent) force.
- [struct TurbulenceForceEffect](turbulenceforceeffect.md)
  A force effect that applies random forces with magnitudes proportional to each body’s velocity.
- [struct VortexForceEffect](vortexforceeffect.md)
  A force effect whose forces circulate around an axis centered at the origin of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/constantforceeffect)*