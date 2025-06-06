# isEnabled

**Framework**: RealityKit  
**Kind**: property

A Boolean that you set to enable or disable the entity and its descendants.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isEnabled: Bool { get set }
```

## Mentions

- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)

#### Discussion

Set this value to `true` to enable the entity. Unless an ancestor is disabled, the entity and all of its enabled descendants, up to the first that’s disabled, report [`isEnabledInHierarchy`](entity/isenabledinhierarchy.md) of `true`. If an ancestor is disabled, they all report `false`. The state of [`isActive`](entity/isactive.md) for enabled entities is `true` if they are anchored, or `false` otherwise.

If you disable an entity, it and all of its descendants become both disabled ([`isEnabledInHierarchy`](entity/isenabledinhierarchy.md) returns `false`) and inactive ([`isActive`](entity/isactive.md) returns `false`), regardless of any other state.

When an entity is disabled, it’s no longer visible in your scene. However, the entity is still included in an [`EntityQuery`](entityquery.md).

## See Also

- [var isEnabledInHierarchy: Bool](entity/isenabledinhierarchy.md)
  A Boolean that indicates whether the entity and all of its ancestors are enabled.
- [var isActive: Bool](entity/isactive.md)
  A Boolean that indicates whether the entity is active.
- [var isAnchored: Bool](entity/isanchored.md)
  A Boolean that indicates whether the entity is anchored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/isenabled)*