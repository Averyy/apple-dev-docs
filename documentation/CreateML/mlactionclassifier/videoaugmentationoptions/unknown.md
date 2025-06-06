# !=(_:_:)

**Framework**: Create ML  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- macOS 10.14+

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

- [func isDisjoint(with: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isSubset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/!=(_:_:))*