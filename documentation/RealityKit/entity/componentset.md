# Entity.ComponentSet

**Framework**: RealityKit  
**Kind**: struct

A collection of components that an entity stores.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct ComponentSet
```

#### Overview

A `ComponentSet` represents all the components that an entity holds. Use this set to add, remove, and update components on an entity. This set can hold one component of each type.

Access the `ComponentSet` of an [`Entity`](entity.md) using its [`components`](entity/components.md) property.

`ComponentSet` conforms to [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence), allowing you to iterate over it to access and use each component, as the example below shows:

```swift
for component in entity.components {
    print(component)
}
```

## Topics

### Updating the set
- [func set<T>(T)](entity/componentset/set(_:)-8sii2.md)
  Adds a new component to the set, or overrides an existing one.
- [func set([any Component])](entity/componentset/set(_:)-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func remove(any Component.Type)](entity/componentset/remove(_:).md)
  Removes the component of the specified type from the collection.
- [func removeAll()](entity/componentset/removeall.md)
  Removes all components from the collection.
### Accessing members
- [subscript<T>(T.Type) -> T?](entity/componentset/subscript(_:)-5wdsf.md)
  Gets or sets the component of the specified type.
- [subscript(any Component.Type) -> (any Component)?](entity/componentset/subscript(_:)-47rhg.md)
  Gets or sets the component with a specific dynamically supplied type.
### Counting members
- [var count: Int](entity/componentset/count.md)
  The number of components in the collection.
### Checking for membership
- [func has(any Component.Type) -> Bool](entity/componentset/has(_:).md)
  Returns a Boolean value that indicates whether the set contains a component of the given type.
### Default Implementations
- [Collection Implementations](entity/componentset/collection-implementations.md)
- [Sequence Implementations](entity/componentset/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var components: Entity.ComponentSet](entity/components.md)
  All the components that an entity stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset)*