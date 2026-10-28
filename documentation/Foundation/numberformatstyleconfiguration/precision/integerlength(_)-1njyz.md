# integerLength(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.

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
static func integerLength(_ length: Int) -> NumberFormatStyleConfiguration.Precision
```

## Return Value

A precision that constrains formatted values to a given number of allowed digits in the integer part.

## Parameters

- `length`: The number of digits to use when formatting the integer part of a number.

## See Also

### Precision configurations
- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](./significantdigits%28_%29-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func significantDigits(Int) -> NumberFormatStyleConfiguration.Precision](./significantdigits%28_%29-9dvpr.md)
  Returns a precision that constrains formatted values to a given number of significant digits.
- [static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision](./integerandfractionlength%28integerlimits,fractionlimits%29.md)
  Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision](./integerandfractionlength%28integer,fraction%29.md)
  Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [static func integerLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./integerlength%28_%29-u8ua.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [static func fractionLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./fractionlength%28_%29-w6fk.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [static func fractionLength(Int) -> NumberFormatStyleConfiguration.Precision](./fractionlength%28_%29-3wkd9.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/integerlength(_:)-1njyz)*