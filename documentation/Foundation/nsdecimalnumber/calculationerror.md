# NSDecimalNumber.CalculationError

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](../nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md).

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
enum CalculationError
```

```c
enum NSCalculationError : NSUInteger;
```

## Topics

### Constants
- [NSDecimalNumber.CalculationError.noError](./calculationerror/noerror.md)
  No error occurred.
- [NSDecimalNumber.CalculationError.lossOfPrecision](./calculationerror/lossofprecision.md)
  The number can’t be represented in 38 significant digits.
- [NSDecimalNumber.CalculationError.overflow](./calculationerror/overflow.md)
  The number is too large to represent.
- [NSDecimalNumber.CalculationError.underflow](./calculationerror/underflow.md)
  The number is too small to represent.
- [NSDecimalNumber.CalculationError.divideByZero](./calculationerror/dividebyzero.md)
  The caller tried to divide by `0`.
### Initializers
- [init?(rawValue: UInt)](./calculationerror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing arithmetic using references
- [func NSDecimalCompact(UnsafeMutablePointer<Decimal>)](../nsdecimalcompact%28_%29.md)
  Compacts the decimal structure for efficiency.
- [func NSDecimalAdd(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimaladd%28_,_,_,_%29.md)
  Adds two decimal values.
- [func NSDecimalSubtract(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimalsubtract%28_,_,_,_%29.md)
  Subtracts one decimal value from another.
- [func NSDecimalDivide(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimaldivide%28_,_,_,_%29.md)
  Divides one decimal value by another.
- [func NSDecimalMultiply(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimalmultiply%28_,_,_,_%29.md)
  Multiplies two decimal numbers together.
- [func NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int16, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimalmultiplybypowerof10%28_,_,_,_%29.md)
  Multiplies a decimal by the specified power of 10.
- [func NSDecimalRound(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode)](../nsdecimalround%28_,_,_,_%29.md)
  Rounds off the decimal value.
- [func NSDecimalPower(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimalpower%28_,_,_,_%29.md)
  Raises the decimal value to the specified power.
- [func NSDecimalNormalize(UnsafeMutablePointer<Decimal>, UnsafeMutablePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](../nsdecimalnormalize%28_,_,_%29.md)
  Normalizes the internal format of two decimal numbers to simplify later operations.
- [typealias RoundingMode](../decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](./roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](../decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/calculationerror)*