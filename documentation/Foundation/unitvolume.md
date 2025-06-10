# UnitVolume

**Framework**: Foundation  
**Kind**: class

A unit of measure for volume.

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
class UnitVolume
```

#### Overview

You typically use instances of [`UnitVolume`](unitvolume.md) to represent specific quantities of volume using the [`NSMeasurement`](nsmeasurement.md) class.

##### Volume

Volume is a quantity of the extend of matter in three dimensions. The SI accepted unit of volume is the liter (L), which is derived as one cubic decimeter (1 dm3). Volume is also commonly expressed in terms of cubic meters (m3), gallons (gal), and cups (cup).

The [`UnitVolume`](unitvolume.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`liters`](unitvolume/liters.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Megaliters | [`megaliters`](unitvolume/megaliters.md) | ML | `1000000.0` |
| Kiloliters | [`kiloliters`](unitvolume/kiloliters.md) | kL | `1000.0` |
| Liters | [`liters`](unitvolume/liters.md) | L | `1.0` |
| Deciliters | [`deciliters`](unitvolume/deciliters.md) | dL | `0.1` |
| Centiliters | [`centiliters`](unitvolume/centiliters.md) | cL | `0.01` |
| Milliliters | [`milliliters`](unitvolume/milliliters.md) | mL | `0.001` |
| Cubic Kilometers | [`cubicKilometers`](unitvolume/cubickilometers.md) | km³ | `1e12` |
| Cubic Meters | [`cubicMeters`](unitvolume/cubicmeters.md) | m³ | `1000.0` |
| Cubic Decimeters | [`cubicDecimeters`](unitvolume/cubicdecimeters.md) | dm³ | `1.0` |
| Cubic Millimeters | [`cubicMillimeters`](unitvolume/cubicmillimeters.md) | mm³ | `0.000001` |
| Cubic Inches | [`cubicInches`](unitvolume/cubicinches.md) | in³ | `0.0163871` |
| Cubic Feet | [`cubicFeet`](unitvolume/cubicfeet.md) | ft³ | `28.3168` |
| Cubic Yards | [`cubicYards`](unitvolume/cubicyards.md) | yd³ | `764.555` |
| Cubic Miles | [`cubicMiles`](unitvolume/cubicmiles.md) | mi³ | `4.168e+12` |
| Acre Foeet | [`acreFeet`](unitvolume/acrefeet.md) | af | `1.233e+6` |
| Bushels | [`bushels`](unitvolume/bushels.md) | bsh | `35.2391` |
| Teaspoons | [`teaspoons`](unitvolume/teaspoons.md) | tsp | `0.00492892` |
| Tablespoons | [`tablespoons`](unitvolume/tablespoons.md) | tbsp | `0.0147868` |
| Fluid Ounces | [`fluidOunces`](unitvolume/fluidounces.md) | fl oz | `0.0295735` |
| Cups | [`cups`](unitvolume/cups.md) | cup | `0.24` |
| Pints | [`pints`](unitvolume/pints.md) | pt | `0.473176` |
| Quarts | [`quarts`](unitvolume/quarts.md) | qt | `0.946353` |
| Gallons | [`gallons`](unitvolume/gallons.md) | gal | `3.78541` |
| Imperial Teaspoons | [`imperialTeaspoons`](unitvolume/imperialteaspoons.md) | tsp | `0.00591939` |
| Imperial Tablespoons | [`imperialTablespoons`](unitvolume/imperialtablespoons.md) | tbsp | `0.0177582` |
| Imperial Fluid Ounces | [`imperialFluidOunces`](unitvolume/imperialfluidounces.md) | fl oz | `0.0284131` |
| Imperial Pints | [`imperialPints`](unitvolume/imperialpints.md) | pt | `0.568261` |
| Imperial Quarts | [`imperialQuarts`](unitvolume/imperialquarts.md) | qt | `1.13652` |
| Imperial Gallons | [`imperialGallons`](unitvolume/imperialgallons.md) | gal | `4.54609` |
| Metric Cups | [`metricCups`](unitvolume/metriccups.md) | metric cup | `0.25` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var megaliters: UnitVolume](unitvolume/megaliters.md)
  The megaliters unit of volume.
- [class var kiloliters: UnitVolume](unitvolume/kiloliters.md)
  The kiloliters unit of volume.
- [class var liters: UnitVolume](unitvolume/liters.md)
  The liters unit of volume.
- [class var deciliters: UnitVolume](unitvolume/deciliters.md)
  The deciliters unit of volume.
- [class var centiliters: UnitVolume](unitvolume/centiliters.md)
  The centiliters unit of volume.
- [class var milliliters: UnitVolume](unitvolume/milliliters.md)
  The milliliters unit of volume.
- [class var cubicKilometers: UnitVolume](unitvolume/cubickilometers.md)
  The cubic kilometers unit of volume.
- [class var cubicMeters: UnitVolume](unitvolume/cubicmeters.md)
  The cubic meters unit of volume.
- [class var cubicDecimeters: UnitVolume](unitvolume/cubicdecimeters.md)
  The cubic decimeters unit of volume.
- [class var cubicCentimeters: UnitVolume](unitvolume/cubiccentimeters.md)
  The cubic centimeters unit of volume.
- [class var cubicMillimeters: UnitVolume](unitvolume/cubicmillimeters.md)
  The cubic millimeters unit of volume.
- [class var cubicInches: UnitVolume](unitvolume/cubicinches.md)
  The cubic inches unit of volume.
- [class var cubicFeet: UnitVolume](unitvolume/cubicfeet.md)
  The cubic feet unit of volume.
- [class var cubicYards: UnitVolume](unitvolume/cubicyards.md)
  The cubic yards unit of volume.
- [class var cubicMiles: UnitVolume](unitvolume/cubicmiles.md)
  The cubic miles unit of volume.
- [class var acreFeet: UnitVolume](unitvolume/acrefeet.md)
  The acre feet unit of volume.
- [class var bushels: UnitVolume](unitvolume/bushels.md)
  The bushels unit of volume.
- [class var teaspoons: UnitVolume](unitvolume/teaspoons.md)
  The teaspoons unit of volume.
- [class var tablespoons: UnitVolume](unitvolume/tablespoons.md)
  The tablespoons unit of volume.
- [class var fluidOunces: UnitVolume](unitvolume/fluidounces.md)
  The fluid ounces unit of volume.
- [class var cups: UnitVolume](unitvolume/cups.md)
  The cups unit of volume.
- [class var pints: UnitVolume](unitvolume/pints.md)
  The pints unit of volume.
- [class var quarts: UnitVolume](unitvolume/quarts.md)
  The quarts unit of volume.
- [class var gallons: UnitVolume](unitvolume/gallons.md)
  The gallons unit of volume.
- [class var imperialTeaspoons: UnitVolume](unitvolume/imperialteaspoons.md)
  The imperial teaspoons unit of volume.
- [class var imperialTablespoons: UnitVolume](unitvolume/imperialtablespoons.md)
  The imperial tablespoons unit of volume.
- [class var imperialFluidOunces: UnitVolume](unitvolume/imperialfluidounces.md)
  The imperial fluid ounces unit of volume.
- [class var imperialPints: UnitVolume](unitvolume/imperialpints.md)
  The imperial pints unit of volume.
- [class var imperialQuarts: UnitVolume](unitvolume/imperialquarts.md)
  The imperial quarts unit of volume.
- [class var imperialGallons: UnitVolume](unitvolume/imperialgallons.md)
  The imperial gallons unit of volume.
- [class var metricCups: UnitVolume](unitvolume/metriccups.md)
  The metric cups unit of volume.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitVolume>)](unitvolume/init(forlocale:usage:).md)

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

- [class UnitArea](unitarea.md)
  A unit of measure for area.
- [class UnitLength](unitlength.md)
  A unit of measure for length.
- [class UnitAngle](unitangle.md)
  A unit of measure for planar angle and rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitvolume)*