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
func decimalSeparator(strategy: IntegerFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Currency
```

#### Return Value

An integer currency format style modified to use the specified decimal separator display strategy.

## Parameters

- `strategy`: The decimal separator display strategy to apply to the format style.

## See Also

- [func grouping(IntegerFormatStyle<Value>.Currency.Configuration.Grouping) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(IntegerFormatStyle<Value>.Currency.Configuration.Precision) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func presentation(IntegerFormatStyle<Value>.Currency.Configuration.Presentation) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/presentation(_:).md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: IntegerFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Currency.Configuration](integerformatstyle/currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/currency/decimalseparator(strategy:))*