# HKUnit

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKUnit : NSObject
```

## Mentions

- [Defining and converting units and quantities](./defining-and-converting-units-and-quantities.md)

## Overview

The unit class supports most standard SI units (meters, seconds, and grams), SI units with prefixes (centimeters, milliseconds and kilograms) and equivalent non-SI units (feet, minutes, and pounds). HealthKit also supports creating complex units by mathematically combining existing units.

You use units when working with HealthKit quantities. Quantities store both the value (as a `double` data type) and its corresponding unit. You can then request the value from the quantity in any compatible units. For more information on working with quantities, see [`HKQuantity`](./hkquantity.md).

> **Note**: Number formatters that use units (for example, [`EnergyFormatter`](../Foundation/energyformatter.md), [`LengthFormatter`](../Foundation/lengthformatter.md), and [`MassFormatter`](../Foundation/massformatter.md)) use a custom enumeration to specify their units. For example, the [`EnergyFormatter`](../Foundation/energyformatter.md) class uses the [`EnergyFormatter.Unit`](../Foundation/energyformatter/unit.md) enum. The [`HKUnit`](./hkunit.md) class provides several methods to translate between the formatter enumerations and the HealthKit units. For more information, see Working with formatter units.

### Using Units

As with many HealthKit classes, don’t subclass the [`HKUnit`](./hkunit.md) class.

The `HKUnit` class is implemented using a facade design pattern. It uses custom subclasses to represent instances of the different unit types. For example, the [`second()`](./hkunit/second%28%29.md) convenience method actually returns an instance of the private `HKTimeUnit` subclass.

Additionally, the unit class uses a single unit instance to represent all copies of the same unit in your app, wherever possible. For example, two calls to the [`second()`](./hkunit/second%28%29.md) method return the same unit object. This helps reduce the amount of memory used by unit instances.

## Topics

### Working with units
- [convenience init(from: String)](./hkunit/init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
- [var unitString: String](./hkunit/unitstring.md)
  A string representation of the unit object.
- [func isNull() -> Bool](./hkunit/isnull%28%29.md)
  Returns a Boolean value indicating whether the unit is null.
### Working with formatter units
- [class func energyFormatterUnit(from: HKUnit) -> EnergyFormatter.Unit](./hkunit/energyformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding energy formatter enumeration value.
- [convenience init(from: EnergyFormatter.Unit)](./hkunit/init%28from%29-1j1pq.md)
  Converts an energy formatter enumeration value into a corresponding HealthKit unit object.
- [class func lengthFormatterUnit(from: HKUnit) -> LengthFormatter.Unit](./hkunit/lengthformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding length formatter enumeration value.
- [convenience init(from: LengthFormatter.Unit)](./hkunit/init%28from%29-55e1u.md)
  Converts a length formatter enumeration value into a corresponding HealthKit object.
- [class func massFormatterUnit(from: HKUnit) -> MassFormatter.Unit](./hkunit/massformatterunit%28from%29.md)
  Converts a HealthKit unit object into a corresponding mass formatter enumeration value.
- [convenience init(from: MassFormatter.Unit)](./hkunit/init%28from%29-7h2li.md)
  Converts a mass formatter enumeration value into a corresponding HealthKit unit object.
### Constructing mass units
- [class func gram() -> Self](./hkunit/gram%28%29.md)
  Returns a HealthKit unit for measuring mass in grams.
- [class func gramUnit(with: HKMetricPrefix) -> Self](./hkunit/gramunit%28with%29.md)
  Returns a HealthKit unit for measuring mass, using gram units with the provided prefix.
- [class func ounce() -> Self](./hkunit/ounce%28%29.md)
  Returns a HealthKit unit for measuring mass in ounces.
- [class func pound() -> Self](./hkunit/pound%28%29.md)
  Returns a HealthKit unit for measuring mass in pounds.
- [class func stone() -> Self](./hkunit/stone%28%29.md)
  Returns a HealthKit unit for measuring mass in stones.
- [class func moleUnit(withMolarMass: Double) -> Self](./hkunit/moleunit%28withmolarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles for a given molar mass.
- [class func moleUnit(with: HKMetricPrefix, molarMass: Double) -> Self](./hkunit/moleunit%28with,molarmass%29.md)
  Returns a HealthKit unit for measuring mass in moles, with the given prefix and molar mass.
- [var HKUnitMolarMassBloodGlucose: Double](./hkunitmolarmassbloodglucose.md)
  The molecular mass of blood glucose, typically used to create mole units for blood glucose.
### Constructing length units
- [class func meter() -> Self](./hkunit/meter%28%29.md)
  Returns a HealthKit unit for measuring length in meters.
- [class func meterUnit(with: HKMetricPrefix) -> Self](./hkunit/meterunit%28with%29.md)
  Returns a HealthKit unit for measuring length, using meter units with the provided prefix.
- [class func inch() -> Self](./hkunit/inch%28%29.md)
  Returns a HealthKit unit for measuring length in inches.
- [class func foot() -> Self](./hkunit/foot%28%29.md)
  Returns a HealthKit unit for measuring length in feet.
- [class func yard() -> Self](./hkunit/yard%28%29.md)
  Returns a HealthKit unit for measuring length in yards.
- [class func mile() -> Self](./hkunit/mile%28%29.md)
  Returns a HealthKit unit for measuring length in miles.
### Constructing volume units
- [class func liter() -> Self](./hkunit/liter%28%29.md)
  Returns a HealthKit unit for measuring volume in liters.
- [class func literUnit(with: HKMetricPrefix) -> Self](./hkunit/literunit%28with%29.md)
  Returns a HealthKit unit for measuring volume, using liter units with the provided prefix.
- [class func fluidOunceUS() -> Self](./hkunit/fluidounceus%28%29.md)
  Returns a HealthKit unit for measuring volume in US fluid ounces.
- [class func fluidOunceImperial() -> Self](./hkunit/fluidounceimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial fluid ounces.
- [class func cupUS() -> Self](./hkunit/cupus%28%29.md)
  Returns a HealthKit unit for measuring volume in US cups.
- [class func cupImperial() -> Self](./hkunit/cupimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial cups.
- [class func pintUS() -> Self](./hkunit/pintus%28%29.md)
  Returns a HealthKit unit for measuring volume in US pints.
- [class func pintImperial() -> Self](./hkunit/pintimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial pints.
### Constructing pressure units
- [class func pascal() -> Self](./hkunit/pascal%28%29.md)
  Returns a HealthKit unit for measuring pressure in pascals.
- [class func pascalUnit(with: HKMetricPrefix) -> Self](./hkunit/pascalunit%28with%29.md)
  Returns a HealthKit unit for measuring pressure, using pascal units with the provided prefix.
- [class func millimeterOfMercury() -> Self](./hkunit/millimeterofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in millimeters of mercury.
- [class func inchesOfMercury() -> Self](./hkunit/inchesofmercury%28%29.md)
  Returns a HealthKit unit for measuring pressure in inches of mercury.
- [class func centimeterOfWater() -> Self](./hkunit/centimeterofwater%28%29.md)
  Returns a HealthKit unit for measuring pressure in centimeters of water.
- [class func atmosphere() -> Self](./hkunit/atmosphere%28%29.md)
  Returns a HealthKit unit for measuring pressure in atmospheres.
- [class func decibelAWeightedSoundPressureLevel() -> Self](./hkunit/decibelaweightedsoundpressurelevel%28%29.md)
  Returns a HealthKit unit for measuring the difference between the local pressure and the ambient atmospheric pressure caused by sound.
### Constructing time units
- [class func second() -> Self](./hkunit/second%28%29.md)
  Returns a HealthKit unit for measuring time in seconds.
- [class func secondUnit(with: HKMetricPrefix) -> Self](./hkunit/secondunit%28with%29.md)
  Returns a HealthKit unit for measuring time, using second units with the provided prefix.
- [class func minute() -> Self](./hkunit/minute%28%29.md)
  Returns a HealthKit unit for measuring time in minutes.
- [class func hour() -> Self](./hkunit/hour%28%29.md)
  Returns a HealthKit unit for measuring time in hours.
- [class func day() -> Self](./hkunit/day%28%29.md)
  Returns a HealthKit unit for measuring time in days.
### Constructing energy units
- [class func joule() -> Self](./hkunit/joule%28%29.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](./hkunit/jouleunit%28with%29.md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](./hkunit/kilocalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](./hkunit/largecalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](./hkunit/smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](./hkunit/calorie%28%29.md)
  Returns a HealthKit unit for measuring energy in calories.
### Constructing power units
- [class func watt() -> Self](./hkunit/watt%28%29.md)
  Returns a HealthKit unit for measuring power in watts.
- [class func wattUnit(with: HKMetricPrefix) -> Self](./hkunit/wattunit%28with%29.md)
  Returns a HealthKit unit for measuring power, using watt units with the provided prefix.
### Constructing temperature units
- [class func degreeCelsius() -> Self](./hkunit/degreecelsius%28%29.md)
  Returns a HealthKit unit for measuring temperature in degrees Celsius.
- [class func degreeFahrenheit() -> Self](./hkunit/degreefahrenheit%28%29.md)
  Returns a HealthKit unit for measuring temperature in degrees Fahrenheit.
- [class func kelvin() -> Self](./hkunit/kelvin%28%29.md)
  Returns a HealthKit unit for measuring temperature in kelvins.
### Constructing hearing sensitivity units
- [class func decibelHearingLevel() -> Self](./hkunit/decibelhearinglevel%28%29.md)
  Returns a HealthKit unit for measuring the intensity of a sound.
### Constructing frequency units
- [class func hertz() -> Self](./hkunit/hertz%28%29.md)
  Returns a HealthKit unit for measuring frequency in hertz.
- [class func hertzUnit(with: HKMetricPrefix) -> Self](./hkunit/hertzunit%28with%29.md)
  Returns a HealthKit unit for measuring frequency in hertz with the provided prefix.
### Constructing vision units
- [class func diopter() -> Self](./hkunit/diopter%28%29.md)
  Returns a HealthKit unit for measuring the optical power of a lens using diopter units.
- [class func prismDiopter() -> Self](./hkunit/prismdiopter%28%29.md)
  Returns a HealthKit unit for measuring the prismatic deviation of a lens using prism diopter units.
### Constructing angle units
- [class func degreeAngle() -> Self](./hkunit/degreeangle%28%29.md)
  Returns a HealthKit unit for measuring angles using degrees.
- [class func radianAngle() -> Self](./hkunit/radianangle%28%29.md)
  Returns a HealthKit unit for measuring angles using radians.
- [class func radianAngleUnit(with: HKMetricPrefix) -> Self](./hkunit/radianangleunit%28with%29.md)
  Returns a HealthKit unit for measuring angles, using radian units with the provided prefix.
### Constructing electrical conductance units
- [class func siemen() -> Self](./hkunit/siemen%28%29.md)
  Returns a HealthKit unit for measuring electrical conductance in siemens.
- [class func siemenUnit(with: HKMetricPrefix) -> Self](./hkunit/siemenunit%28with%29.md)
  Returns a HealthKit unit for measuring electrical conductance, using siemen units with the provided prefix.
### Electrical potential difference
- [class func volt() -> Self](./hkunit/volt%28%29.md)
  Returns a HealthKit unit for measuring the difference in electrical potential using volts.
- [class func voltUnit(with: HKMetricPrefix) -> Self](./hkunit/voltunit%28with%29.md)
  Returns a HealthKit unit for measuring the electrical potential difference in volts with the provided prefix.
### Constructing pharmacology units
- [class func internationalUnit() -> Self](./hkunit/internationalunit%28%29.md)
  Returns a HealthKit unit that measures the amount of a biologically active substance in international units (IU).
### Constructing scalar units
- [class func count() -> Self](./hkunit/count%28%29.md)
  Returns a HealthKit unit for measuring counts.
- [class func percent() -> Self](./hkunit/percent%28%29.md)
  Returns a HealthKit unit for measuring percentages.
### Performing unit math
- [func unitMultiplied(by: HKUnit) -> HKUnit](./hkunit/unitmultiplied%28by%29.md)
  Creates a complex unit by multiplying the receiving unit with another unit.
- [func unitDivided(by: HKUnit) -> HKUnit](./hkunit/unitdivided%28by%29.md)
  Creates a complex unit by dividing the receiving unit by another unit.
- [func unitRaised(toPower: Int) -> HKUnit](./hkunit/unitraised%28topower%29.md)
  Creates a complex unit by raising the unit to the given power.
- [func reciprocal() -> HKUnit](./hkunit/reciprocal%28%29.md)
  Returns a complex unit representing the unit’s reciprocal.
### Constants
- [enum HKMetricPrefix](./hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.
### Initializers
- [init?(coder: NSCoder)](./hkunit/init%28coder%29.md)
- [convenience init(fromEnergyFormatterUnit: EnergyFormatter.Unit)](./hkunit/init%28fromenergyformatterunit%29.md)
- [convenience init(fromLengthFormatterUnit: LengthFormatter.Unit)](./hkunit/init%28fromlengthformatterunit%29.md)
- [convenience init(fromMassFormatterUnit: MassFormatter.Unit)](./hkunit/init%28frommassformatterunit%29.md)
- [convenience init(fromString: String)](./hkunit/init%28fromstring%29.md)
### Type Methods
- [class func appleEffortScore() -> Self](./hkunit/appleeffortscore%28%29.md)
- [class func lux() -> Self](./hkunit/lux%28%29.md)
  Returns a HealthKit unit for measuring illuminance in lux.
- [class func luxUnit(with: HKMetricPrefix) -> Self](./hkunit/luxunit%28with%29.md)
  Returns a HealthKit unit for measuring illuminance, using lux units with the provided prefix.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Units and quantities
- [Defining and converting units and quantities](./defining-and-converting-units-and-quantities.md)
  Create and convert units and quantities.
- [class HKQuantity](./hkquantity.md)
  An object that stores a value for a given unit.
- [enum HKMetricPrefix](./hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit)*