# ==(_:_:)

**Framework**: RealityKit  
**Kind**: op

Indicates whether two scenes are equal.

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
static func == (lhs: Scene, rhs: Scene) -> Bool
```

#### Return Value

A Boolean value set to `true` if the two scenes are equal.

## Parameters

- `lhs`: The first scene to compare.
- `rhs`: The second scene to compare.

## See Also

- [func hash(into: inout Hasher)](scene/hash(into:).md)
  Hashes the essential components of the scene by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/==(_:_:))*