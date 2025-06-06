# NumberFormatStyleConfiguration

**Framework**: Foundation  
**Kind**: enum

Configuration settings for formatting numbers of different types.

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
enum NumberFormatStyleConfiguration
```

#### Overview

This type is effectively a namespace to collect types that configure parts of a formatted number, such as grouping, precision, and separator and sign characters.

## Topics

### Specifying Configuration
- [NumberFormatStyleConfiguration.DecimalSeparatorDisplayStrategy](numberformatstyleconfiguration/decimalseparatordisplaystrategy.md)
  A structure that an integer format style uses to configure a decimal separator display strategy.
- [NumberFormatStyleConfiguration.Grouping](numberformatstyleconfiguration/grouping.md)
  A structure that an integer format style uses to configure grouping.
- [NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision.md)
  A structure that an integer format style uses to configure precision.
- [NumberFormatStyleConfiguration.RoundingRule](numberformatstyleconfiguration/roundingrule.md)
  The type used for rounding rule values.
- [NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy.md)
  A structure that an integer format style uses to configure a sign display strategy.
- [NumberFormatStyleConfiguration.Notation](numberformatstyleconfiguration/notation.md)
  A structure that an integer format style uses to configure notation.

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
- [Decimal.FormatStyle.Configuration](decimal/formatstyle/configuration.md)
  The type the format style uses for configuration settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration)*