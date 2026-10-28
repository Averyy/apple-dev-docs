# presentation(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified presentation.

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
func presentation(_ p: Decimal.FormatStyle.Currency.Configuration.Presentation) -> Decimal.FormatStyle.Currency
```

## Return Value

A decimal currency format style modified to use the specified presentation.

## Parameters

- `p`: A currency presentation value, such as [`isoCode`](../../../currencyformatstyleconfiguration/presentation/isocode.md) or [`fullName`](../../../currencyformatstyleconfiguration/presentation/fullname.md).

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Currency](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Currency.Configuration.Grouping) -> Decimal.FormatStyle.Currency](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> Decimal.FormatStyle.Currency](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(Decimal.FormatStyle.Currency.Configuration.Precision) -> Decimal.FormatStyle.Currency](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Currency.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Currency](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Currency](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Currency.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Currency](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Currency.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../../../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/presentation(_:))*