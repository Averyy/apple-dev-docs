# -(_:_:)

**Framework**: Foundation  
**Kind**: op

Subtracts one decimal number from another.

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
static func - (lhs: Decimal, rhs: Decimal) -> Decimal
```

#### Return Value

The result of subtracting `rhs` from `lhs`.

#### Discussion

If the result of this operation requires more precision than the `Decimal` type can provide, the result is rounded using the [`NSDecimalNumber.RoundingMode.plain`](nsdecimalnumber/roundingmode/plain.md) rounding mode. To specify a different rounding mode, use the [`NSDecimalSubtract(_:_:_:_:)`](nsdecimalsubtract(_:_:_:_:).md) function instead.

## Parameters

- `lhs`: The value to subtract from.
- `rhs`: The value to subtract.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/-(_:_:))*