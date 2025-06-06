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
func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule = .toNearestOrEven, increment: Double? = nil) -> FloatingPointFormatStyle<Value>
```

#### Return Value

A floating-point format style modified to use the specified rounding rule and increment.

#### Discussion

The following example creates a default [`FloatingPointFormatStyle`](floatingpointformatstyle.md) for the `en_US` locale, and modifies its rounding behavior. It uses the [`FloatingPointRoundingRule.up`](https://developer.apple.com/documentation/Swift/FloatingPointRoundingRule/up) rounding rule, and an increment of `0.25`. It then applies this style to an array of floating-point values, rounding them to the next greater increment of 0.25.

```swift
let roundedStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
    .rounded(rule: .up, increment: 0.25)
let nums = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
let roundedNums = nums.map { roundedStyle.format($0) } // ["1.00", "1.25", "1.25", "1.50", "1.50", "1.50", "1.75"]
```

## Parameters

- `rule`: The rounding rule to apply to the format style.
- `increment`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is   (the default), the formatter doesn’t apply an increment.

## See Also

- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Configuration.Grouping) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Configuration.Notation) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Configuration.Precision) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func scale(Double) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [FloatingPointFormatStyle.Configuration](floatingpointformatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/rounded(rule:increment:))*