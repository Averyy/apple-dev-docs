# NSDecimalNumber.RoundingMode

**Framework**: Foundation  
**Kind**: enum

These constants specify rounding behaviors.

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
enum RoundingMode
```

#### Overview

The rounding mode matters only if the [`scale()`](nsdecimalnumberbehaviors/scale().md) method sets a limit on the precision of `NSDecimalNumber` return values. It has no effect if [`scale()`](nsdecimalnumberbehaviors/scale().md) returns `NSDecimalNoScale`. Assuming that [`scale()`](nsdecimalnumberbehaviors/scale().md) returns 1, the rounding mode has the following effects on various original values:

| Original Value | NSRoundPlain | NSRoundDown & NS RoundUp | NSRoundBankers |
| --- | --- | --- | --- |
| 1.24 | 1.2 | 1.2 & 1.3 | 1.2 |
| 1.26 | 1.3 | 1.2 & 1.3 | 1.3 |
| 1.25 | 1.3 | 1.2 & 1.3 | 1.2 |
| 1.35 | 1.4 | 1.3  & 1.4 | 1.4 |
| –1.35 | –1.4 | –1.4  & -1.3 | –1.4 |

## Topics

### Constants
- [NSDecimalNumber.RoundingMode.plain](nsdecimalnumber/roundingmode/plain.md)
  Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSDecimalNumber.RoundingMode.down](nsdecimalnumber/roundingmode/down.md)
  Round return values down.
- [NSDecimalNumber.RoundingMode.up](nsdecimalnumber/roundingmode/up.md)
  Round return values up.
- [NSDecimalNumber.RoundingMode.bankers](nsdecimalnumber/roundingmode/bankers.md)
  Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.
- [NSDecimalNumber.RoundingMode.plain](nsdecimalnumber/roundingmode/plain.md)
  Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSDecimalNumber.RoundingMode.down](nsdecimalnumber/roundingmode/down.md)
  Round return values down.
- [NSDecimalNumber.RoundingMode.up](nsdecimalnumber/roundingmode/up.md)
  Round return values up.
- [NSDecimalNumber.RoundingMode.bankers](nsdecimalnumber/roundingmode/bankers.md)
  Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.
### Initializers
- [init?(rawValue: UInt)](nsdecimalnumber/roundingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [typealias CalculationError](decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/roundingmode)*