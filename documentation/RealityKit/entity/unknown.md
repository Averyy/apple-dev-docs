# ==(_:_:)

**Framework**: RealityKit  
**Kind**: op

Indicates whether two entities are equal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
nonisolated
static func == (lhs: Entity, rhs: Entity) -> Bool
```

#### Return Value

A Boolean value set to `true` if the two entities are equal.

## Parameters

- `lhs`: The first entity to compare.
- `rhs`: The second entity to compare.

## See Also

- [func hash(into: inout Hasher)](entity/hash(into:).md)
  Hashes the essential components of the entity by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/==(_:_:))*