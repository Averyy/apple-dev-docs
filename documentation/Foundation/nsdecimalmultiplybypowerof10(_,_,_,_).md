# NSDecimalMultiplyByPowerOf10(_:_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Multiplies a decimal by the specified power of 10.

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
func NSDecimalMultiplyByPowerOf10(_ result: UnsafeMutablePointer<Decimal>, _ number: UnsafePointer<Decimal>, _ power: Int16, _ roundingMode: NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError
```

```c
extern NSCalculationError NSDecimalMultiplyByPowerOf10(NSDecimal *result, const NSDecimal *number, short power, NSRoundingMode roundingMode);
```

## Discussion

Multiplies `number` by `power` of 10 and stores the product, possibly rounded off according to `roundingMode`, in `result`.

For explanations of the possible return values and rounding modes, see [`NSDecimalAdd(_:_:_:_:)`](./nsdecimaladd%28_,_,_,_%29.md).

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
- [func NSDecimalRound(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode)](./nsdecimalround%28_,_,_,_%29.md)
  Rounds off the decimal value.
- [func NSDecimalPower(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalpower%28_,_,_,_%29.md)
  Raises the decimal value to the specified power.
- [func NSDecimalNormalize(UnsafeMutablePointer<Decimal>, UnsafeMutablePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](./nsdecimalnormalize%28_,_,_%29.md)
  Normalizes the internal format of two decimal numbers to simplify later operations.
- [typealias RoundingMode](./decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](./nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](./decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](./nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](./nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalmultiplybypowerof10(_:_:_:_:))*