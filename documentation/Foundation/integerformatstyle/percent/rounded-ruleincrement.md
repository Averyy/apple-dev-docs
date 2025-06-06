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
func rounded(rule: IntegerFormatStyle<Value>.Percent.Configuration.RoundingRule = .toNearestOrEven, increment: Int? = nil) -> IntegerFormatStyle<Value>.Percent
```

#### Return Value

An integer percent format style modified to use the specified rounding rule and increment.

## Parameters

- `rule`: The rounding rule to apply to the format style.
- `increment`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is   (the default), the formatter doesn’t apply an increment.

## See Also

- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Percent.Configuration.Grouping) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Percent.Configuration.Notation) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Percent.Configuration.Precision) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func scale(Double) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Percent.Configuration](integerformatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent/rounded(rule:increment:))*