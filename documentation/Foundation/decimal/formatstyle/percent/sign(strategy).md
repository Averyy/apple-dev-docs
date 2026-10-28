# sign(strategy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified sign display strategy.

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
func sign(strategy: Decimal.FormatStyle.Percent.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Percent
```

## Return Value

A decimal format style modified to use the specified sign display strategy.

## Parameters

- `strategy`: The sign display strategy to apply to the format style.

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: Decimal.FormatStyle.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Percent](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Percent.Configuration.Grouping) -> Decimal.FormatStyle.Percent](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> Decimal.FormatStyle.Percent](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(Decimal.FormatStyle.Percent.Configuration.Notation) -> Decimal.FormatStyle.Percent](./notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Percent.Configuration.Precision) -> Decimal.FormatStyle.Percent](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Percent.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle.Percent](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle.Percent](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [Decimal.FormatStyle.Percent.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../../../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent/sign(strategy:))*