# decimalSeparator(strategy:)

**Framework**: Foundation  
**Kind**: method

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
func decimalSeparator(strategy: IntegerFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>
```

#### Return Value

An integer format style modified to use the specified decimal separator display strategy.

#### Discussion

The following example creates a default [`IntegerFormatStyle`](integerformatstyle.md) for the `en_US` locale, and a second style that uses the [`always`](numberformatstyleconfiguration/decimalseparatordisplaystrategy/always.md) strategy. It then applies each style to an array of integers. The formatting that the modified style applies adds a trailing decimal separator in all cases.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let alwaysStyle = defaultStyle.decimalSeparator(strategy: .always)
let nums = [100, 1000, 10000, 100000, 1000000]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100", "1,000", "10,000", "100,000", "1,000,000"]
let alwaysNums = nums.map { alwaysStyle.format($0) } // ["100.", "1,000.", "10,000.", "100,000.", "1,000,000."]
```

## Parameters

- `strategy`: The decimal separator display strategy to apply to the format style.

## See Also

- [func grouping(IntegerFormatStyle<Value>.Configuration.Grouping) -> IntegerFormatStyle<Value>](integerformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Configuration.Notation) -> IntegerFormatStyle<Value>](integerformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Configuration.Precision) -> IntegerFormatStyle<Value>](integerformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>](integerformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>](integerformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [IntegerFormatStyle.Configuration](integerformatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/decimalseparator(strategy:))*