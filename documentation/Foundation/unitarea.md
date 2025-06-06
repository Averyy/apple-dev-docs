# UnitArea

**Framework**: Foundation  
**Kind**: class

A unit of measure for area.

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
class UnitArea
```

#### Overview

You typically use instances of [`UnitArea`](unitarea.md) to represent specific quantities of area using the [`NSMeasurement`](nsmeasurement.md) class.

##### Area

Area is a quantity of extent in two dimensions. Area can be expressed by SI derived units in terms of square meters (m2). Area is also commonly measured in square feet (ft2) and acres (ac).

The [`UnitArea`](unitarea.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`squareMeters`](unitarea/squaremeters.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Square Megameters | [`squareMegameters`](unitarea/squaremegameters.md) | Mm² | `1e12` |
| Square Kilometers | [`squareKilometers`](unitarea/squarekilometers.md) | km² | `1000000.0` |
| Square Meters | [`squareMeters`](unitarea/squaremeters.md) | m² | `1.0` |
| Square Centimeter | [`squareCentimeters`](unitarea/squarecentimeters.md) | cm² | `0.0001` |
| Square Millimeters | [`squareMillimeters`](unitarea/squaremillimeters.md) | mm² | `0.000001` |
| Square Micrometers | [`squareMicrometers`](unitarea/squaremicrometers.md) | µm² | `1e-12` |
| Square Nanometers | [`squareNanometers`](unitarea/squarenanometers.md) | nm² | `1e-18` |
| Square Inches | [`squareInches`](unitarea/squareinches.md) | in² | `0.00064516` |
| Square Feet | [`squareFeet`](unitarea/squarefeet.md) | ft² | `0.092903` |
| Square Yards | [`squareYards`](unitarea/squareyards.md) | yd² | `0.836127` |
| Square Miles | [`squareMiles`](unitarea/squaremiles.md) | mi² | `2.59e+6` |
| Acres | [`acres`](unitarea/acres.md) | ac | `4046.86` |
| Ares | [`ares`](unitarea/ares.md) | a | `100` |
| Hectares | [`hectares`](unitarea/hectares.md) | ha | `10000` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var squareMegameters: UnitArea](unitarea/squaremegameters.md)
  The square megameters unit of area.
- [class var squareKilometers: UnitArea](unitarea/squarekilometers.md)
  The square kilometers unit of area.
- [class var squareMeters: UnitArea](unitarea/squaremeters.md)
  The square meters unit of area.
- [class var squareCentimeters: UnitArea](unitarea/squarecentimeters.md)
  The square centimeters unit of area.
- [class var squareMillimeters: UnitArea](unitarea/squaremillimeters.md)
  The square millimeters unit of area.
- [class var squareMicrometers: UnitArea](unitarea/squaremicrometers.md)
  The square micrometers unit of area.
- [class var squareNanometers: UnitArea](unitarea/squarenanometers.md)
  The square nanometers unit of area.
- [class var squareInches: UnitArea](unitarea/squareinches.md)
  The square inches unit of area.
- [class var squareFeet: UnitArea](unitarea/squarefeet.md)
  The square feet unit of area.
- [class var squareYards: UnitArea](unitarea/squareyards.md)
  The square yards unit of area.
- [class var squareMiles: UnitArea](unitarea/squaremiles.md)
  The square miles unit of area.
- [class var acres: UnitArea](unitarea/acres.md)
  The acres unit of area.
- [class var ares: UnitArea](unitarea/ares.md)
  The ares unit of area.
- [class var hectares: UnitArea](unitarea/hectares.md)
  The hectares unit of area.

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

- [class UnitLength](unitlength.md)
  A unit of measure for length.
- [class UnitVolume](unitvolume.md)
  A unit of measure for volume.
- [class UnitAngle](unitangle.md)
  A unit of measure for planar angle and rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitarea)*