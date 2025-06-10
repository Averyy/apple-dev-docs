# !=(_:_:)

**Framework**: EnergyKit  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct/!=(_:_:))*