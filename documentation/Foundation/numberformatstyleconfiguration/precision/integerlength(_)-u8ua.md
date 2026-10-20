# integerLength(_:)

**Framework**: Foundation  
**Kind**: method

Returns a precision that constrains formatted values to a range of allowed digits in the integer part.

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
static func integerLength<R>(_ limits: R) -> NumberFormatStyleConfiguration.Precision where R : RangeExpression
```

#### Return Value

A precision that constrains formatted values to ranges of digits in the integer part.

## Parameters

- `limits`: A range from the minimum to the maximum number of digits to use when formatting the integer part of a number.

## See Also

- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/significantdigits(_:)-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func significantDigits(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/significantdigits(_:)-9dvpr.md)
  Returns a precision that constrains formatted values to a given number of significant digits.
- [static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerandfractionlength(integerlimits:fractionlimits:).md)
  Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerandfractionlength(integer:fraction:).md)
  Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [static func integerLength(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerlength(_:)-1njyz.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [static func fractionLength<R>(R) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/fractionlength(_:)-w6fk.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [static func fractionLength(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/fractionlength(_:)-3wkd9.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerlength(_:)-u8ua)*