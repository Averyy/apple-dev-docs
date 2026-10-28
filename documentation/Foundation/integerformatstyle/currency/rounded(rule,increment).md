# rounded(rule:increment:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func rounded(rule: IntegerFormatStyle<Value>.Currency.Configuration.RoundingRule = .toNearestOrEven, increment: Int? = nil) -> IntegerFormatStyle<Value>.Currency
```

## Return Value

An integer currency format style modified to use the specified rounding rule and increment.

## Parameters

- `rule`: The rounding rule to apply to the format style.
- `increment`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment.

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Currency.Configuration.Grouping) -> IntegerFormatStyle<Value>.Currency](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> IntegerFormatStyle<Value>.Currency](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(IntegerFormatStyle<Value>.Currency.Configuration.Precision) -> IntegerFormatStyle<Value>.Currency](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func presentation(IntegerFormatStyle<Value>.Currency.Configuration.Presentation) -> IntegerFormatStyle<Value>.Currency](./presentation%28_%29.md)
  Modifies the format style to use the specified presentation.
- [func scale(Double) -> IntegerFormatStyle<Value>.Currency](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Currency.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/currency/rounded(rule:increment:))*