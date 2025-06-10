# UnitElectricPotentialDifference

**Framework**: Foundation  
**Kind**: class

A unit of measure for electric potential difference.

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
class UnitElectricPotentialDifference
```

#### Overview

You typically use instances of [`UnitElectricPotentialDifference`](unitelectricpotentialdifference.md) to represent specific quantities of electric potential difference using the [`NSMeasurement`](nsmeasurement.md) class.

##### Electric Potential Difference

Electric potential difference is the amount of electric potential energy of a point charge at a point in space. The SI unit for electric potential difference is the volt (V), which is derived as the difference in electric potential energy between two points of a linear conductor when an electric current of one ampere dissipates one watt of power between those points (1V = 1W/1A).

The [`UnitElectricPotentialDifference`](unitelectricpotentialdifference.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`volts`](unitelectricpotentialdifference/volts.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Megavolts | [`megavolts`](unitelectricpotentialdifference/megavolts.md) | MV | `1000000.0` |
| Kilovolts | [`kilovolts`](unitelectricpotentialdifference/kilovolts.md) | kV | `1000.0` |
| Volts | [`volts`](unitelectricpotentialdifference/volts.md) | V | `1.0` |
| Millivolts | [`millivolts`](unitelectricpotentialdifference/millivolts.md) | mV | `0.001` |
| Microvolts | [`microvolts`](unitelectricpotentialdifference/microvolts.md) | µV | `0.000001` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var megavolts: UnitElectricPotentialDifference](unitelectricpotentialdifference/megavolts.md)
  The megavolts unit of electric potential difference.
- [class var kilovolts: UnitElectricPotentialDifference](unitelectricpotentialdifference/kilovolts.md)
  The kilovolts unit of electric potential difference.
- [class var volts: UnitElectricPotentialDifference](unitelectricpotentialdifference/volts.md)
  The volts unit of electric potential difference.
- [class var millivolts: UnitElectricPotentialDifference](unitelectricpotentialdifference/millivolts.md)
  The millivolts unit of electric potential difference.
- [class var microvolts: UnitElectricPotentialDifference](unitelectricpotentialdifference/microvolts.md)
  The microvolts unit of electric potential difference.

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
- [class UnitElectricResistance](unitelectricresistance.md)
  A unit of measure for electric resistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference)*