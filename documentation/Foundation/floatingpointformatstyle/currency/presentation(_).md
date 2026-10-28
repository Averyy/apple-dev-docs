# presentation(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified presentation.

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
func presentation(_ p: FloatingPointFormatStyle<Value>.Currency.Configuration.Presentation) -> FloatingPointFormatStyle<Value>.Currency
```

## Return Value

A floating-point currency format style modified to use the specified presentation.

## Parameters

- `p`: A currency presentation value, such as [`isoCode`](../../currencyformatstyleconfiguration/presentation/isocode.md) or [`fullName`](../../currencyformatstyleconfiguration/presentation/fullname.md).

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Currency.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Currency](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> FloatingPointFormatStyle<Value>.Currency](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(FloatingPointFormatStyle<Value>.Currency.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Currency](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Currency](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Currency](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Currency.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/presentation(_:))*