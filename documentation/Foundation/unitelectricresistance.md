# UnitElectricResistance

**Framework**: Foundation  
**Kind**: class

A unit of measure for electric resistance.

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
class UnitElectricResistance
```

#### Overview

You typically use instances of [`UnitElectricResistance`](unitelectricresistance.md) to represent specific quantities of electric resistance using the [`NSMeasurement`](nsmeasurement.md) class.

##### Electric Resistance

Electric resistance is the difficulty of passing an electric current through a conductor. The SI unit for electric resistance is the ohm (Ω), which is derived as the electric resistance that produces one ampere of current between two points in conductor with one volt of electric potential difference (1Ω = 1V/1A).

The [`UnitElectricResistance`](unitelectricresistance.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`ohms`](unitelectricresistance/ohms.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Megaohms | [`megaohms`](unitelectricresistance/megaohms.md) | MΩ | `1000000.0` |
| Kiloohms | [`kiloohms`](unitelectricresistance/kiloohms.md) | kΩ | `1000.0` |
| Ohms | [`ohms`](unitelectricresistance/ohms.md) | Ω | `1.0` |
| Milliohms | [`milliohms`](unitelectricresistance/milliohms.md) | mΩ | `0.001` |
| Microohms | [`microohms`](unitelectricresistance/microohms.md) | µΩ | `0.000001` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var megaohms: UnitElectricResistance](unitelectricresistance/megaohms.md)
  The megaohms unit of electric resistance.
- [class var kiloohms: UnitElectricResistance](unitelectricresistance/kiloohms.md)
  The kiloohms unit of electric resistance.
- [class var ohms: UnitElectricResistance](unitelectricresistance/ohms.md)
  The ohms unit of electric resistance.
- [class var milliohms: UnitElectricResistance](unitelectricresistance/milliohms.md)
  The milliohms unit of electric resistance.
- [class var microohms: UnitElectricResistance](unitelectricresistance/microohms.md)
  The microohms unit of electric resistance.

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

- [class UnitElectricCharge](unitelectriccharge.md)
  A unit of measure for electric charge.
- [class UnitElectricCurrent](unitelectriccurrent.md)
  A unit of measure for electric current.
- [class UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
  A unit of measure for electric potential difference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitelectricresistance)*