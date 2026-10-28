# NSDecimalNormalize(_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern NSCalculationError NSDecimalNormalize(NSDecimal *number1, NSDecimal *number2, NSRoundingMode roundingMode);
```

## Discussion

[`Decimal`](./decimal.md) instances are represented in memory as a mantissa and an exponent, expressing the value mantissa x 10^exponent. A number can have many representations; for example, the following table lists several valid representations for the number 100:

| Mantissa | Exponent |
| --- | --- |
| 100 | 0 |
| 10 | 1 |
| 1 | 2 |

Format `number1` and `number2` so that they have equal exponents. This format makes addition and subtraction very convenient. Both [`NSDecimalAdd(_:_:_:_:)`](./nsdecimaladd%28_,_,_,_%29.md) and [`NSDecimalSubtract(_:_:_:_:)`](./nsdecimalsubtract%28_,_,_,_%29.md) call [`NSDecimalNormalize(_:_:_:)`](./nsdecimalnormalize%28_,_,_%29.md). You may want to use it if you write more complicated addition or subtraction routines.

For explanations of the possible return values, see [`NSDecimalAdd(_:_:_:_:)`](./nsdecimaladd%28_,_,_,_%29.md).

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Performing arithmetic using references
- [func NSDecimalCompact(UnsafeMutablePointer<Decimal>)](./nsdecimalcompact%28_%29.md)
  Compacts the decimal structure for efficiency.
- [func NSDecimalAdd(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimaladd%28_,_,_,_%29.md)
  Adds two decimal values.
- [func NSDecimalSubtract(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalsubtract%28_,_,_,_%29.md)
  Subtracts one decimal value from another.
- [func NSDecimalDivide(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimaldivide%28_,_,_,_%29.md)
  Divides one decimal value by another.
- [func NSDecimalMultiply(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalmultiply%28_,_,_,_%29.md)
  Multiplies two decimal numbers together.
- [func NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int16, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalmultiplybypowerof10%28_,_,_,_%29.md)
  Multiplies a decimal by the specified power of 10.
- [func NSDecimalRound(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode)](./nsdecimalround%28_,_,_,_%29.md)
  Rounds off the decimal value.
- [func NSDecimalPower(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalpower%28_,_,_,_%29.md)
  Raises the decimal value to the specified power.
- [typealias RoundingMode](./decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](./nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](./decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](./nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](./nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnormalize(_:_:_:))*