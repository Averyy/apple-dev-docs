# Dimension

**Framework**: Foundation  
**Kind**: class

An abstract class representing a dimensional unit of measure.

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
class Dimension
```

#### Overview

The Foundation framework provides concrete subclasses for many of the most common types of physical units.

Table 1: [`Dimension`](dimension.md) subclasses.

| NSDimension subclass | Description | Base unit |
| --- | --- | --- |
| [`UnitAcceleration`](unitacceleration.md) | Unit of measure for acceleration | meters per second squared (m/s²) |
| [`UnitAngle`](unitangle.md) | Unit of measure for planar angle and rotation | degrees (°) |
| [`UnitArea`](unitarea.md) | Unit of measure for area | square meters (m²) |
| [`UnitConcentrationMass`](unitconcentrationmass.md) | Unit of measure for concentration of mass | grams per liter (g/L) |
| [`UnitDispersion`](unitdispersion.md) | Unit of measure for dispersion | parts per million (ppm) |
| [`UnitDuration`](unitduration.md) | Unit of measure for duration of time | seconds (sec) |
| [`UnitElectricCharge`](unitelectriccharge.md) | Unit of measure for electric charge | coulombs (C) |
| [`UnitElectricCurrent`](unitelectriccurrent.md) | Unit of measure for electric current | amperes (A) |
| [`UnitElectricPotentialDifference`](unitelectricpotentialdifference.md) | Unit of measure for electric potential difference | volts (V) |
| [`UnitElectricResistance`](unitelectricresistance.md) | Unit of measure for electric resistance | ohms (Ω) |
| [`UnitEnergy`](unitenergy.md) | Unit of measure for energy | joules (J) |
| [`UnitFrequency`](unitfrequency.md) | Unit of measure for frequency | hertz (Hz) |
| [`UnitFuelEfficiency`](unitfuelefficiency.md) | Unit of measure for fuel efficiency | liters per 100 kilometers (L/100km) |
| [`UnitIlluminance`](unitilluminance.md) | Unit of measure for illuminance | lux (lx) |
| [`UnitInformationStorage`](unitinformationstorage.md) | Unit of measure for quantities of information | bytes (b) |
| [`UnitLength`](unitlength.md) | Unit of measure for length | meters (m) |
| [`UnitMass`](unitmass.md) | Unit of measure for mass | kilograms (kg) |
| [`UnitPower`](unitpower.md) | Unit of measure for power | watts (W) |
| [`UnitPressure`](unitpressure.md) | Unit of measure for pressure | newtons per square meter (N/m²) |
| [`UnitSpeed`](unitspeed.md) | Unit of measure for speed | meters per second (m/s) |
| [`UnitTemperature`](unittemperature.md) | Unit of measure for temperature | kelvin (K) |
| [`UnitVolume`](unitvolume.md) | Unit of measure for volume | liters (L) |

Each instance of a [`Dimension`](dimension.md) subclass has a [`converter`](dimension/converter.md), which represents the unit in terms of the dimension’s [`baseUnit()`](dimension/baseunit().md). For example, the `NSLengthUnit` class uses [`meters`](unitlength/meters.md) as its base unit. The system defines the predefined [`miles`](unitlength/miles.md) unit by a [`UnitConverterLinear`](unitconverterlinear.md) with a [`coefficient`](unitconverterlinear/coefficient.md) of `1609.34`, which corresponds to the conversion ratio of miles to meters (1 mi = 1609.34 m); the system defines the predefined [`meters`](unitlength/meters.md) unit by a [`UnitConverterLinear`](unitconverterlinear.md) with a [`coefficient`](unitconverterlinear/coefficient.md) of `1.0` because it’s the base unit.

You typically use an `NSDimension` subclass in conjunction with the [`NSMeasurement`](nsmeasurement.md) class to represent specific quantities of a particular unit.

##### Working with Custom Units

In addition to the Apple-provided units, you can define custom units. You can initialize custom units from a symbol and converter of an existing type or implemented as a class method of an existing type for additional convenience. You can also define your own `NSDimension` subclass to represent an entirely new unit dimension.

###### Initializing a Custom Unit with a Specified Symbol and Definition

The simplest way to define a custom unit is to create a new instance of an existing `NSDimension` subclass using the [`init(symbol:converter:)`](dimension/init(symbol:converter:).md) method.

For example, the  is a nonstandard unit of length (1 smoot = 1.70180 m). You can create a new instance of [`UnitLength`](unitlength.md) as follows:

###### Extending Existing Dimension Subclasses

Alternatively, if you use a custom unit extensively throughout an app, consider extending the corresponding [`Dimension`](dimension.md) subclass and adding a static variable.

For example, a measurement of speed can be furlongs per fortnight (1 fur/ftn = 201.168 m / 1,209,600 s). If an app makes frequent use of this unit, you can extend [`UnitSpeed`](unitspeed.md) to add a `furlongsPerFortnight` static variable for convenient access as follows:

###### Creating a Custom Dimension Subclass

You can create a new subclass of [`Dimension`](dimension.md) to describe a new unit dimension.

For example, the Foundation framework doesn’t define any units for radioactivity. Radioactivity is the process by which the nucleus of an atom emits radiation. The SI unit of measure for radioactivity is the becquerel (Bq), which is the quantity of radioactive material in which one nucleus decays per second (1 Bq = 1 s-1). Radioactivity is also commonly described in terms of curies (Ci), a unit defined relative to the decay of one gram of the radium-226 isotope (1 Ci = 3.7 × 1010 Bq). You can implement a `CustomUnitRadioactivity` class that defines both units of radioactivity as follows:

##### Subclassing Notes

The system provides [`Dimension`](dimension.md) for subclassing. Although the subclasses listed in Table 1 above are suitable for most purposes, you may want to define a custom unit type. For instance, you may need a custom unit type to represent a derived unit, such as magnetic flux (measured as the product of electric potential difference and time).

To represent dimensionless units, subclass [`Unit`](unit.md) directly.

###### Methods to Override

All subclasses must fully implement the [`baseUnit()`](dimension/baseunit().md) method designating the base unit, relative to which you define any additional units.

You must also implement a class method named for the base unit itself, to use interchangeably. For example, the [`UnitIlluminance`](unitilluminance.md) class defines its [`baseUnit()`](dimension/baseunit().md) in terms of the lux (lx) and provides a corresponding [`lux`](unitilluminance/lux.md) class method.

###### Alternatives to Subclassing

As described in [`Working with Custom Units`](dimension#Working-with-Custom-Units.md), you need to create a custom subclass of [`Dimension`](dimension.md) only if you or the system haven’t defined a unit of the desired dimension. You can define a custom unit for an existing [`Dimension`](dimension.md) subclass by either calling the [`init(symbol:converter:)`](dimension/init(symbol:converter:).md) method or extending the subclass and adding a corresponding class method.

## Topics

### Creating Dimensions
- [init(symbol: String, converter: UnitConverter)](dimension/init(symbol:converter:).md)
  Initializes a dimensional unit with the symbol and unit converter you specify.
### Accessing the Unit Converter
- [var converter: UnitConverter](dimension/converter.md)
  The unit converter that represents the unit in terms of the dimension’s base unit.
### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Initializers
- [convenience init(forLocale: Locale)](dimension/init(forlocale:).md)
  Creates a `Dimension` which the specified `locale` prefers.

## Relationships

### Inherits From
- [Unit](unit.md)
### Inherited By
- [UnitAcceleration](unitacceleration.md)
- [UnitAngle](unitangle.md)
- [UnitArea](unitarea.md)
- [UnitConcentrationMass](unitconcentrationmass.md)
- [UnitDispersion](unitdispersion.md)
- [UnitDuration](unitduration.md)
- [UnitElectricCharge](unitelectriccharge.md)
- [UnitElectricCurrent](unitelectriccurrent.md)
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
- [UnitElectricResistance](unitelectricresistance.md)
- [UnitEnergy](unitenergy.md)
- [UnitFrequency](unitfrequency.md)
- [UnitFuelEfficiency](unitfuelefficiency.md)
- [UnitIlluminance](unitilluminance.md)
- [UnitInformationStorage](unitinformationstorage.md)
- [UnitLength](unitlength.md)
- [UnitMass](unitmass.md)
- [UnitPower](unitpower.md)
- [UnitPressure](unitpressure.md)
- [UnitSpeed](unitspeed.md)
- [UnitTemperature](unittemperature.md)
- [UnitVolume](unitvolume.md)
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

- [struct Measurement](measurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class NSMeasurement](nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Unit](unit.md)
  An abstract class representing a unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dimension)*