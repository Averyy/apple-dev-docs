# components

**Framework**: RealityKit  
**Kind**: property

All the components that an entity stores.

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
@preconcurrency var components: Entity.ComponentSet { get set }
```

#### Discussion

You can only store one component of a given type on an entity.

## See Also

- [Entity.ComponentSet](entity/componentset.md)
  A collection of components that an entity stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/components)*