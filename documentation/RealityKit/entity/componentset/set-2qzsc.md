# set(_:)

**Framework**: RealityKit  
**Kind**: method

Adds multiple components to the set, overriding any existing components of the same type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func set(_ components: [any Component])
```

#### Discussion

If the input array includes multiple components of the same type, the set adds the component with the highest index. This is because the set can only hold one component of each type.

## Parameters

- `components`: An array of components to add.

## See Also

- [func set<T>(T)](entity/componentset/set(_:)-8sii2.md)
  Adds a new component to the set, or overrides an existing one.
- [func remove(any Component.Type)](entity/componentset/remove(_:).md)
  Removes the component of the specified type from the collection.
- [func removeAll()](entity/componentset/removeall.md)
  Removes all components from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(_:)-2qzsc)*