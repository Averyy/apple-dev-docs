# significantDigits(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a precision that constrains formatted values to a given number of significant digits.

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
static func significantDigits(_ digits: Int) -> NumberFormatStyleConfiguration.Precision
```

#### Return Value

A precision that constrains formatted values to a given number of significant digits.

#### Discussion

When using this precision, the formatter rounds values that have more sigificant digits than the maximum of the range, as seen in the following example:

```swift
let myNum = 123456.formatted(.number
    .precision(.significantDigits(4))
    .rounded(rule: .down)) // "123,400"
```

## Parameters

- `digits`: The maximum number of significant digits to use when formatting values.

## See Also

### Precision configurations
- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](./significantdigits%28_%29-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision](./integerandfractionlength%28integerlimits,fractionlimits%29.md)
  Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision/significantdigits(_:)-9dvpr)*