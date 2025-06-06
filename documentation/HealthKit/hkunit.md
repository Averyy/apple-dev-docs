# HKUnit

**Framework**: HealthKit  
**Kind**: class

A class for managing the units of measure within HealthKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKUnit
```

## Mentions

- [Defining and converting units and quantities](defining-and-converting-units-and-quantities.md)

#### Overview

The unit class supports most standard SI units (meters, seconds, and grams), SI units with prefixes (centimeters, milliseconds and kilograms) and equivalent non-SI units (feet, minutes, and pounds). HealthKit also supports creating complex units by mathematically combining existing units.

You use units when working with HealthKit quantities. Quantities store both the value (as a `double` data type) and its corresponding unit. You can then request the value from the quantity in any compatible units. For more information on working with quantities, see [`HKQuantity`](hkquantity.md).

> **Note**: Number formatters that use units (for example, [`EnergyFormatter`](https://developer.apple.com/documentation/Foundation/EnergyFormatter), [`LengthFormatter`](https://developer.apple.com/documentation/Foundation/LengthFormatter), and [`MassFormatter`](https://developer.apple.com/documentation/Foundation/MassFormatter)) use a custom enumeration to specify their units. For example, the [`EnergyFormatter`](https://developer.apple.com/documentation/Foundation/EnergyFormatter) class uses the [`EnergyFormatter.Unit`](https://developer.apple.com/documentation/Foundation/EnergyFormatter/Unit) enum. The [`HKUnit`](hkunit.md) class provides several methods to translate between the formatter enumerations and the HealthKit units. For more information, see Working with formatter units.

Number formatters that use units (for example, [`EnergyFormatter`](https://developer.apple.com/documentation/Foundation/EnergyFormatter), [`LengthFormatter`](https://developer.apple.com/documentation/Foundation/LengthFormatter), and [`MassFormatter`](https://developer.apple.com/documentation/Foundation/MassFormatter)) use a custom enumeration to specify their units. For example, the [`EnergyFormatter`](https://developer.apple.com/documentation/Foundation/EnergyFormatter) class uses the [`EnergyFormatter.Unit`](https://developer.apple.com/documentation/Foundation/EnergyFormatter/Unit) enum. The [`HKUnit`](hkunit.md) class provides several methods to translate between the formatter enumerations and the HealthKit units. For more information, see Working with formatter units.

##### Using Units

Like many HealthKit classes, the `HKUnit` class is not extendable and should not be subclassed.

The `HKUnit` class is implemented using a facade design pattern. It uses custom subclasses to represent instances of the different unit types. For example, the [`second()`](hkunit/second().md) convenience method actually returns an instance of the private `HKTimeUnit` subclass.

Additionally, the unit class uses a single unit instance to represent all copies of the same unit in your app, wherever possible. For example, two calls to the [`second()`](hkunit/second().md) method return the same unit object. This helps reduce the amount of memory used by unit instances.

## Topics

### Working with units
- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [var unitString: String](hkunit/unitstring.md)
  A string representation of the unit object.
- [func isNull() -> Bool](hkunit/isnull.md)
  Returns a Boolean value indicating whether the unit is null.
### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](hkunit/energyformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](hkunit/init(from:)-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](hkunit/lengthformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](hkunit/init(from:)-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](hkunit/massformatterunit(from:).md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](hkunit/init(from:)-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.
### Constructing mass units
- [class func gram() -> Self](hkunit/gram.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func gramUnit(with: HKMetricPrefix) -> Self](hkunit/gramunit(with:).md)
  Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.
- [class func ounce() -> Self](hkunit/ounce.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](hkunit/pound.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](hkunit/stone.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](hkunit/moleunit(withmolarmass:).md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](hkunit/moleunit(with:molarmass:).md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.
### Constructing length units
- [class func meter() -> Self](hkunit/meter.md)
  Returns a HealthKit unit for measuring length in meters.
- [class func meterUnit(with: HKMetricPrefix) -> Self](hkunit/meterunit(with:).md)
  Returns a HealthKit unit for measuring length, using meter units with the provided prefix.
- [class func inch() -> Self](hkunit/inch.md)
  Returns a HealthKit unit for measuring length in inches.
- [class func foot() -> Self](hkunit/foot.md)
  Returns a HealthKit unit for measuring length in feet.
- [class func yard() -> Self](hkunit/yard.md)
  Returns a HealthKit unit for measuring length in yards.
- [class func mile() -> Self](hkunit/mile.md)
  Returns a HealthKit unit for measuring length in miles.
### Constructing volume units
- [class func liter() -> Self](hkunit/liter.md)
  Returns a HealthKit unit for measuring volume in liters.
- [class func literUnit(with: HKMetricPrefix) -> Self](hkunit/literunit(with:).md)
  Returns a HealthKit unit for measuring volume, using liter units with the provided prefix.
- [class func fluidOunceUS() -> Self](hkunit/fluidounceus.md)
  Returns a HealthKit unit for measuring volume in US fluid ounces.
- [class func fluidOunceImperial() -> Self](hkunit/fluidounceimperial.md)
  Returns a HealthKit unit for measuring volume in imperial fluid ounces.
- [class func cupUS() -> Self](hkunit/cupus.md)
  Returns a HealthKit unit for measuring volume in US cups.
- [class func cupImperial() -> Self](hkunit/cupimperial.md)
  Returns a HealthKit unit for measuring volume in imperial cups.
- [class func pintUS() -> Self](hkunit/pintus.md)
  Returns a HealthKit unit for measuring volume in US pints.
- [class func pintImperial() -> Self](hkunit/pintimperial.md)
  Returns a HealthKit unit for measuring volume in imperial pints.
### Constructing pressure units
- [class func pascal() -> Self](hkunit/pascal.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func pascalUnit(with: HKMetricPrefix) -> Self](hkunit/pascalunit(with:).md)
  Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.
- [class func millimeterOfMercury() -> Self](hkunit/millimeterofmercury.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func inchesOfMercury() -> Self](hkunit/inchesofmercury.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](hkunit/centimeterofwater.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](hkunit/atmosphere.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](hkunit/decibelaweightedsoundpressurelevel.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.
### Constructing time units
- [class func second() -> Self](hkunit/second.md)
  Returns a HealthKit unit for measuring time in seconds.
- [class func secondUnit(with: HKMetricPrefix) -> Self](hkunit/secondunit(with:).md)
  Returns a HealthKit unit for measuring time, using second units with the provided prefix.
- [class func minute() -> Self](hkunit/minute.md)
  Returns a HealthKit unit for measuring time in minutes.
- [class func hour() -> Self](hkunit/hour.md)
  Returns a HealthKit unit for measuring time in hours.
- [class func day() -> Self](hkunit/day.md)
  Returns a HealthKit unit for measuring time in days.
### Constructing energy units
- [class func joule() -> Self](hkunit/joule.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](hkunit/jouleunit(with:).md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](hkunit/kilocalorie.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](hkunit/largecalorie.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](hkunit/smallcalorie.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](hkunit/calorie.md)
  Returns a HealthKit unit for measuring energy in calories.
### Constructing power units
- [class func watt() -> Self](hkunit/watt.md)
  Returns a HealthKit unit for measuring power in watts.
- [class func wattUnit(with: HKMetricPrefix) -> Self](hkunit/wattunit(with:).md)
  Returns a HealthKit unit for measuring power, using watt units with the provided prefix.
### Constructing temperature units
- [class func degreeCelsius() -> Self](hkunit/degreecelsius.md)
  Returns a HealthKit unit for measuring temperature in degrees Celsius.
- [class func degreeFahrenheit() -> Self](hkunit/degreefahrenheit.md)
  Returns a HealthKit unit for measuring temperature in degrees Fahrenheit.
- [class func kelvin() -> Self](hkunit/kelvin.md)
  Returns a HealthKit unit for measuring temperature in kelvins.
### Constructing hearing sensitivity units
- [class func decibelHearingLevel() -> Self](hkunit/decibelhearinglevel.md)
  Returns a HealthKit unit for measuring the intensity of a sound.
### Constructing frequency units
- [class func hertz() -> Self](hkunit/hertz.md)
  Returns a HealthKit unit for measuring frequency in hertz.
- [class func hertzUnit(with: HKMetricPrefix) -> Self](hkunit/hertzunit(with:).md)
  Returns a HealthKit unit for measuring frequency in hertz with the provided prefix.
### Constructing vision units
- [class func diopter() -> Self](hkunit/diopter.md)
  Returns a HealthKit unit for measuring the optical power of a lens using diopter units.
- [class func prismDiopter() -> Self](hkunit/prismdiopter.md)
  Returns a HealthKit unit for measuring the prismatic deviation of a lens using prism diopter units.
### Constructing angle units
- [class func degreeAngle() -> Self](hkunit/degreeangle.md)
  Returns a HealthKit unit for measuring angles using degrees.
- [class func radianAngle() -> Self](hkunit/radianangle.md)
  Returns a HealthKit unit for measuring angles using radians.
- [class func radianAngleUnit(with: HKMetricPrefix) -> Self](hkunit/radianangleunit(with:).md)
  Returns a HealthKit unit for measuring angles, using radian units with the provided prefix.
### Constructing electrical conductance units
- [class func siemen() -> Self](hkunit/siemen.md)
  Returns a HealthKit unit for measuring electrical conductance in siemens.
- [class func siemenUnit(with: HKMetricPrefix) -> Self](hkunit/siemenunit(with:).md)
  Returns a HealthKit unit for measuring electrical conductance, using siemen units with the provided prefix.
### Electrical potential difference
- [class func volt() -> Self](hkunit/volt.md)
  Returns a HealthKit unit for measuring the difference in electrical potential using volts.
- [class func voltUnit(with: HKMetricPrefix) -> Self](hkunit/voltunit(with:).md)
  Returns a HealthKit unit for measuring the electrical potential difference in volts with the provided prefix.
### Constructing pharmacology units
- [class func internationalUnit() -> Self](hkunit/internationalunit.md)
  Returns a HealthKit unit that measures the amount of a biologically active substance in international units (IU).
### Constructing scalar units
- [class func count() -> Self](hkunit/count.md)
  Returns a HealthKit unit for measuring counts.
- [class func percent() -> Self](hkunit/percent.md)
  Returns a HealthKit unit for measuring percentages.
### Performing unit math
- [func unitMultiplied(by: HKUnit) -> HKUnit](hkunit/unitmultiplied(by:).md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitDivided(by: HKUnit) -> HKUnit](hkunit/unitdivided(by:).md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func unitRaised(toPower: Int) -> HKUnit](hkunit/unitraised(topower:).md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](hkunit/reciprocal.md)
  Returns a complex unit representing the unit’s reciprocal.
### Constants
- [enum HKMetricPrefix](hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.
### Type Methods
- [class func appleEffortScore() -> Self](hkunit/appleeffortscore.md)
- [class func lux() -> Self](hkunit/lux.md)
  Returns a HealthKit unit for measuring illuminance in lux.
- [class func luxUnit(with: HKMetricPrefix) -> Self](hkunit/luxunit(with:).md)
  Returns a HealthKit unit for measuring illuminance, using lux units with the provided prefix.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Defining and converting units and quantities](defining-and-converting-units-and-quantities.md)
  Create and convert units and quantities.
- [class HKQuantity](hkquantity.md)
  An object that stores a value for a given unit.
- [enum HKMetricPrefix](hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit)*