# decimalSeparator(strategy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func decimalSeparator(strategy: Decimal.FormatStyle.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle
```

## Return Value

A decimal format style modified to use the specified decimal separator display strategy.

## Discussion

The following example creates a default [`Decimal.FormatStyle`](../formatstyle.md) for the `en_US` locale, and a second style that uses the [`always`](../../numberformatstyleconfiguration/decimalseparatordisplaystrategy/always.md) strategy. It then applies each style to an array of decimal values that don’t have a fractional part. The formatting that the modified style applies adds a trailing decimal separator in all cases.

```swift
let defaultStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let alwaysStyle = defaultStyle.decimalSeparator(strategy: .always)
let nums: [Decimal] = [100.0, 1000.0, 10000.0, 100000.0, 1000000.0]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100", "1,000", "10,000", "100,000", "1,000,000"]
let alwaysNums = nums.map { alwaysStyle.format($0) } // ["100.", "1,000.", "10,000.", "100,000.", "1,000,000."]
```

## Parameters

- `strategy`: The decimal separator display strategy to apply to the format style.

## See Also

### Customizing style behavior
- [func grouping(Decimal.FormatStyle.Configuration.Grouping) -> Decimal.FormatStyle](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> Decimal.FormatStyle](./locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle](./notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Decimal.FormatStyle.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/decimalseparator(strategy:))*