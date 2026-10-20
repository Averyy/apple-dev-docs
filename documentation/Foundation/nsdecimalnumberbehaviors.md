# NSDecimalNumberBehaviors

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSDecimalNumberBehaviors
```

#### Overview

The [`scale()`](./nsdecimalnumberbehaviors/scale%28%29.md) and [`roundingMode()`](./nsdecimalnumberbehaviors/roundingmode%28%29.md) methods determine the precision of `NSDecimalNumber`’s return values and the way in which those values should be rounded to fit that precision. The [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](./nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md) method determines the way in which an `NSDecimalNumber` object should handle different calculation errors.

For an example of a class that adopts the `NSDecimalBehaviors` protocol, see the specification for [`NSDecimalNumberHandler`](./nsdecimalnumberhandler.md).

## Topics

### Rounding
- [func roundingMode() -> NSDecimalNumber.RoundingMode](./nsdecimalnumberbehaviors/roundingmode%28%29.md)
  Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.
- [func scale() -> Int16](./nsdecimalnumberbehaviors/scale%28%29.md)
  Returns the number of digits allowed after the decimal separator.
### Handling errors
- [func exceptionDuringOperation(Selector, error: NSDecimalNumber.CalculationError, leftOperand: NSDecimalNumber, rightOperand: NSDecimalNumber?) -> NSDecimalNumber?](./nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md)
  Specifies what an `NSDecimalNumber` object will do when it encounters an error.
### Constants
- [NSDecimalNumber.RoundingMode](./nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [NSDecimalNumber.CalculationError](./nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](./nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md).

## Relationships

### Conforming Types
- [NSDecimalNumberHandler](./nsdecimalnumberhandler.md)

## See Also

### Managing Behavior
- [class var defaultBehavior: any NSDecimalNumberBehaviors](./nsdecimalnumber/defaultbehavior.md)
  The way arithmetic methods round off and handle error conditions.
- [class NSDecimalNumberHandler](./nsdecimalnumberhandler.md)
  A class that adopts the decimal number behaviors protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors)*