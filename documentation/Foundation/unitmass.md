# UnitMass

**Framework**: Foundation  
**Kind**: class

A unit of measure for mass.

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
class UnitMass
```

#### Overview

You typically use instances of [`UnitMass`](unitmass.md) to represent specific quantities of mass using the [`NSMeasurement`](nsmeasurement.md) class.

##### Mass

Mass is a fundamental property of matter that causes it to resist a force accelerating it. The SI unit for mass is the kilogram (kg), which defined in terms of the mass of the international prototype kilogram.

The [`UnitMass`](unitmass.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`kilograms`](unitmass/kilograms.md), and provides the following units, which [`UnitConverterLinear`](unitconverterlinear.md) converters initialize with the given coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Kilograms | [`kilograms`](unitmass/kilograms.md) | kg | `1.0` |
| Grams | [`grams`](unitmass/grams.md) | g | `0.001` |
| Decigrams | [`decigrams`](unitmass/decigrams.md) | dg | `0.0001` |
| Centigrams | [`centigrams`](unitmass/centigrams.md) | cg | `0.00001` |
| Milligrams | [`milligrams`](unitmass/milligrams.md) | mg | `0.000001` |
| Micrograms | [`micrograms`](unitmass/micrograms.md) | µg | `1e-9` |
| Nanograms | [`nanograms`](unitmass/nanograms.md) | ng | `1e-12` |
| Picograms | [`picograms`](unitmass/picograms.md) | pg | `1e-15` |
| Ounces | [`ounces`](unitmass/ounces.md) | oz | `0.0283495` |
| Pounds | [`pounds`](unitmass/pounds.md) | lb | `0.453592` |
| Stones | [`stones`](unitmass/stones.md) | st | `0.157473` |
| Metric Tons | [`metricTons`](unitmass/metrictons.md) | t | `1000` |
| Short Tons | [`shortTons`](unitmass/shorttons.md) | ton | `907.185` |
| Carats | [`carats`](unitmass/carats.md) | ct | `0.0002` |
| Ounces Troy | [`ouncesTroy`](unitmass/ouncestroy.md) | oz t | `0.03110348` |
| Slugs | [`slugs`](unitmass/slugs.md) | slug | `14.5939` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var kilograms: UnitMass](unitmass/kilograms.md)
  The kilograms unit of mass.
- [class var grams: UnitMass](unitmass/grams.md)
  The grams unit of mass.
- [class var decigrams: UnitMass](unitmass/decigrams.md)
  The decigrams unit of mass.
- [class var centigrams: UnitMass](unitmass/centigrams.md)
  The centigrams unit of mass.
- [class var milligrams: UnitMass](unitmass/milligrams.md)
  The milligrams unit of mass.
- [class var micrograms: UnitMass](unitmass/micrograms.md)
  The micrograms unit of mass.
- [class var nanograms: UnitMass](unitmass/nanograms.md)
  The nanograms unit of mass.
- [class var picograms: UnitMass](unitmass/picograms.md)
  The picograms unit of mass.
- [class var ounces: UnitMass](unitmass/ounces.md)
  The ounces unit of mass.
- [pounds](1808594-pounds.md)
  Returns the pounds unit of mass.
- [class var pounds: UnitMass](unitmass/pounds.md)
  The pounds unit of mass.
- [class var stones: UnitMass](unitmass/stones.md)
  The stone unit of mass.
- [class var metricTons: UnitMass](unitmass/metrictons.md)
  The metric tons unit of mass.
- [class var shortTons: UnitMass](unitmass/shorttons.md)
  The short tons unit of mass.
- [class var carats: UnitMass](unitmass/carats.md)
  The carats unit of mass.
- [class var ouncesTroy: UnitMass](unitmass/ouncestroy.md)
  The ounces troy unit of mass.
- [class var slugs: UnitMass](unitmass/slugs.md)
  The slugs unit of mass.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitMass>)](unitmass/init(forlocale:usage:).md)

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

- [class UnitPressure](unitpressure.md)
  A unit of measure for pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitmass)*