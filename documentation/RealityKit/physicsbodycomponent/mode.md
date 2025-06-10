# mode

**Framework**: RealityKit  
**Kind**: property

The behavioral mode that controls the way the physics body moves and interacts with other physics bodies in a simulation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var mode: PhysicsBodyMode
```

#### Discussion

The property’s default value is [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md), which means the physics body responds to forces and can collide with all other physics bodies in the simulation.

> ❗ **Important**: Improve the performance of your app by applying `dynamic` mode to the physics bodies for just entities that need to interact with all other physics bodies, because each dynamic physics body can be computationally expensive.

To configure the physics body so that an entity can move around the simulation without reacting to forces, set the property to [`PhysicsBodyMode.kinematic`](physicsbodymode/kinematic.md). Apps typically use kinematic mode for entities the app programmatically controls, such as in response to a control or a person’s interaction. For entities that don’t need to move at all, set its physics body’s mode to [`PhysicsBodyMode.static`](physicsbodymode/static.md).

Physics bodies in `static` or `kinematic` mode can’t collide with other physics bodies with either mode, by default. Optionally, you can add collision support for entities that have a physics body in either static or kinematic mode by adding a [`PhysicsSimulationComponent`](physicssimulationcomponent.md) to an entity that’s a common ancestor to the entities you want to collide. Then you can set [`PhysicsSimulationComponent.CollisionOptions`](physicssimulationcomponent/collisionoptions-swift.struct.md) to your preference.

You can change the mode of an entity’s physics body at any time, but changing it from `static` to another mode can affect your app’s performance because the transition to a non-static mode can trigger the simulation to rebuild its state.

> 💡 **Tip**: Set the mode of an entity’s physics body to `static` if you know the entity doesn’t ever need to move; otherwise, set the mode to `kinematic` or `dynamic`, even if the entity isn’t currently moving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/mode)*