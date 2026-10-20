# Decimal.FormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that converts between decimal percentage values and their textual representations.

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
struct Percent
```

## Topics

### Creating a decimal percent format style
- [init(locale: Locale)](./percent/init%28locale%29.md)
  Creates a decimal percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Percent](./percent/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Percent.Configuration.Grouping) -> Decimal.FormatStyle.Percent](./percent/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> Decimal.FormatStyle.Percent](./percent/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(Decimal.FormatStyle.Percent.Configuration.Notation) -> Decimal.FormatStyle.Percent](./percent/notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Percent.Configuration.Precision) -> Decimal.FormatStyle.Percent](./percent/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Percent.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Percent](./percent/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Percent](./percent/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Percent.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Percent](./percent/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Percent.Configuration](./percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Formatting decimal percent values
- [func format(Decimal) -> String](./percent/format%28_%29.md)
  Formats an decimal, using this style.
### Creating attributed strings
- [var attributed: Decimal.FormatStyle.Attributed](./percent/attributed.md)
  An attributed format style based on the decimal percent format style.
- [Decimal.FormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](./percent/locale.md)
  The locale of the format style.
### Parsing decimal percent values
- [var parseStrategy: Decimal.ParseStrategy<Decimal.FormatStyle.Percent>](./percent/parsestrategy.md)
  The parse strategy that this format style uses.
### Locating decimal values in regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Decimal)?](./percent/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./percent/customconsumingregexcomponent-implementations.md)
- [ParseableFormatStyle Implementations](./percent/parseableformatstyle-implementations.md)

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

## See Also

### Supporting types
- [Decimal.FormatStyle.Currency](./currency.md)
  A format style that converts between decimal currency values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent)*