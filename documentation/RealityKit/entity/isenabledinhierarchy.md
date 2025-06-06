# isEnabledInHierarchy

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the entity and all of its ancestors are enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isEnabledInHierarchy: Bool { get }
```

#### Discussion

The value of this property is `true` if the entity and all of its ancestors are enabled, regardless of anchor state.

## See Also

- [var isEnabled: Bool](entity/isenabled.md)
  A Boolean that you set to enable or disable the entity and its descendants.
- [var isActive: Bool](entity/isactive.md)
  A Boolean that indicates whether the entity is active.
- [var isAnchored: Bool](entity/isanchored.md)
  A Boolean that indicates whether the entity is anchored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/isenabledinhierarchy)*