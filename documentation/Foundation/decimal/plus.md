# +(_:_:)

**Framework**: Foundation  
**Kind**: op

Adds two decimal numbers.

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
static func + (lhs: Decimal, rhs: Decimal) -> Decimal
```

#### Return Value

The result of adding `lhs` and `rhs`.

#### Discussion

If the result of this operation requires more precision than the `Decimal` type can provide, the result is rounded using the [`NSDecimalNumber.RoundingMode.plain`](nsdecimalnumber/roundingmode/plain.md) rounding mode. To specify a different rounding mode, use the [`NSDecimalAdd(_:_:_:_:)`](nsdecimaladd(_:_:_:_:).md) function instead.

## Parameters

- `lhs`: A value to add.
- `rhs`: Another value to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/+(_:_:))*