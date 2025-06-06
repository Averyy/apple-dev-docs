# sign(strategy:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.

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
func sign(strategy: Decimal.FormatStyle.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle
```

#### Return Value

A decimal format style modified to use the specified sign display strategy.

#### Discussion

The following example creates a default [`Decimal.FormatStyle`](decimal/formatstyle.md) for the `en_US` locale, and a second style that displays a sign for all values except zero. It then applies each style to an array of decimal values. The formatting that the modified style applies adds the negative (`-`) or positive (`+`) sign to all the numbers.

```swift
let defaultStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
let alwaysStyle = defaultStyle.sign(strategy: .always(includingZero: false))
let nums = [-2.1, -1.2, 0, 1.4, 2.5]
let defaultNums = nums.map { defaultStyle.format($0) } // ["-2.1", "-1.2", "0", "1.4", "2.5"]
let alwaysNums = nums.map { alwaysStyle.format($0) } // ["-2.1", "-1.2", "0", "+1.4", "+2.5"]
```

## Parameters

- `strategy`: The sign display strategy to apply to the format style, such as   or  .

## See Also

- [func decimalSeparator(strategy: Decimal.FormatStyle.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Configuration.Grouping) -> Decimal.FormatStyle](decimal/formatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle](decimal/formatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle](decimal/formatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle](decimal/formatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle](decimal/formatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [Decimal.FormatStyle.Configuration](decimal/formatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/sign(strategy:))*