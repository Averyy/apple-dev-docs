# scale(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the format style to use the specified scale.

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
func scale(_ multiplicand: Double) -> FloatingPointFormatStyle<Value>
```

#### Return Value

A floating-point format style modified to use the specified scale.

#### Discussion

The following example creates a default [`FloatingPointFormatStyle`](floatingpointformatstyle.md) for the `en_US` locale, and a second style that scales by a `multiplicand` of `0.001`. It then applies each style to an array of floating-point values. The formatting that the modified style applies expresses each value in terms of one-thousandths.

```swift
let defaultStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
let scaledStyle = defaultStyle.scale(0.001)
let nums = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]
let scaledNums = nums.map { scaledStyle.format($0) } // ["0.1001", "1.0002", "10.0003", "100.0004", "1,000.0005"]
```

## Parameters

- `multiplicand`: The multiplicand to apply to the format style.

## See Also

- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Configuration.Grouping) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Configuration.Notation) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Configuration.Precision) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [FloatingPointFormatStyle.Configuration](floatingpointformatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/scale(_:))*