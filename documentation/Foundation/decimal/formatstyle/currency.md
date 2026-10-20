# Decimal.FormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(code: String, locale: Locale)](./currency/init%28code,locale%29.md)
  Creates a decimal currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Currency](./currency/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Currency.Configuration.Grouping) -> Decimal.FormatStyle.Currency](./currency/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> Decimal.FormatStyle.Currency](./currency/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(Decimal.FormatStyle.Currency.Configuration.Precision) -> Decimal.FormatStyle.Currency](./currency/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func presentation(Decimal.FormatStyle.Currency.Configuration.Presentation) -> Decimal.FormatStyle.Currency](./currency/presentation%28_%29.md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: Decimal.FormatStyle.Currency.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Currency](./currency/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Currency](./currency/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Currency.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Currency](./currency/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Currency.Configuration](./currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Formatting decimal currency values
- [func format(Decimal) -> String](./currency/format%28_%29.md)
  Formats a decimal value, using this style.
### Creating attributed strings
- [var attributed: Decimal.FormatStyle.Attributed](./currency/attributed.md)
  An attributed format style based on the decimal currency format style.
- [Decimal.FormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var currencyCode: String](./currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](./currency/locale.md)
  The locale of the format style.
### Parsing decimal currency values
- [var parseStrategy: Decimal.ParseStrategy<Decimal.FormatStyle.Currency>](./currency/parsestrategy.md)
  The parse strategy that this format style uses.
### Locating currency values in regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Decimal)?](./currency/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Instance Methods
- [func notation(Decimal.FormatStyle.Currency.Configuration.Notation) -> Decimal.FormatStyle.Currency](./currency/notation%28_%29.md)
  Modifies the format style to use the specified notation.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./currency/customconsumingregexcomponent-implementations.md)
- [ParseableFormatStyle Implementations](./currency/parseableformatstyle-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [FormatStyle](../../formatstyle.md)
- [Hashable](../../../Swift/hashable.md)
- [ParseableFormatStyle](../../parseableformatstyle.md)
- [RegexComponent](../../../Swift/regexcomponent.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency)*