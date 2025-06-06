# NSDecimalNormalize(_:_:_:)

**Framework**: Foundation  
**Kind**: func

Normalizes the internal format of two decimal numbers to simplify later operations.

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
func NSDecimalNormalize(_ number1: UnsafeMutablePointer<Decimal>, _ number2: UnsafeMutablePointer<Decimal>, _ roundingMode: NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError
```

#### Discussion

[`Decimal`](decimal.md) instances are represented in memory as a mantissa and an exponent, expressing the value mantissa x 10^exponent. A number can have many representations; for example, the following table lists several valid representations for the number 100:

| Mantissa | Exponent |
| --- | --- |
| 100 | 0 |
| 10 | 1 |
| 1 | 2 |

Format `number1` and `number2` so that they have equal exponents. This format makes addition and subtraction very convenient. Both [`NSDecimalAdd(_:_:_:_:)`](nsdecimaladd(_:_:_:_:).md) and [`NSDecimalSubtract(_:_:_:_:)`](nsdecimalsubtract(_:_:_:_:).md) call [`NSDecimalNormalize(_:_:_:)`](nsdecimalnormalize(_:_:_:).md). You may want to use it if you write more complicated addition or subtraction routines.

For explanations of the possible return values, see [`NSDecimalAdd(_:_:_:_:)`](nsdecimaladd(_:_:_:_:).md).

For more information, see [`Number and Value Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

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
- [typealias RoundingMode](decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnormalize(_:_:_:))*