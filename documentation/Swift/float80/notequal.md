# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- macOS 10.10+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/!=(_:_:))*