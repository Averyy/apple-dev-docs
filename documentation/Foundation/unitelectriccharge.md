# UnitElectricCharge

**Framework**: Foundation  
**Kind**: class

A unit of measure for electric charge.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UnitElectricCharge
```

#### Overview

You typically use instances of [`UnitElectricCharge`](unitelectriccharge.md) to represent specific quantities of electric charge using the [`NSMeasurement`](nsmeasurement.md) class.

##### Electric Charge

Electric charge is a fundamental physical property of matter that causes it to experience a force within an electromagnetic field. The SI unit for electric charge is the coulomb (C), which is defined as the amount of charge carried by a current of one ampere in one second (1C = 1A · 1s). Charge is also commonly expressed in terms of ampere hours (Ah).

The [`UnitElectricCharge`](unitelectriccharge.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`coulombs`](unitelectriccharge/coulombs.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Coulombs | [`coulombs`](unitelectriccharge/coulombs.md) | C | `1.0` |
| Megaampere Hours | [`megaampereHours`](unitelectriccharge/megaamperehours.md) | MAh | `3.6e9` |
| Kiloampere Hours | [`kiloampereHours`](unitelectriccharge/kiloamperehours.md) | kAh | `3600000.0` |
| Ampere Hours | [`ampereHours`](unitelectriccharge/amperehours.md) | Ah | `3600.0` |
| Milliampere Hours | [`milliampereHours`](unitelectriccharge/milliamperehours.md) | mAh | `3.6` |
| Microampere Hours | [`microampereHours`](unitelectriccharge/microamperehours.md) | µAh | `0.0036` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var coulombs: UnitElectricCharge](unitelectriccharge/coulombs.md)
  The coulombs unit of electric charge.
- [class var megaampereHours: UnitElectricCharge](unitelectriccharge/megaamperehours.md)
  The megaampere hours unit of electric charge.
- [class var kiloampereHours: UnitElectricCharge](unitelectriccharge/kiloamperehours.md)
  The kiloampere hours unit of electric charge.
- [class var ampereHours: UnitElectricCharge](unitelectriccharge/amperehours.md)
  The ampere hours unit of electric charge.
- [class var milliampereHours: UnitElectricCharge](unitelectriccharge/milliamperehours.md)
  The milliampere hours unit of electric charge.
- [class var microampereHours: UnitElectricCharge](unitelectriccharge/microamperehours.md)
  The microampere hours unit of electric charge.

## Relationships

### Inherits From
- [Dimension](dimension.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UnitElectricCurrent](unitelectriccurrent.md)
  A unit of measure for electric current.
- [class UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
  A unit of measure for electric potential difference.
- [class UnitElectricResistance](unitelectricresistance.md)
  A unit of measure for electric resistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitelectriccharge)*