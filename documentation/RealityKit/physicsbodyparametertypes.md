# PhysicsBodyParameterTypes

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines which rigid body inputs are required by a force effect’s update handler.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsBodyParameterTypes
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./physicsbodyparametertypes/init%28rawvalue%29.md)
### Instance Properties
- [let rawValue: UInt32](./physicsbodyparametertypes/rawvalue.md)
  The backing storage for force effect inputs.
### Type Properties
- [static let angularVelocity: PhysicsBodyParameterTypes](./physicsbodyparametertypes/angularvelocity.md)
  The angular velocity of each rigid body.
- [static let distance: PhysicsBodyParameterTypes](./physicsbodyparametertypes/distance.md)
  The distance of each rigid body from the effect origin.
- [static let inertiaTensor: PhysicsBodyParameterTypes](./physicsbodyparametertypes/inertiatensor.md)
  The inertia tensor of each rigid body.
- [static let mass: PhysicsBodyParameterTypes](./physicsbodyparametertypes/mass.md)
  The mass of each rigid body,
- [static let orientation: PhysicsBodyParameterTypes](./physicsbodyparametertypes/orientation.md)
  The orientation of each rigid body relative to the effect orientation.
- [static let position: PhysicsBodyParameterTypes](./physicsbodyparametertypes/position.md)
  The center of mass of each rigid body relative to the effect origin.
- [static let velocity: PhysicsBodyParameterTypes](./physicsbodyparametertypes/velocity.md)
  The linear velocity of each rigid body.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Updating effects
- [func update(parameters: inout ForceEffectParameters)](./forceeffectprotocol/update%28parameters%29.md)
  Defines how the custom force effect computes forces at each physics simulation step.
- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](./forceeffectprotocol/register%28_%29-1zt9t.md)
  Registers the custom effect.
- [struct ForceEffectParameters](./forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct ForceEffectEvent](./forceeffectevent.md)
  A struct that defines the arguments to the custom force effect update closure.
- [struct UnsafeForceEffectBuffer](./unsafeforceeffectbuffer.md)
  Provides access to physics body parameters from the effect’s update function or event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodyparametertypes)*