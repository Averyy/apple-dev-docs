# rounded(rule:increment:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified rounding rule and increment.

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
func rounded(rule: Decimal.FormatStyle.Percent.Configuration.RoundingRule = .toNearestOrEven, increment: Int? = nil) -> Decimal.FormatStyle.Percent
```

#### Return Value

A decimal format style modified to use the specified rounding rule and increment.

## Parameters

- `rule`: The rounding rule to apply to the format style.
- `increment`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is   (the default), the formatter doesn’t apply an increment.

## See Also

- [func decimalSeparator(strategy: Decimal.FormatStyle.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Percent.Configuration.Grouping) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(Decimal.FormatStyle.Percent.Configuration.Notation) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Percent.Configuration.Precision) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func scale(Double) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Percent.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle.Percent](decimal/formatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [Decimal.FormatStyle.Percent.Configuration](decimal/formatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent/rounded(rule:increment:))*