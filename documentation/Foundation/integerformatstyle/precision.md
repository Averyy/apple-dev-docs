# precision(_:)

**Framework**: Foundation  
**Kind**: method

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
func precision(_ p: IntegerFormatStyle<Value>.Configuration.Precision) -> IntegerFormatStyle<Value>
```

#### Return Value

An integer format style modified to use the specified precision.

#### Discussion

The [`NumberFormatStyleConfiguration.Precision`](numberformatstyleconfiguration/precision.md) type lets you specify a fixed number of digits to show for a number’s integer and fractional parts, although [`IntegerFormatStyle`](integerformatstyle.md) only uses the former. You can also set a fixed number of significant digits.

The following example creates a default [`IntegerFormatStyle`](integerformatstyle.md) for the `en_US` locale, and a second style that uses a maximum of four significant digits. It then applies each style to an array of integers. The formatting that the modified style applies truncates precision to `0` after the fourth most significant digit.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let precisionStyle = defaultStyle.precision(.significantDigits(1...4))
let nums = [123, 1234, 12345, 123456, 1234567]
let defaultNums = nums.map { defaultStyle.format($0) } // ["123", "1,234", "12,345", "123,456", "1,234,567"]
let precisionNums = nums.map { precisionStyle.format($0) } // ["123", "1,234", "12,340", "123,500", "1,235,000"]
```

## Parameters

- `p`: The precision to apply to the format style.

## See Also

- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Configuration.Grouping) -> IntegerFormatStyle<Value>](integerformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Configuration.Notation) -> IntegerFormatStyle<Value>](integerformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/precision(_:))*