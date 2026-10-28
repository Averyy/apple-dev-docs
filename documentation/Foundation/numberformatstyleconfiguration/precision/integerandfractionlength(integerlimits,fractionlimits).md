# integerAndFractionLength(integerLimits:fractionLimits:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.

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
static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision where R1 : RangeExpression, R2 : RangeExpression, R1.Bound == Int, R2.Bound == Int
```

## Return Value

A precision that constrains formatted values to ranges of digits in the integer and fraction parts.

## Discussion

When using this precision, the formatter rounds values that have more digits than the maximum of the range, as seen in the following example:

```swift
let myNum = 12345.6789.formatted(.number
    .precision(.integerAndFractionLength(integerLimits: 2...,
                                         fractionLimits: 2...3))
    .rounded(rule: .down)) // "12,345.678"
```

## Parameters

- `integerLimits`: A range from the minimum to the maximum number of digits to use when formatting the integer part of a number.
- `fractionLimits`: A range from the minimum to the maximum number of digits to use when formatting the fraction part of a number.

## See Also

### Precision configurations
- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](./significantdigits%28_%29-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func significantDigits(Int) -> NumberFormatStyleConfiguration.Precision](./significantdigits%28_%29-9dvpr.md)
  Returns a precision that constrains formatted values to a given number of significant digits.
- [static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision](./integerandfractionlength%28integer,fraction%29.md)
  Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [static func integerLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./integerlength%28_%29-u8ua.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [static func integerLength(Int) -> NumberFormatStyleConfiguration.Precision](./integerlength%28_%29-1njyz.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [static func fractionLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./fractionlength%28_%29-w6fk.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [static func fractionLength(Int) -> NumberFormatStyleConfiguration.Precision](./fractionlength%28_%29-3wkd9.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerandfractionlength(integerlimits:fractionlimits:))*