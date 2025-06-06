# NSDecimalNumber.CalculationError

**Framework**: Foundation  
**Kind**: enum

Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).

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

## Topics

### Constants
- [NSDecimalNumber.CalculationError.noError](nsdecimalnumber/calculationerror/noerror.md)
  No error occurred.
- [NSDecimalNumber.CalculationError.lossOfPrecision](nsdecimalnumber/calculationerror/lossofprecision.md)
  The number can’t be represented in 38 significant digits.
- [NSDecimalNumber.CalculationError.overflow](nsdecimalnumber/calculationerror/overflow.md)
  The number is too large to represent.
- [NSDecimalNumber.CalculationError.underflow](nsdecimalnumber/calculationerror/underflow.md)
  The number is too small to represent.
- [NSDecimalNumber.CalculationError.divideByZero](nsdecimalnumber/calculationerror/dividebyzero.md)
  The caller tried to divide by `0`.
- [NSDecimalNumber.CalculationError.noError](nsdecimalnumber/calculationerror/noerror.md)
  No error occurred.
- [NSDecimalNumber.CalculationError.lossOfPrecision](nsdecimalnumber/calculationerror/lossofprecision.md)
  The number can’t be represented in 38 significant digits.
- [NSDecimalNumber.CalculationError.overflow](nsdecimalnumber/calculationerror/overflow.md)
  The number is too large to represent.
- [NSDecimalNumber.CalculationError.underflow](nsdecimalnumber/calculationerror/underflow.md)
  The number is too small to represent.
- [NSDecimalNumber.CalculationError.divideByZero](nsdecimalnumber/calculationerror/dividebyzero.md)
  The caller tried to divide by `0`.
### Initializers
- [init?(rawValue: UInt)](nsdecimalnumber/calculationerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func NSDecimalCompact(UnsafeMutablePointer<Decimal>)](nsdecimalcompact(_:).md)
  Compacts the decimal structure for efficiency.
- [func NSDecimalAdd(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimaladd(_:_:_:_:).md)
  Adds two decimal values.
- [func NSDecimalSubtract(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalsubtract(_:_:_:_:).md)
  Subtracts one decimal value from another.
- [func NSDecimalDivide(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimaldivide(_:_:_:_:).md)
  Divides one decimal value by another.
- [func NSDecimalMultiply(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalmultiply(_:_:_:_:).md)
  Multiplies two decimal numbers together.
- [func NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int16, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalmultiplybypowerof10(_:_:_:_:).md)
  Multiplies a decimal by the specified power of 10.
- [func NSDecimalRound(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode)](nsdecimalround(_:_:_:_:).md)
  Rounds off the decimal value.
- [func NSDecimalPower(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalpower(_:_:_:_:).md)
  Raises the decimal value to the specified power.
- [func NSDecimalNormalize(UnsafeMutablePointer<Decimal>, UnsafeMutablePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalnormalize(_:_:_:).md)
  Normalizes the internal format of two decimal numbers to simplify later operations.
- [typealias RoundingMode](decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/calculationerror)*