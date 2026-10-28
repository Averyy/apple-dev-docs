# precision(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified precision.

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
func precision(_ p: FloatingPointFormatStyle<Value>.Percent.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Percent
```

## Return Value

A floating-point format style modified to use the specified precision.

## Discussion

The [`NumberFormatStyleConfiguration.Precision`](../../numberformatstyleconfiguration/precision.md) type lets you specify a fixed number of digits to show for a number’s integer and fractional part.

## Parameters

- `p`: The precision to apply to the format style.

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Percent.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Percent](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> FloatingPointFormatStyle<Value>.Percent](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(FloatingPointFormatStyle<Value>.Percent.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Percent](./notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Percent](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Percent](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Percent.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/precision(_:))*