# notation(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified notation.

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
func notation(_ notation: IntegerFormatStyle<Value>.Percent.Configuration.Notation) -> IntegerFormatStyle<Value>.Percent
```

#### Return Value

An integer percent format style modified to use the specified notation.

## Parameters

- `notation`: The notation to apply to the format style.

## See Also

- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Percent.Configuration.Grouping) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(IntegerFormatStyle<Value>.Percent.Configuration.Precision) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Percent.Configuration](integerformatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent/notation(_:))*