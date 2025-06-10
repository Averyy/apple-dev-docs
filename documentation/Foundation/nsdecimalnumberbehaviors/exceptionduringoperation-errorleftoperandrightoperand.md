# exceptionDuringOperation(_:error:leftOperand:rightOperand:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Specifies what an `NSDecimalNumber` object will do when it encounters an error.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 1.0+
- macOS 10.0+
- tvOS 1.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func exceptionDuringOperation(_ operation: Selector, error: NSDecimalNumber.CalculationError, leftOperand: NSDecimalNumber, rightOperand: NSDecimalNumber?) -> NSDecimalNumber?
```

#### Discussion

There are four possible values for `error`, described in [`NSDecimalNumber.CalculationError`](nsdecimalnumber/calculationerror.md). The first three have to do with limits on the ability of `NSDecimalNumber` to represent decimal numbers. An `NSDecimalNumber` object can represent any number that can be expressed as mantissa x 10^exponent, where mantissa is a decimal integer up to 38 digits long, and exponent is between –256 and 256. The fourth results from the caller trying to divide by `0`.

In implementing [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md), you can handle each of these errors in several ways:

- Raise an exception. For an explanation of exceptions, see [`Exception Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Exceptions.html#//apple_ref/doc/uid/10000012i).
- Return `nil`. The calling method will return its value as though no error had occurred. If `error` is `NSCalculationLossOfPrecision`, `operation` will return an imprecise value—that is, one constrained to 38 significant digits. If `error` is `NSCalculationUnderflow` or `NSCalculationOverflow`, `operation` will return `NSDecimalNumber`‘s `notANumber`. You shouldn’t return `nil` if `error` is `NSDivideByZero`.
- Correct the error and return a valid `NSDecimalNumber` object. The calling method will use this as its own return value.

## Parameters

- `operation`: The method that was being executed when the error occurred.
- `error`: The type of error that was generated.
- `leftOperand`: The left operand.
- `rightOperand`: The right operand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:))*