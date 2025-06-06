# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Formats the decimal using the provided format style.

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
func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Decimal
```

#### Return Value

A localized, formatted string representation of the decimal.

#### Discussion

Use this method when you want to format a single decimal value with a specific format style or multiple format styles. The following example shows the results of formatting a given decimal value with format styles for the `en_US` and `fr_FR` locales:

```swift
let decimal: Decimal = 123456.789
let usStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let frStyle = Decimal.FormatStyle(locale: Locale(identifier: "fr_FR"))
let formattedUS = decimal.formatted(usStyle) // 123,456.789
let formattedFR = decimal.formatted(frStyle) // 123 456,789
```

## Parameters

- `format`: The format style to apply when formatting the decimal.

## See Also

- [func formatted() -> String](decimal/formatted.md)
  Formats the decimal using a default localized format style.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatted(_:))*