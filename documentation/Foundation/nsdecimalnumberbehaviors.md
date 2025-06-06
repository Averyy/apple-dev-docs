# NSDecimalNumberBehaviors

**Framework**: Foundation  
**Kind**: protocol

A protocol that declares three methods that control the discretionary aspects of working with decimal numbers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSDecimalNumberBehaviors
```

#### Overview

The [`scale()`](nsdecimalnumberbehaviors/scale().md) and [`roundingMode()`](nsdecimalnumberbehaviors/roundingmode().md) methods determine the precision of `NSDecimalNumber`’s return values and the way in which those values should be rounded to fit that precision. The [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md) method determines the way in which an `NSDecimalNumber` object should handle different calculation errors.

For an example of a class that adopts the `NSDecimalBehaviors` protocol, see the specification for [`NSDecimalNumberHandler`](nsdecimalnumberhandler.md).

## Topics

### Rounding
- [func roundingMode() -> NSDecimalNumber.RoundingMode](nsdecimalnumberbehaviors/roundingmode.md)
  Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.
- [func scale() -> Int16](nsdecimalnumberbehaviors/scale.md)
  Returns the number of digits allowed after the decimal separator.
### Handling errors
- [func exceptionDuringOperation(Selector, error: NSDecimalNumber.CalculationError, leftOperand: NSDecimalNumber, rightOperand: NSDecimalNumber?) -> NSDecimalNumber?](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md)
  Specifies what an `NSDecimalNumber` object will do when it encounters an error.
### Constants
- [NSDecimalNumber.RoundingMode](nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [NSDecimalNumber.CalculationError](nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).

## Relationships

### Conforming Types
- [NSDecimalNumberHandler](nsdecimalnumberhandler.md)

## See Also

- [class var defaultBehavior: any NSDecimalNumberBehaviors](nsdecimalnumber/defaultbehavior.md)
  The way arithmetic methods round off and handle error conditions.
- [class NSDecimalNumberHandler](nsdecimalnumberhandler.md)
  A class that adopts the decimal number behaviors protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors)*