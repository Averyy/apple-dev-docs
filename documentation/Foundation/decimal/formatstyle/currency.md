# Decimal.FormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct

A format style that converts between decimal currency values and their textual representations.

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
struct Currency
```

## Topics

### Creating a decimal currency style
- [init(code: String, locale: Locale)](decimal/formatstyle/currency/init(code:locale:).md)
  Creates a decimal currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Currency.Configuration.Grouping) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(Decimal.FormatStyle.Currency.Configuration.Precision) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func presentation(Decimal.FormatStyle.Currency.Configuration.Presentation) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/presentation(_:).md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: Decimal.FormatStyle.Currency.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Currency.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Currency.Configuration](decimal/formatstyle/currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Creating attributed strings
- [var attributed: Decimal.FormatStyle.Attributed](decimal/formatstyle/currency/attributed.md)
  An attributed format style based on the decimal currency format style.
- [Decimal.FormatStyle.Attributed](decimal/formatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var currencyCode: String](decimal/formatstyle/currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](decimal/formatstyle/currency/locale.md)
  The locale of the format style.
### Instance Methods
- [func notation(Decimal.FormatStyle.Currency.Configuration.Notation) -> Decimal.FormatStyle.Currency](decimal/formatstyle/currency/notation(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency)*