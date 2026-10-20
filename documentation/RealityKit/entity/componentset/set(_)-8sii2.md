# set(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds a new component to the set, or overrides an existing one.

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
@preconcurrency func set<T>(_ component: T) where T : Component
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func set(_ components: [any Component])
```

```swift
@MainActor
@preconcurrency func set<T>(_ component: T) where T : _ImplicitlyAnimatableBuiltinComponent
```

## Parameters

- `component`: The component to add.

## See Also

### Updating the set
- [func set([any Component])](./set%28_%29-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func remove(any Component.Type)](./remove%28_%29.md)
  Removes the component of the specified type from the collection.
- [func removeAll()](./removeall%28%29.md)
  Removes all components from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(_:)-8sii2)*