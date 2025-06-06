# Units and Measurement

**Framework**: Foundation

Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.

## Topics

### Essentials
- [struct Measurement](measurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class NSMeasurement](nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Unit](unit.md)
  An abstract class representing a unit of measure.
- [class Dimension](dimension.md)
  An abstract class representing a dimensional unit of measure.
### Conversion
- [class UnitConverter](unitconverter.md)
  An abstract class that provides a description of how to convert a unit to and from the base unit of its dimension.
- [class UnitConverterLinear](unitconverterlinear.md)
  A description of how to convert between units using a linear equation.
### Physical Dimension
- [class UnitArea](unitarea.md)
  A unit of measure for area.
- [class UnitLength](unitlength.md)
  A unit of measure for length.
- [class UnitVolume](unitvolume.md)
  A unit of measure for volume.
- [class UnitAngle](unitangle.md)
  A unit of measure for planar angle and rotation.
### Mass, Weight, and Force
- [class UnitMass](unitmass.md)
  A unit of measure for mass.
- [class UnitPressure](unitpressure.md)
  A unit of measure for pressure.
### Time and Motion
- [class UnitAcceleration](unitacceleration.md)
  A unit of measure for acceleration.
- [class UnitDuration](unitduration.md)
  A unit of measure for a duration of time.
- [class UnitFrequency](unitfrequency.md)
  A unit of measure for frequency.
- [class UnitSpeed](unitspeed.md)
  A unit of measure for speed.
### Energy, Heat, and Light
- [class UnitEnergy](unitenergy.md)
  A unit of measure for energy.
- [class UnitPower](unitpower.md)
  A unit of measure for power.
- [class UnitTemperature](unittemperature.md)
  A unit of measure for temperature.
- [class UnitIlluminance](unitilluminance.md)
  A unit of measure for illuminance.
### Electricity
- [class UnitElectricCharge](unitelectriccharge.md)
  A unit of measure for electric charge.
- [class UnitElectricCurrent](unitelectriccurrent.md)
  A unit of measure for electric current.
- [class UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
  A unit of measure for electric potential difference.
- [class UnitElectricResistance](unitelectricresistance.md)
  A unit of measure for electric resistance.
### Concentration and Dispersion
- [class UnitConcentrationMass](unitconcentrationmass.md)
  A unit of measure for concentration of mass.
- [class UnitDispersion](unitdispersion.md)
  A unit of measure for specific quantities of dispersion.
### Fuel Efficiency
- [class UnitFuelEfficiency](unitfuelefficiency.md)
  A unit of measure for fuel efficiency.
### Data Storage
- [class UnitInformationStorage](unitinformationstorage.md)
  A unit of measure for quantities of information.
### Formatting Measurements
- [struct MeasurementFormatUnitUsage](measurementformatunitusage.md)
  A type that provides the generalized usage for a formatted measurement.

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/units-and-measurement)*