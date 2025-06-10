# ==(_:_:)

**Framework**: RealityKit  
**Kind**: op

Indicates whether two bounding boxes are equal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static func == (lhs: BoundingBox, rhs: BoundingBox) -> Bool
```

#### Return Value

A Boolean value set to `true` if the two boxes are equal.

## Parameters

- `lhs`: The first box to compare.
- `rhs`: The second box to compare.

## See Also

- [func hash(into: inout Hasher)](boundingbox/hash(into:).md)
  Hashes the essential components of the bounding box by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/==(_:_:))*