# *=(_:_:)

**Framework**: Foundation  
**Kind**: op  
**Role**: Operator

Multiplies two decimal numbers, storing the result in the first number.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func *= (lhs: inout Decimal, rhs: Decimal)
```

## Discussion

If the result of this operation requires more precision than the `Decimal` type can provide, the result is rounded using the [`NSDecimalNumber.RoundingMode.plain`](../nsdecimalnumber/roundingmode/plain.md) rounding mode. To specify a different rounding mode, use the [`NSDecimalMultiply(_:_:_:_:)`](../nsdecimalmultiply%28_,_,_,_%29.md) function instead.

## Parameters

- `lhs`: A value to multiply.
- `rhs`: Another value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/*=(_:_:))*