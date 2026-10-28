# IntegerFormatStyle.Currency.Configuration

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

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
typealias Configuration = CurrencyFormatStyleConfiguration
```

## Discussion

[`IntegerFormatStyle.Currency`](../currency.md) uses [`CurrencyFormatStyleConfiguration`](../../currencyformatstyleconfiguration.md) for its configuration type.

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
- [func rounded(rule: IntegerFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Currency](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Currency](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [enum CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/currency/configuration)*