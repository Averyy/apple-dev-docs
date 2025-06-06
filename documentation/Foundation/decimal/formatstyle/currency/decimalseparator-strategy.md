# decimalSeparator(strategy:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified decimal separator display strategy.

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
func decimalSeparator(strategy: Decimal.FormatStyle.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Currency
```

#### Return Value

A decimal currency format style modified to use the specified decimal separator display strategy.

## Parameters

- `strategy`: The decimal separator display strategy to apply to the format style.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/decimalseparator(strategy:))*