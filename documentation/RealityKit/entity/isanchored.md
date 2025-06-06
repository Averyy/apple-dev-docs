# isAnchored

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the entity is anchored.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isAnchored: Bool { get }
```

#### Discussion

The value of this property is `true` if the entity is anchored in a scene. An entity that isn’t anchored becomes inactive ([`isActive`](entity/isactive.md) returns `false`), meaning RealityKit doesn’t render or simulate it.

## See Also

- [var isEnabled: Bool](entity/isenabled.md)
  A Boolean that you set to enable or disable the entity and its descendants.
- [var isEnabledInHierarchy: Bool](entity/isenabledinhierarchy.md)
  A Boolean that indicates whether the entity and all of its ancestors are enabled.
- [var isActive: Bool](entity/isactive.md)
  A Boolean that indicates whether the entity is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/isanchored)*