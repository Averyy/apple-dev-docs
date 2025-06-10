# remove(_:)

**Framework**: RealityKit  
**Kind**: method

Removes the component of the specified type from the collection.

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
@preconcurrency func remove(_ componentType: any Component.Type)
```

## See Also

- [func set<T>(T)](entity/componentset/set(_:)-8sii2.md)
  Adds a new component to the set, or overrides an existing one.
- [func set([any Component])](entity/componentset/set(_:)-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func removeAll()](entity/componentset/removeall.md)
  Removes all components from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/remove(_:))*