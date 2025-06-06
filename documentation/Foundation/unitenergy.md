# UnitEnergy

**Framework**: Foundation  
**Kind**: class

A unit of measure for energy.

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
class UnitEnergy
```

#### Overview

You typically use instances of [`UnitEnergy`](unitenergy.md) to represent specific quantities of energy using the [`NSMeasurement`](nsmeasurement.md) class.

##### Energy

Energy is a fundamental property of matter than can be transferred and converted into different forms, such as kinetic, electric, and thermal. The SI unit for energy is the joule (J), which is derived as the work of one meter of displacement in the direction of a force of one newton (1J = 1N ∙ 1m). It can also be derived as the work required to displace an electric charge of one coulomb through an electrical potential difference of one volt (1J = 1C ∙ 1V), or the work required to produce one watt of power for one second (1J = 1W ∙ 1s). Energy is also commonly expressed in terms of the calorie (cal), or the energy needed to raise the temperature of one gram of water by one degree Celsius at a pressure of one atmosphere (1cal ≡ 4.184J).

The [`UnitEnergy`](unitenergy.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`joules`](unitenergy/joules.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Kilojoules | [`kilojoules`](unitenergy/kilojoules.md) | kJ | `1000.0` |
| Joules | [`joules`](unitenergy/joules.md) | J | `1.0` |
| Kilocalories | [`kilocalories`](unitenergy/kilocalories.md) | kCal | `4184.0` |
| Calories | [`calories`](unitenergy/calories.md) | cal | `4.184` |
| Kilowatt Hours | [`kilowattHours`](unitenergy/kilowatthours.md) | kWh | `3600000.0` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var kilojoules: UnitEnergy](unitenergy/kilojoules.md)
  The kilojoules unit of energy.
- [class var joules: UnitEnergy](unitenergy/joules.md)
  The joules unit of energy.
- [class var kilocalories: UnitEnergy](unitenergy/kilocalories.md)
  The kilocalories unit of energy.
- [class var calories: UnitEnergy](unitenergy/calories.md)
  The calories unit of energy.
- [class var kilowattHours: UnitEnergy](unitenergy/kilowatthours.md)
  The kilowatt hours unit of energy.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitEnergy>)](unitenergy/init(forlocale:usage:).md)

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

- [class UnitPower](unitpower.md)
  A unit of measure for power.
- [class UnitTemperature](unittemperature.md)
  A unit of measure for temperature.
- [class UnitIlluminance](unitilluminance.md)
  A unit of measure for illuminance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitenergy)*