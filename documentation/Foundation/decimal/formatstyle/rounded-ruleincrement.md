# rounded(rule:increment:)

**Framework**: Foundation  
**Kind**: method

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
func rounded(rule: Decimal.FormatStyle.Configuration.RoundingRule = .toNearestOrEven, increment: Int? = nil) -> Decimal.FormatStyle
```

#### Return Value

A decimal format style modified to use the specified rounding rule and increment.

#### Discussion

The following example creates a default [`Decimal.FormatStyle`](decimal/formatstyle.md) for the `en_US` locale, and a modified style that rounds integers to the nearest multiple of `100`. It then formats the value `1999.95` using these format styles.

```swift
let defaultStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let roundedStyle = defaultStyle.rounded(rule: .toNearestOrEven,
                                        increment: 100)
let num: Decimal = 1999.95
let defaultNum = num.formatted(defaultStyle) // "1,999.95"
let roundedNum = num.formatted(roundedStyle) // "2,000"
```

## Parameters

- `rule`: The rounding rule to apply to the format style.
- `increment`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is   (the default), the formatter doesn’t apply an increment.

## See Also

- [func decimalSeparator(strategy: Decimal.FormatStyle.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Configuration.Grouping) -> Decimal.FormatStyle](decimal/formatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle](decimal/formatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle](decimal/formatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func scale(Double) -> Decimal.FormatStyle](decimal/formatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Decimal.FormatStyle.Configuration](decimal/formatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/rounded(rule:increment:))*