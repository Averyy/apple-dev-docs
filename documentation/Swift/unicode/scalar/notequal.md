# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func != (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (Unicode.Scalar, Unicode.Scalar) -> Bool](unicode/scalar/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Unicode.Scalar, Unicode.Scalar) -> Bool](unicode/scalar/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/!=(_:_:))*