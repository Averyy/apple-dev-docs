# UnitPower

**Framework**: Foundation  
**Kind**: class

A unit of measure for power.

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
class UnitPower
```

#### Overview

You typically use instances of [`UnitPower`](unitpower.md) to represent specific quantities of power using the [`NSMeasurement`](nsmeasurement.md) class.

##### Power

Power is the amount of energy used over time. The SI unit for power is the watt (W), which is derived as one joule per second (1W = 1J / 1s).

The [`UnitPower`](unitpower.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`watts`](unitpower/watts.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Terawatts | [`terawatts`](unitpower/terawatts.md) | TW | `1e12` |
| Gigawatts | [`gigawatts`](unitpower/gigawatts.md) | GW | `1e9` |
| Megawatts | [`megawatts`](unitpower/megawatts.md) | MW | `1000000.0` |
| Kilowatts | [`kilowatts`](unitpower/kilowatts.md) | kW | `1000.0` |
| Watts | [`watts`](unitpower/watts.md) | W | `1` |
| Milliwatts | [`milliwatts`](unitpower/milliwatts.md) | mW | `0.001` |
| Microwatts | [`microwatts`](unitpower/microwatts.md) | µW | `0.000001` |
| Nanowatts | [`nanowatts`](unitpower/nanowatts.md) | nW | `1e-9` |
| Picowatts | [`picowatts`](unitpower/picowatts.md) | pW | `1e-12` |
| Femtowatts | [`femtowatts`](unitpower/femtowatts.md) | fW | `1e-15` |
| Horsepower | [`horsepower`](unitpower/horsepower.md) | hp | `745.7` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var terawatts: UnitPower](unitpower/terawatts.md)
  The terawatts unit of power.
- [class var gigawatts: UnitPower](unitpower/gigawatts.md)
  The gigawatts unit of power.
- [class var megawatts: UnitPower](unitpower/megawatts.md)
  The megawatts unit of power.
- [class var kilowatts: UnitPower](unitpower/kilowatts.md)
  The kilowatts unit of power.
- [class var watts: UnitPower](unitpower/watts.md)
  The watts unit of power.
- [class var milliwatts: UnitPower](unitpower/milliwatts.md)
  The milliwatts unit of power.
- [class var microwatts: UnitPower](unitpower/microwatts.md)
  The microwatts unit of power.
- [class var nanowatts: UnitPower](unitpower/nanowatts.md)
  The nanowatts unit of power.
- [class var picowatts: UnitPower](unitpower/picowatts.md)
  The picowatts unit of power.
- [class var femtowatts: UnitPower](unitpower/femtowatts.md)
  The femtowatts unit of power.
- [class var horsepower: UnitPower](unitpower/horsepower.md)
  The horsepower unit of power.

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

- [class UnitEnergy](unitenergy.md)
  A unit of measure for energy.
- [class UnitTemperature](unittemperature.md)
  A unit of measure for temperature.
- [class UnitIlluminance](unitilluminance.md)
  A unit of measure for illuminance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitpower)*