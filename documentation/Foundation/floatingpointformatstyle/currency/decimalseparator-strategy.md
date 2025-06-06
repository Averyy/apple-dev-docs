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
func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency
```

#### Return Value

A floating-point currency format style modified to use the specified decimal separator display strategy.

## Parameters

- `strategy`: The decimal separator display strategy to apply to the format style.

## See Also

- [func grouping(FloatingPointFormatStyle<Value>.Currency.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(FloatingPointFormatStyle<Value>.Currency.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func presentation(FloatingPointFormatStyle<Value>.Currency.Configuration.Presentation) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/presentation(_:).md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Currency.Configuration](floatingpointformatstyle/currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/decimalseparator(strategy:))*