# IntegerFormatStyle.Configuration

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

[`IntegerFormatStyle`](integerformatstyle.md) uses [`NumberFormatStyleConfiguration`](numberformatstyleconfiguration.md) for its configuration type.

## See Also

- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Configuration.Grouping) -> IntegerFormatStyle<Value>](integerformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Configuration.Notation) -> IntegerFormatStyle<Value>](integerformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Configuration.Precision) -> IntegerFormatStyle<Value>](integerformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>](integerformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>](integerformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/configuration)*