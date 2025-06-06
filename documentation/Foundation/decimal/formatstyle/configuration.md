# Decimal.FormatStyle.Configuration

**Framework**: Foundation  
**Kind**: typealias

The type the format style uses for configuration settings.

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
typealias Configuration = NumberFormatStyleConfiguration
```

#### Discussion

[`Decimal.FormatStyle`](decimal/formatstyle.md) uses [`NumberFormatStyleConfiguration`](numberformatstyleconfiguration.md) for its configuration type.

## See Also

- [func decimalSeparator(strategy: Decimal.FormatStyle.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Configuration.Grouping) -> Decimal.FormatStyle](decimal/formatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle](decimal/formatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle](decimal/formatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle](decimal/formatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle](decimal/formatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/configuration)*