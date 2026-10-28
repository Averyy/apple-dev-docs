# grouping(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified grouping.

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
func grouping(_ group: IntegerFormatStyle<Value>.Percent.Configuration.Grouping) -> IntegerFormatStyle<Value>.Percent
```

## Return Value

An integer percent format style modified to use the specified grouping.

## Parameters

- `group`: The grouping to apply to the format style.

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func locale(Locale) -> IntegerFormatStyle<Value>.Percent](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(IntegerFormatStyle<Value>.Percent.Configuration.Notation) -> IntegerFormatStyle<Value>.Percent](./notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Percent.Configuration.Precision) -> IntegerFormatStyle<Value>.Percent](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Percent](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Percent](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Percent.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent/grouping(_:))*