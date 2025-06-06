# init(components:)

**Framework**: RealityKit  
**Kind**: init

Creates an entity with one or multiple components.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init<each T>(components: repeat each T) where repeat each T : Component
```

#### Discussion

The components you specify in this initializer override any default components of the same type that RealityKit creates the entity with, such as [`Transform`](transform.md).

For example, you can use this initializer to create an entity that has a [`SpotLightComponent`](spotlightcomponent.md):

```swift
let spotlightEntity = Entity(components: SpotLightComponent())
```

You can also create an entity with multiple initial components, such as a [`ModelComponent`](modelcomponent.md) and a [`Transform`](transform.md):

```swift
let sphereEntity = Entity(
    components: ModelComponent(mesh: .generateBox(size: 1), materials: []),
                Transform(translation: [0, 0.5, 0])
)
```

> **Note**: You can change any of the entity’s components at any time by modifying the entity’s [`components`](entity/components.md) set.

You can change any of the entity’s components at any time by modifying the entity’s [`components`](entity/components.md) set.

## Parameters

- `components`: A comma-delimited list of components to add to the entity.

## See Also

- [init()](entity/init.md)
  Creates a new entity.
- [convenience init(components: [any Component])](entity/init(components:)-41rn1.md)
  Creates an entity with multiple components.
- [func clone(recursive: Bool) -> Self](entity/clone(recursive:).md)
  Duplicates an entity to create a new entity.
- [func didClone(from: Entity)](entity/didclone(from:).md)
  Tells a newly cloned entity that cloning is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init(components:)-80z41)*