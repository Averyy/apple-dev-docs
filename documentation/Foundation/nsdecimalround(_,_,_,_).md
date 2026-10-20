# NSDecimalRound(_:_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Rounds off the decimal value.

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
func NSDecimalRound(_ result: UnsafeMutablePointer<Decimal>, _ number: UnsafePointer<Decimal>, _ scale: Int, _ roundingMode: NSDecimalNumber.RoundingMode)
```

```c
extern void NSDecimalRound(NSDecimal *result, const NSDecimal *number, NSInteger scale, NSRoundingMode roundingMode);
```

#### Discussion

Rounds `number` off according to the parameters `scale` and `roundingMode` and stores the result in `result`.

The `scale` value specifies the number of digits `result` can have after its decimal point. `roundingMode` specifies the way that number is rounded off. There are four possible values for `roundingMode`: [`NSDecimalNumber.RoundingMode.down`](./nsdecimalnumber/roundingmode/down.md), [`NSDecimalNumber.RoundingMode.up`](./nsdecimalnumber/roundingmode/up.md), [`NSDecimalNumber.RoundingMode.plain`](./nsdecimalnumber/roundingmode/plain.md), and [`NSDecimalNumber.RoundingMode.bankers`](./nsdecimalnumber/roundingmode/bankers.md). For thorough discussions of `scale` and `roundingMode`, see [`NSDecimalNumberBehaviors`](./nsdecimalnumberbehaviors.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalround(_:_:_:_:))*