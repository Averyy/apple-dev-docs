# scale(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified scale.

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
func scale(_ multiplicand: Double) -> FloatingPointFormatStyle<Value>.Percent
```

#### Return Value

A floating-point format style modified to use the specified scale.

## Parameters

- `multiplicand`: The multiplicand to apply to the format style.

## See Also

- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Percent.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Percent.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Percent.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Percent.Configuration](floatingpointformatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/scale(_:))*