# locale(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the format style to use the specified locale.

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
func locale(_ locale: Locale) -> FloatingPointFormatStyle<Value>
```

Available when `Value` conforms to `BinaryFloatingPoint`.

## Return Value

A floating-point format style modified to use the provided locale.

## Discussion

Use this modifier to change the locale that an existing format style uses. To instead determine the locale this format style uses, use the [`locale`](./locale.md) property.

The following example creates a default [`FloatingPointFormatStyle`](../floatingpointformatstyle.md) for the `en_US` locale, and applies the [`notation(_:)`](../integerformatstyle/notation%28_%29.md) modifier to use compact name notation. Next, the sample creates a second style based on this first style, but using the German (`DE`) locale. It then applies each style to an array of floating-point values.

```swift
let compactStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
    .notation(.compactName)
let germanStyle = compactStyle.locale(Locale(identifier: "DE"))
let nums: [Double] = [100, 1000, 10000, 100000, 1000000]
let enUSCompactNums = nums.map { compactStyle.format($0) } // ["100", "1K", "10K", "100K", "1M"]
let deCompactNums = nums.map { germanStyle.format($0) } // ["100", "1000", "10.000", "100.000", "1 Mio."]

```

## Parameters

- `locale`: The locale to apply to the format style.

## See Also

### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>](./decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Configuration.Grouping) -> FloatingPointFormatStyle<Value>](./grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Configuration.Notation) -> FloatingPointFormatStyle<Value>](./notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Configuration.Precision) -> FloatingPointFormatStyle<Value>](./precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>](./rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>](./scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>](./sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [FloatingPointFormatStyle.Configuration](./configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/locale(_:))*