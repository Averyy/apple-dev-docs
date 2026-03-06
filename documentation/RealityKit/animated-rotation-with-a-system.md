# Animating entity rotation with a system

**Framework**: RealityKit

Rotate an entity around an axis using a Component and a System.

**Availability**:
- visionOS 2.0+
- Xcode 16.3+

#### Overview

You can use the Entity Component System (ECS) from RealityKit to apply logic to any number of entities in a scene. This sample code provides a component. The system queries scene for all entities that have that component and then rotates those entities based on the speed and axis in the component.

For more information about the ECS, see [`Understanding the modular architecture of RealityKit`](https://developer.apple.com/documentation/visionOS/understanding-the-realitykit-modular-architecture), and for more information about systems, see [`Implementing systems for entities in a scene`](implementing-systems-for-entities-in-a-scene.md).

##### Add the Rotation Component to the Entity

After creating the entity in `ContentView` the sample adds an instance of the `RotationComponent` to the entity:

```swift
telescopeScene.components[RotationComponent.self] = RotationComponent()
```

By default, the rotation speed is `0.0` and the axis of rotation is the x-axis.

##### Enable Swiftui to Control the Animation

The `ContentView` type has two `@State` variables that control the animation:

```swift
@State var axis: RotationAxis = .x
@State var rotating: Bool = false
```

- `RotationAxis` is an enumeration with one case for each ordinal direction.
- The `rotating` value sets the `speed` to `0.0` when `rotating` is `false`, and `1.0` when `rotating` is `true`.

##### Update the Realitykit State on Swiftui State Changes

The system calls the `RealityView` `update:` block when the `rotating` or `speed` values change.

```swift
update: { context in
  telescope?.components[RotationComponent.self]?.rotationAxis = axis
  telescope?.components[RotationComponent.self]?.speed = rotating ? 1.0 : 0.0
}
```

##### Update the Rotation of the Entity on Every Frame

The framework calls the `RotationSystem` function [`update(context:)`](System/update(context:).md) for each frame. The sample includes a query to quickly find entities that have the component:

```swift
static let rotationQuery = EntityQuery(where: .has(RotationComponent.self))
```

This function uses `rotationQuery` to find relevant entities. The function then sets the orientation of the entities based on the values in the attached component:

```swift
for entity in context.entities(matching: Self.rotationQuery, updatingSystemWhen: .rendering) {
  guard let component: RotationComponent = entity.components[RotationComponent.self] else { continue }
  if component.speed == 0 { continue }
  entity.setOrientation(simd_quatf(angle: component.speed * Float(context.deltaTime),
                                   axis: component.axis),
                        relativeTo: entity)
}
```

While the component’s `speed` value isn’t zero, the system animates the entity’s rotation around `axis`.

The `relativeTo:` argument specifies what coordinate system the rotation acts in. Specifying `entity` here rotates the entity around its own coordinate system. In this sample there is only one entity. In a more complex scene many interesting effects are achieved by rotating in a different coordinate system.

## See Also

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)
  Apply behaviors and physical effects to the objects and characters in a RealityKit scene with the Entity Component System (ECS).
- [protocol System](system.md)
  An object that affects multiple entities in every update of a RealityKit scene.
- [struct SystemUpdateCondition](systemupdatecondition.md)
  A condition which causes a system to update.
- [struct SceneUpdateContext](sceneupdatecontext.md)
  An object that contains information about the scene to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animated-rotation-with-a-system)*