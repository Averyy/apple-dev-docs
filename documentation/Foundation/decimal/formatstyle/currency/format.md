# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a decimal value, using this style.

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
func format(_ value: Decimal) -> String
```

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple decimal values. To format a single decimal value, use the [`Decimal`](decimal.md) instance method [`formatted(_:)`](decimal/formatted(_:).md), passing in an instance of [`Decimal.FormatStyle.Currency`](decimal/formatstyle/currency.md).

## Parameters

- `value`: The floating-point value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/format(_:))*