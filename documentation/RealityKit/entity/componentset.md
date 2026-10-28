# Entity.ComponentSet

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of components that an entity stores.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency struct ComponentSet
```

## Overview

A `ComponentSet` represents all the components that an entity holds. Use this set to add, remove, and update components on an entity. This set can hold one component of each type.

Access the `ComponentSet` of an [`Entity`](../entity.md) using its [`components`](./components.md) property.

`ComponentSet` conforms to [`Sequence`](../../Swift/sequence.md), allowing you to iterate over it to access and use each component, as the example below shows:

```swift
for component in entity.components {
    print(component)
}
```

## Topics

### Updating the set
- [func set<T>(T)](./componentset/set%28_%29-8sii2.md)
  Adds a new component to the set, or overrides an existing one.
- [func set([any Component])](./componentset/set%28_%29-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func remove(any Component.Type)](./componentset/remove%28_%29.md)
  Removes the component of the specified type from the collection.
- [func removeAll()](./componentset/removeall%28%29.md)
  Removes all components from the collection.
### Accessing members
- [subscript<T>(T.Type) -> T?](./componentset/subscript%28_%29-5wdsf.md)
  Gets or sets the component of the specified type.
- [subscript(any Component.Type) -> (any Component)?](./componentset/subscript%28_%29-47rhg.md)
  Gets or sets the component with a specific dynamically supplied type.
### Checking for membership
- [func has(any Component.Type) -> Bool](./componentset/has%28_%29.md)
  Returns a Boolean value that indicates whether the set contains a component of the given type.
### Accessing components
- [subscript<T>(componentType _: T.Type) -> T?](./componentset/subscript%28componenttype%29-8y2jv.md)
  Gets or sets the component of the specified type.
- [subscript<T>(T.Type, Void) -> T?](./componentset/subscript%28_,_%29-404se.md)
  Gets or sets the component of the specified type.
### Accessing animatable components
- [subscript<T>(componentType _: T.Type) -> T?](./componentset/subscript%28componenttype%29-3miek.md)
- [subscript<T>(T.Type, Void) -> T?](./componentset/subscript%28_,_%29-b2gl.md)
- [subscript<T>(withoutAnimation _: T.Type) -> T?](./componentset/subscript%28withoutanimation%29.md)
  Gets or sets the component of the specified type, without considering implicit animations.
### Setting components by name
- [func set(qualifiedComponentName: String, representation: some Encodable) throws](./componentset/set%28qualifiedcomponentname,representation%29.md)
  Adds component data to an entity that is written to a Reality file but has no other effect at author time.
### Instance Properties
- [var count: Int](./componentset/count.md)
  The number of components in the collection.
- [var entity: Entity](./componentset/entity.md)
### Instance Methods
- [func set(_:)](./componentset/set%28_%29.md)
  Adds multiple components to the set, overriding any existing components of the same type.
### Subscripts
- [subscript(_:)](./componentset/subscript%28_%29.md)
  Gets or sets the component with a specific dynamically supplied type.
- [subscript(_:_:)](./componentset/subscript%28_,_%29.md)
  Gets or sets the component of the specified type.
- [subscript(componentType:)](./componentset/subscript%28componenttype%29.md)
  Gets or sets the component of the specified type.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Managing components
- [var components: Entity.ComponentSet](./components.md)
  All the components that an entity stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset)*