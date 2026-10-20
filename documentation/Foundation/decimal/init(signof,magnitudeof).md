# init(signOf:magnitudeOf:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and initializes a decimal with the sign and magnitude of the given decimals.

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
init(signOf: Decimal, magnitudeOf magnitude: Decimal)
```

## Parameters

- `signOf`: A [`Decimal`](../decimal.md) to use for the sign of the newly-created [`Decimal`](../decimal.md).
- `magnitude`: A [`Decimal`](../decimal.md) to use for the magnitude of the newly-created [`Decimal`](../decimal.md).

## See Also

### Creating a decimal from another decimal
- [func NSDecimalCopy(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>)](../nsdecimalcopy%28_,_%29.md)
  Copies the value of a decimal number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/init(signof:magnitudeof:))*