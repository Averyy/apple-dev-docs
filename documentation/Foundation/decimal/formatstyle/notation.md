# notation(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified notation.

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
func notation(_ notation: Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle
```

#### Return Value

A decimal format style modified to use the specified notation.

#### Discussion

The following example creates a default [`Decimal.FormatStyle`](decimal/formatstyle.md) for the `en_US` locale, and a second style that uses scientific notation style. It then applies each style to an array of decimal values.

```swift
let defaultStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let scientificStyle = defaultStyle.notation(.scientific)
let nums: [Decimal] = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]
let scientificNums = nums.map { scientificStyle.format($0) } // ["1.001E2", "1.0002E3", "1.00003E4", "1.000004E5", "1E6"]
```

## Parameters

- `notation`: The notation to apply to the format style.

## See Also

- [func decimalSeparator(strategy: Decimal.FormatStyle.Configuration.DecimalSeparatorDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(Decimal.FormatStyle.Configuration.Grouping) -> Decimal.FormatStyle](decimal/formatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle](decimal/formatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: Decimal.FormatStyle.Configuration.RoundingRule, increment: Int?) -> Decimal.FormatStyle](decimal/formatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> Decimal.FormatStyle](decimal/formatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: Decimal.FormatStyle.Configuration.SignDisplayStrategy) -> Decimal.FormatStyle](decimal/formatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Decimal.FormatStyle.Configuration](decimal/formatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/notation(_:))*