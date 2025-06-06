# !=(_:_:)

**Framework**: TabularData  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

Returns a Boolean that indicates whether the columns are unequal.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.
- `lhs`: A type-erased column.
- `rhs`: Another type-erased column.

## See Also

- [static func == (AnyColumn, AnyColumn) -> Bool](anycolumn/==(_:_:).md)
  Returns a Boolean that indicates whether the columns are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/!=(_:_:))*