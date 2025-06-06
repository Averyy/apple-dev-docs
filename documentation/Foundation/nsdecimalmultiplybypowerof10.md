# NSDecimalMultiplyByPowerOf10(_:_:_:_:)

**Framework**: Foundation  
**Kind**: func

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

#### Discussion

Multiplies `number` by `power` of 10 and stores the product, possibly rounded off according to `roundingMode`, in `result`.

For explanations of the possible return values and rounding modes, see [`NSDecimalAdd(_:_:_:_:)`](nsdecimaladd(_:_:_:_:).md).

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
- [NSDecimalNumber.CalculationError](nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalmultiplybypowerof10(_:_:_:_:))*