# ForceEffectComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines the forces that affect an entity, including custom forces that you define.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ForceEffectComponent
```

#### Overview

After you assign a `ForceEffectComponent` to an entity, the force effects in the component apply each physics update for as long as the component and force effects exist. Each [`ForceEffect`](forceeffect.md) updates sequentially while the physics system accumulates its forces. The center frame of each [`ForceEffect`](forceeffect.md) coincides with and moves alongside the entity’s position and orientation. To offset this center frame, set the position and orientation.

> **Note**: You can set the [`simulationState`](forceeffectcomponent/simulationstate-swift.property.md) parameter to [`ForceEffectComponent.SimulationState.pause`](forceeffectcomponent/simulationstate-swift.enum/pause.md) if you want to apply forces later.

##### Create Forces

Use [`ConstantForceEffect`](constantforceeffect.md) to apply a constant force in a direction:

```swift
let constantForceEffect = ForceEffect(effect: ConstantForceEffect(strength: 1, direction: [1, 0, 0]))
```

RealityKit provides a set of useful forces you can use with `ForceEffectComponent`:

- [`ConstantForceEffect`](constantforceeffect.md)
- [`ConstantRadialForceEffect`](constantradialforceeffect.md)
- [`DragForceEffect`](dragforceeffect.md)
- [`RadialForceEffect`](radialforceeffect.md)
- [`TurbulenceForceEffect`](turbulenceforceeffect.md)
- [`VortexForceEffect`](vortexforceeffect.md)

##### Create Custom Forces

To create a custom force effect, define a structure that implements [`ForceEffectProtocol`](forceeffectprotocol.md), then create an instance of [`ForceEffectBase`](forceeffectbase.md) with your custom `ForceEffectProtocol` implementation:

```swift
// CustomForce implements ForceEffectProtocol, and has a custom parameter, thrustersActive, that determines how the system applies your force to a physics body.
let thrusterForce = CustomForce(thrustersActive: true)
// Create an instance of ForceEffectBase using your custom force.
let thursterForceEffect = ForceEffect(effect: thrusterForce)
```

> **Note**: To apply force to a physics body with a custom `ForceEffectProtocol`, you must implement and apply forces in [`update(parameters:)`](forceeffectprotocol/update(parameters:).md).

##### Apply Forces

You can apply multiple forces to your entity at once by including them in `ForceEffectComponent`:

```swift
let forceEffectComponent = ForceEffectComponent(effects: [constantForceEffect, thrusterForceEffect])
entity.components.set(forceEffectComponent)
```

## Topics

### Initializers
- [init(effect: any ForceEffectBase)](forceeffectcomponent/init(effect:).md)
  Creates a force effect component with a single force effect, and automatically plays it.
- [init(effects: [any ForceEffectBase], simulationState: ForceEffectComponent.SimulationState)](forceeffectcomponent/init(effects:simulationstate:).md)
  Creates a force effect component.
### Instance Properties
- [var effects: [any ForceEffectBase]](forceeffectcomponent/effects.md)
  One or more effects used to simulate forces.
- [var simulationState: ForceEffectComponent.SimulationState?](forceeffectcomponent/simulationstate-swift.property.md)
  The desired state of the simulation.
### Enumerations
- [ForceEffectComponent.SimulationState](forceeffectcomponent/simulationstate-swift.enum.md)
  The simulation runtime states.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ForceEffect](forceeffect.md)
  Defines a force effect’s system, and type specific properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectcomponent)*