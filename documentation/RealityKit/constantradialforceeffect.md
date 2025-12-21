# ConstantRadialForceEffect

**Framework**: RealityKit  
**Kind**: struct

A force effect that pulls objects toward its center with a constant strength.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ConstantRadialForceEffect
```

#### Overview

This force’s magnitude is constant and does not depend on objects’ distances to the effect origin.

## Topics

### Initializers
- [init(strength: Double)](constantradialforceeffect/init(strength:).md)
  Creates a radial force effect with constant magnitude.
### Instance Properties
- [var forceMode: ForceMode](constantradialforceeffect/forcemode.md)
  The type of force this effect applies.
- [var parameterTypes: PhysicsBodyParameterTypes](constantradialforceeffect/parametertypes.md)
  The input rigid body parameters.
- [let strength: Float](constantradialforceeffect/strength.md)
  The magnitude of the force.
### Instance Methods
- [func update(parameters: inout ForceEffectParameters)](constantradialforceeffect/update(parameters:).md)
  Calculates the radial forces with constant magnitude for rigid bodies from the force effect.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [ForceEffectProtocol](forceeffectprotocol.md)

## See Also

- [struct ConstantForceEffect](constantforceeffect.md)
  A force effect that exerts a constant force in a direction relative to the effect’s transform.
- [struct DragForceEffect](dragforceeffect.md)
  A force effect that slows bodies within its area of effect with a force proportional to the body’s velocity.
- [struct RadialForceEffect](radialforceeffect.md)
  A force effect that pulls objects toward its center with a spring-like (distance dependent) force.
- [struct TurbulenceForceEffect](turbulenceforceeffect.md)
  A force effect that applies random forces with magnitudes proportional to each body’s velocity.
- [struct VortexForceEffect](vortexforceeffect.md)
  A force effect whose forces circulate around an axis centered at the origin of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/constantradialforceeffect)*