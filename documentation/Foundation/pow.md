# pow(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a decimal number raised to a given power.

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
func pow(_ x: Decimal, _ y: Int) -> Decimal
```

#### Return Value

The result of raising `x` to the power of `y`.

#### Discussion

If the result of this operation requires more precision than the `Decimal` type can provide, the result is rounded using the [`NSDecimalNumber.RoundingMode.plain`](nsdecimalnumber/roundingmode/plain.md) rounding mode. To specify a different rounding mode, use the [`NSDecimalPower(_:_:_:_:)`](nsdecimalpower(_:_:_:_:).md) function instead.

## Parameters

- `x`: A decimal value.
- `y`: The power by which to raise  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/pow(_:_:))*