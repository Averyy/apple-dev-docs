# UnitElectricCurrent

**Framework**: Foundation  
**Kind**: class

A unit of measure for electric current.

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
class UnitElectricCurrent
```

#### Overview

You typically use instances of [`UnitElectricCurrent`](unitelectriccurrent.md) to represent specific quantities of electric current using the [`NSMeasurement`](nsmeasurement.md) class.

##### Electric Current

Electric current is the flow of electric charge. The SI unit for electric current is the ampere (A), which is defined in terms the production of electromagnetic force between two parallel linear conductors. It can also be expressed as the flow of one coulomb per second (1A = 1C / s).

The [`UnitElectricCurrent`](unitelectriccurrent.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`amperes`](unitelectriccurrent/amperes.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Megaamperes | [`megaamperes`](unitelectriccurrent/megaamperes.md) | MA | `1000000.0` |
| Kiloamperes | [`kiloamperes`](unitelectriccurrent/kiloamperes.md) | kA | `1000.0` |
| Amperes | [`amperes`](unitelectriccurrent/amperes.md) | A | `1.0` |
| Milliamperes | [`milliamperes`](unitelectriccurrent/milliamperes.md) | mA | `0.001` |
| Microamperes | [`microamperes`](unitelectriccurrent/microamperes.md) | µA | `0.000001` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var megaamperes: UnitElectricCurrent](unitelectriccurrent/megaamperes.md)
  The megaamperes unit of electric current.
- [class var kiloamperes: UnitElectricCurrent](unitelectriccurrent/kiloamperes.md)
  The kiloamperes unit of electric current.
- [class var amperes: UnitElectricCurrent](unitelectriccurrent/amperes.md)
  The amperes unit of electric current.
- [class var milliamperes: UnitElectricCurrent](unitelectriccurrent/milliamperes.md)
  The milliamperes unit of electric current.
- [class var microamperes: UnitElectricCurrent](unitelectriccurrent/microamperes.md)
  The microamperes unit of electric current.

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

## See Also

- [class UnitElectricCharge](unitelectriccharge.md)
  A unit of measure for electric charge.
- [class UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
  A unit of measure for electric potential difference.
- [class UnitElectricResistance](unitelectricresistance.md)
  A unit of measure for electric resistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitelectriccurrent)*