# isActive

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the entity is active.

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
@preconcurrency var isActive: Bool { get }
```

#### Discussion

The value of this property is `true` if the entity is anchored in a scene, and it and all of its ancestors are enabled ([`isEnabled`](./isenabled.md) is set to `true`). RealityKit doesn’t simulate or render inactive entities.

## See Also

### Managing the entity’s state
- [var isEnabled: Bool](./isenabled.md)
  A Boolean that you set to enable or disable the entity and its descendants.
- [var isEnabledInHierarchy: Bool](./isenabledinhierarchy.md)
  A Boolean that indicates whether the entity and all of its ancestors are enabled.
- [var isAnchored: Bool](./isanchored.md)
  A Boolean that indicates whether the entity is anchored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/isactive)*