# NSDecimalNumber.RoundingMode

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSRoundingMode : NSUInteger;
```

## Overview

The rounding mode matters only if the [`scale()`](../nsdecimalnumberbehaviors/scale%28%29.md) method sets a limit on the precision of `NSDecimalNumber` return values. It has no effect if [`scale()`](../nsdecimalnumberbehaviors/scale%28%29.md) returns `NSDecimalNoScale`. Assuming that [`scale()`](../nsdecimalnumberbehaviors/scale%28%29.md) returns 1, the rounding mode has the following effects on various original values:

| Original Value | NSRoundPlain | NSRoundDown & NS RoundUp | NSRoundBankers |
| --- | --- | --- | --- |
| 1.24 | 1.2 | 1.2 & 1.3 | 1.2 |
| 1.26 | 1.3 | 1.2 & 1.3 | 1.3 |
| 1.25 | 1.3 | 1.2 & 1.3 | 1.2 |
| 1.35 | 1.4 | 1.3  & 1.4 | 1.4 |
| –1.35 | –1.4 | –1.4  & -1.3 | –1.4 |

## Topics

### Constants
- [NSDecimalNumber.RoundingMode.plain](./roundingmode/plain.md)
  Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSDecimalNumber.RoundingMode.down](./roundingmode/down.md)
  Round return values down.
- [NSDecimalNumber.RoundingMode.up](./roundingmode/up.md)
  Round return values up.
- [NSDecimalNumber.RoundingMode.bankers](./roundingmode/bankers.md)
  Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.
### Initializers
- [init?(rawValue: UInt)](./roundingmode/init%28rawvalue%29.md)

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
- [typealias CalculationError](../decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](./calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](../nsdecimalnumberbehaviors/exceptionduringoperation%28_,error,leftoperand,rightoperand%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/roundingmode)*