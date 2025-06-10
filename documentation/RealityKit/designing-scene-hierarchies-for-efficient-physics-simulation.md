# Designing scene hierarchies for efficient physics simulation

**Framework**: RealityKit

Configure your RealityKit scenes to avoid performance bottlenecks.

#### Overview

[`RealityKit`](RealityKit.md) simulates physical interactions between the virtual objects in your scene, as well as between virtual objects and detected surfaces in the real world, such as floors, walls, or tabletops. On iOS devices with a LiDAR Scanner, RealityKit can even simulate interactions between virtual objects and scanned real-world geometry.

Simulating real-world physics can be computationally expensive, however, so set up your project to maximize performance.

##### Design Scenes with Flat Hierarchies

Make sure every entity in your scene that participates in the physics simulation is a child of the scene root, if possible, and avoid having unnecessary entities in your scene hierarchy.

For scenes created in Reality Composer, minimize the use of groups for objects that participate in the physics simulation. Grouping objects creates implicit parent-child relationships and invisible parent entities, both of which can negatively impact performance.

> ❗ **Important**: Although RealityKit performs better with shallow scene hierarchies, don’t flatten or otherwise modify the hierarchy of Reality Composer scenes. Reality Composer stores references to entities based on their location in the scene hierarchy. Flattening the hierarchy at runtime breaks those references.

##### Assign a Physics Origin

By default, RealityKit uses the scene’s root entity as the origin of the physics simulation and simulates objects at their actual size. You can alternatively designate a different entity in your scene to be the  by using the [`physicsOrigin`](arview/physicsorigin.md) property of your [`ARView`](arview.md). Designating an entity as the physics origin means that all physics calculations are relative to the specified entity rather than the scene’s root entity. For more information about when to specify a separate physics origin, see [`Handling different-sized objects in physics simulations`](handling-different-sized-objects-in-physics-simulations.md).

```swift
arView.physicsOrigin = entity
```

When you set the physics origin, you can modify the scale, position, and orientation of the scene in the view without affecting the physics simulation. You can also use transform values that are different from the values used in the visible scene. For example, you can create a tabletop AR experience with characters that are a few inches tall but behave as if they’re much larger.

> ❗ **Important**: Set the [`physicsOrigin`](arview/physicsorigin.md) before you add entities to your scene. Unpredictable behavior can occur if you change the physics origin in a scene after the simulation begins.

You can’t specify a different physics origin using Reality Composer. Instead, designate an entity in a loaded Reality Composer scene as the physics entity or add a new entity to the loaded scene to act as the physics origin.

This example shows how to retrieve a named entity from your Reality Composer scene and specify it as the physics origin:

```swift
    let boxAnchor = try! Experience.loadBox()
    arView.scene.anchors.append(boxAnchor)
    if let physicsRoot = boxAnchor.findEntity(named: "Physics Root") {
        self.arView.physicsOrigin = physicsRoot
    }
```

##### Prefer Impulses Over Forces

RealityKit provides two different mechanisms for applying force to an entity:  and . An impulse represents a constant amount of force applied over a specific unit of time. RealityKit applies forces for the entire duration of the current frame, but it applies an impulse all at once. Using forces gives different results depending on the current rendering framerate, while applying an impulse gives consistent results regardless of the framerate. Using impulses results in consistent, predictable behavior on any device at any frame rate.

Additionally, the effect of adding a force isn’t visible until after the next simulation update occurs, while the result of applying an impulse is visible immediately.

##### Apply Forces and Impulses Relative to the Physics Origin

When changing velocities or applying forces or impulses to simulated objects, apply the changes relative to the physics origin. Specifying units relative to the physics origin eliminates the need to account for scale changes made to the rendered scene.

[`PhysicsMotionComponent`](physicsmotioncomponent.md) internally stores velocity values relative to the physics origin. Specifying forces and impulses relative to the physics origin eliminates the need for the physics engine to convert or translate values and therefore results in better performance.

```swift
// Apply impulse to shoot the object up.
let impulseStrength = 10
let impulseDirection = SIMD3<Float>(0, 1, 0)
model.applyLinearImpulse(impulseStrength * impulseDirection, relativeTo: arView.physicsOrigin)
```

##### Avoid Extreme Differences in Size and Mass

RealityKit’s physics simulations work best if the size and mass ratios don’t exceed one order of magnitude.

- The largest object in your scene should be no more than 10 times the size of the smallest object.
- The heaviest object in your scene should be no more than 10 times the mass of your lightest object.

Additionally, the physics simulation works best if the smallest dimension of each object is at least `0.05` units in size and the largest dimension of each object is no more than `10` units in size. If you need objects outside of this range, create objects that are inside this range and then scale the physics origin at runtime.

##### Increase Density Instead of Mass

For best results, keep the mass of your scene’s objects at their calculated mass. Entities with substantially increased mass result in a proportional increase in momentum, which can make the physics simulation unstable. To simulate heavy, dense objects like gold or lead, leave the mass at its calculated value and increase the entity’s density property. The pre-defined physics materials available in Reality Composer use density to simulate heavy materials.

```swift
// Use the initializer with density instead of mass.
model.physicsBody = .init(shapes: [boxShape], density: 200)
```

The [`init(shapes:density:material:mode:)`](physicsbodycomponent/init(shapes:density:material:mode:).md) initializer automatically computes mass based on volume and density, Water has a density of about 1000 kg/m³ and steel has a density of 7800 kg/m³. When setting the mass of an object, keep in mind that real-world objects aren’t always completely solid, and can be hollow. Densities of less than 1000 kg/m³ work well in most scenarios.

## See Also

- [Handling different-sized objects in physics simulations](handling-different-sized-objects-in-physics-simulations.md)
  Set up a scene hierarchy for accurate physics simulations.
- [struct PhysicsSimulationComponent](physicssimulationcomponent.md)
  A component that controls localized physics simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/designing-scene-hierarchies-for-efficient-physics-simulation)*