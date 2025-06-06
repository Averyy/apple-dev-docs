# !=(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (AnimationPlaybackController, AnimationPlaybackController) -> Bool](animationplaybackcontroller/==(_:_:).md)
  Indicates whether two animation playback controllers are equal.
- [func hash(into: inout Hasher)](animationplaybackcontroller/hash(into:).md)
  Hashes the essential components of the controller by feeding them into the given hash function.
- [var hashValue: Int](animationplaybackcontroller/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/!=(_:_:))*