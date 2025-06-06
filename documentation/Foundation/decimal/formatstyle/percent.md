# Decimal.FormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct

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
- [init(locale: Locale)](decimal/formatstyle/percent/init(locale:).md)
  Creates a decimal percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Percent.Configuration.Grouping) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(Decimal.FormatStyle.Percent.Configuration.Notation) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Percent.Configuration.Precision) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Percent.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Percent.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Percent.Configuration](decimal/formatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Creating attributed strings
- [var attributed: Decimal.FormatStyle.Attributed](decimal/formatstyle/percent/attributed.md)
  An attributed format style based on the decimal percent format style.
- [Decimal.FormatStyle.Attributed](decimal/formatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](decimal/formatstyle/percent/locale.md)
  The locale of the format style.

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

## See Also

- [Decimal.FormatStyle.Currency](decimal/formatstyle/currency.md)
  A format style that converts between decimal currency values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent)*