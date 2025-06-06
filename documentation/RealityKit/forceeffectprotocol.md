# ForceEffectProtocol

**Framework**: RealityKit  
**Kind**: protocol

A protocol that defines a custom force effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol ForceEffectProtocol
```

#### Overview

A custom force effect is a function of a set of input rigid body attributes and returns force-like vector quantities. You can declare this custom force effect’s input types ([`parameterTypes`](forceeffectprotocol/parametertypes.md)) and output types ([`forceMode`](forceeffectprotocol/forcemode.md)) by conforming to `ForceEffectProtocol`.

For example, you can declare a custom force effect that depends on rigid bodies’ position and mass, and computes acceleration for each rigid body.

```swift
struct MyCustomForce : ForceEffectProtocol {
    var parameterTypes: PhysicsBodyParameterTypes { [.position, .mass] }
    var forceMode: ForceMode = .acceleration
    func update(parameters: inout ForceEffectParameters) {
    }
}
```

Register your custom force effect to enable the physics system to compute forces affected by rigid bodies.

```swift
MyCustomForce.register()
```

At each physics update, the [`update(parameters:)`](forceeffectprotocol/update(parameters:).md) method receives the declared inputs from [`ForceEffectParameters`](forceeffectparameters.md). You can set the output forces for each rigid body with [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md).

Sometimes, you may need to access properties from both your custom force effect and the current context while computing forces in the update function. The [`register(_:)`](forceeffectprotocol/register(_:)-1zt9t.md) method accepts an optional closure that allows you to capture the necessary properties. If you provide this closure to the register method, the update method is not required.

```swift
struct MyCustomForceClosure: ForceEffectProtocol {
    var forceMode: RealityFoundation.ForceMode = .force
    var parameterTypes: PhysicsBodyParameterTypes { [.position, .mass] }
    let customProperty: Double = 1
}

let contextualProperty: Double = 1

MyCustomForceClosure.register { event in
    // Access the effect property via `event.effect.customProperty`.
    // Access the input rigid body attributes via `event.parameters`.
    // Access the contextual property directly by `contextualProperty`.
}
```

## Topics

### Updating effects
- [func update(parameters: inout ForceEffectParameters)](forceeffectprotocol/update(parameters:).md)
  Defines how the custom force effect computes forces at each physics simulation step.
- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](forceeffectprotocol/register(_:)-1zt9t.md)
  Registers the custom effect.
- [struct PhysicsBodyParameterTypes](physicsbodyparametertypes.md)
  Defines which rigid body inputs are required by a force effect’s update handler.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct ForceEffectEvent](forceeffectevent.md)
  A struct that defines the arguments to the custom force effect update closure.
- [struct UnsafeForceEffectBuffer](unsafeforceeffectbuffer.md)
  Provides access to physics body parameters from the effect’s update function or event handler.
### Instance Properties
- [var forceMode: ForceMode](forceeffectprotocol/forcemode.md)
  The mode that controls how the physics system interprets the outputs from a user’s custom force computation.
- [var parameterTypes: PhysicsBodyParameterTypes](forceeffectprotocol/parametertypes.md)
  The input types to user’s custom force computation.
### Type Methods
- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](forceeffectprotocol/register(_:)-96fsp.md)
  Register the codable custom effect. If a handler is specified, the closure is used to update the effect.

## Relationships

### Conforming Types
- [ConstantForceEffect](constantforceeffect.md)
- [ConstantRadialForceEffect](constantradialforceeffect.md)
- [DragForceEffect](dragforceeffect.md)
- [RadialForceEffect](radialforceeffect.md)
- [TurbulenceForceEffect](turbulenceforceeffect.md)
- [VortexForceEffect](vortexforceeffect.md)

## See Also

- [enum ForceMode](forcemode.md)
  The options that control how physics system applies the forces.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [protocol ForceEffectBase](forceeffectbase.md)
  The base protocol for the wrapping force effect structure containing common parameters for all force-effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectprotocol)*