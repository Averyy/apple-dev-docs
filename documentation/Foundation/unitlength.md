# UnitLength

**Framework**: Foundation  
**Kind**: class

A unit of measure for length.

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
class UnitLength
```

#### Overview

You typically use instances of [`UnitLength`](unitlength.md) to represent specific quantities of length using the [`NSMeasurement`](nsmeasurement.md) class.

##### Length

Length is the dimensional extent of matter. The SI unit for length is the meter (m), which is defined in terms of the distance traveled by light in a vacuum.

The [`UnitLength`](unitlength.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`meters`](unitlength/meters.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Megameters | [`megameters`](unitlength/megameters.md) | Mm | `1000000.0` |
| Kilometers | [`kilometers`](unitlength/kilometers.md) | kM | `1000.0` |
| Hectometers | [`hectometers`](unitlength/hectometers.md) | hm | `100.0` |
| Decameters | [`decameters`](unitlength/decameters.md) | dam | `10.0` |
| Meters | [`meters`](unitlength/meters.md) | m | `1.0` |
| Decimeters | [`decimeters`](unitlength/decimeters.md) | dm | `0.1` |
| Centimeters | [`centimeters`](unitlength/centimeters.md) | cm | `0.01` |
| Millimeters | [`millimeters`](unitlength/millimeters.md) | mm | `0.001` |
| Micrometers | [`micrometers`](unitlength/micrometers.md) | µm | `0.000001` |
| Nanometers | [`nanometers`](unitlength/nanometers.md) | nm | `1e-9` |
| Picometers | [`picometers`](unitlength/picometers.md) | pm | `1e-12` |
| Inches | [`inches`](unitlength/inches.md) | in | `0.0254` |
| Feet | [`feet`](unitlength/feet.md) | ft | `0.3048` |
| Yards | [`yards`](unitlength/yards.md) | yd | `0.9144` |
| Miles | [`miles`](unitlength/miles.md) | mi | `1609.34` |
| Scandinavian Miles | [`scandinavianMiles`](unitlength/scandinavianmiles.md) | smi | `10000` |
| Light Years | [`lightyears`](unitlength/lightyears.md) | ly | `9.461e+15` |
| Nautical Miles | [`nauticalMiles`](unitlength/nauticalmiles.md) | NM | `1852` |
| Fathoms | [`fathoms`](unitlength/fathoms.md) | ftm | `1.8288` |
| Furlongs | [`furlongs`](unitlength/furlongs.md) | fur | `201.168` |
| Astronomical Units | [`astronomicalUnits`](unitlength/astronomicalunits.md) | ua | `1.496e+11` |
| Parsecs | [`parsecs`](unitlength/parsecs.md) | pc | `3.086e+16` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var megameters: UnitLength](unitlength/megameters.md)
  The megameters unit of length.
- [class var kilometers: UnitLength](unitlength/kilometers.md)
  The kilometers unit of length.
- [class var hectometers: UnitLength](unitlength/hectometers.md)
  The hectometers unit of length.
- [class var decameters: UnitLength](unitlength/decameters.md)
  The decameters unit of length.
- [class var meters: UnitLength](unitlength/meters.md)
  The meters unit of length.
- [class var decimeters: UnitLength](unitlength/decimeters.md)
  The decimeters unit of length.
- [class var centimeters: UnitLength](unitlength/centimeters.md)
  The centimeters unit of length.
- [class var millimeters: UnitLength](unitlength/millimeters.md)
  The millimeters unit of length.
- [class var micrometers: UnitLength](unitlength/micrometers.md)
  The micrometers unit of length.
- [class var nanometers: UnitLength](unitlength/nanometers.md)
  The nanometers unit of length.
- [class var picometers: UnitLength](unitlength/picometers.md)
  The picometers unit of length.
- [class var inches: UnitLength](unitlength/inches.md)
  The inches unit of length.
- [class var feet: UnitLength](unitlength/feet.md)
  The feet unit of length.
- [class var yards: UnitLength](unitlength/yards.md)
  The yards unit of length.
- [class var miles: UnitLength](unitlength/miles.md)
  The miles unit of length.
- [class var scandinavianMiles: UnitLength](unitlength/scandinavianmiles.md)
  The Scandinavian miles unit of length.
- [class var lightyears: UnitLength](unitlength/lightyears.md)
  The light years unit of length.
- [class var nauticalMiles: UnitLength](unitlength/nauticalmiles.md)
  The nautical miles unit of length.
- [class var fathoms: UnitLength](unitlength/fathoms.md)
  The fathoms unit of length.
- [class var furlongs: UnitLength](unitlength/furlongs.md)
  The furlongs unit of length.
- [class var astronomicalUnits: UnitLength](unitlength/astronomicalunits.md)
  The astronomical units unit of length.
- [class var parsecs: UnitLength](unitlength/parsecs.md)
  The parsecs unit of length.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitLength>)](unitlength/init(forlocale:usage:).md)

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
- [class UnitVolume](unitvolume.md)
  A unit of measure for volume.
- [class UnitAngle](unitangle.md)
  A unit of measure for planar angle and rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitlength)*