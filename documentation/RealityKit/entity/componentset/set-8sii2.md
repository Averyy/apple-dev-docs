# set(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a new component to the set, or overrides an existing one.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func set<T>(_ component: T) where T : Component
```

## Parameters

- `component`: The component to add.

## See Also

- [func set([any Component])](entity/componentset/set(_:)-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func remove(any Component.Type)](entity/componentset/remove(_:).md)
  Removes the component of the specified type from the collection.
- [func removeAll()](entity/componentset/removeall.md)
  Removes all components from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(_:)-8sii2)*