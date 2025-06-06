# ==(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS ?+

## Declaration

```swift
static func == (a: NetworkCompatibilityToken.Compatibility, b: NetworkCompatibilityToken.Compatibility) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [var hashValue: Int](networkcompatibilitytoken/compatibility/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](networkcompatibilitytoken/compatibility/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func != (Self, Self) -> Bool](networkcompatibilitytoken/compatibility/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibility/==(_:_:))*