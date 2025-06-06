# UnitTemperature

**Framework**: Foundation  
**Kind**: class

A unit of measure for temperature.

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
class UnitTemperature
```

#### Overview

You typically use instances of [`UnitTemperature`](unittemperature.md) to represent specific quantities of temperature using the [`NSMeasurement`](nsmeasurement.md) class.

##### Temperature

Temperature is a comparative measure of thermal energy. The SI unit for temperature is the kelvin (K), which is defined in terms of the triple point of water. Temperature is also commonly measured by degrees of various scales, including Celsius (°C) and Fahrenheit (°F).

The [`UnitTemperature`](unittemperature.md) class defines its [`baseUnit()`](dimension/baseunit().md) to be [`kelvin`](unittemperature/kelvin.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients and constants:

| Name | Method | Symbol | Coefficient | Constant |
| --- | --- | --- | --- | --- |
| Kelvin | [`kelvin`](unittemperature/kelvin.md) | K | `1` | `0` |
| Degree Celsius | [`celsius`](unittemperature/celsius.md) | °C | `1.0` | `273.15` |
| Degree Fahrenheit | [`fahrenheit`](unittemperature/fahrenheit.md) | °F | `0.55555555555556` | `255.37222222222427` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var kelvin: UnitTemperature](unittemperature/kelvin.md)
  The kelvin unit of temperature.
- [class var celsius: UnitTemperature](unittemperature/celsius.md)
  The degree Celsius unit of temperature.
- [class var fahrenheit: UnitTemperature](unittemperature/fahrenheit.md)
  The degree Fahrenheit unit of temperature.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitTemperature>)](unittemperature/init(forlocale:usage:).md)

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
- [class UnitPower](unitpower.md)
  A unit of measure for power.
- [class UnitIlluminance](unitilluminance.md)
  A unit of measure for illuminance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unittemperature)*