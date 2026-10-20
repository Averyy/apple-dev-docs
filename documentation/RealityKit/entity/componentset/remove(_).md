# remove(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes the component of the specified type from the collection.

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
@preconcurrency func remove(_ componentType: any Component.Type)
```

## See Also

### Updating the set
- [func set<T>(T)](./set%28_%29-8sii2.md)
  Adds a new component to the set, or overrides an existing one.
- [func set([any Component])](./set%28_%29-2qzsc.md)
  Adds multiple components to the set, overriding any existing components of the same type.
- [func removeAll()](./removeall%28%29.md)
  Removes all components from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/remove(_:))*