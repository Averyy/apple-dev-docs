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

- [static func == (JointTransforms, JointTransforms) -> Bool](jointtransforms/==(_:_:).md)
  Returns a Boolean value that indicates whether two collections of joints are equal.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](jointtransforms/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/!=(_:_:))*