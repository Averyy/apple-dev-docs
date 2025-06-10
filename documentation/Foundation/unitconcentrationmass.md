# UnitConcentrationMass

**Framework**: Foundation  
**Kind**: class

A unit of measure for concentration of mass.

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
class UnitConcentrationMass
```

#### Overview

You typically use instances of [`UnitConcentrationMass`](unitconcentrationmass.md) to represent specific quantities of concentration using the [`NSMeasurement`](nsmeasurement.md) class.

##### Concentration of Mass

Concentration is the abundance of a constituent within a volume. Concentration can be expressed by SI derived units in terms of kilograms per cubic meter (kg/m3).

The [`UnitConcentrationMass`](unitconcentrationmass.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`gramsPerLiter`](unitconcentrationmass/gramsperliter.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Grams Per Liter | [`gramsPerLiter`](unitconcentrationmass/gramsperliter.md) | g/L | `1` |
| Milligrams Per Deciliter | [`milligramsPerDeciliter`](unitconcentrationmass/milligramsperdeciliter.md) | mg/dL | `0.01` |
| Millimoles Per Liter | [`millimolesPerLiter(withGramsPerMole:)`](unitconcentrationmass/millimolesperliter(withgramspermole:).md) | mmol/L | `18 * gramsPerMole` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var gramsPerLiter: UnitConcentrationMass](unitconcentrationmass/gramsperliter.md)
  The grams per liter unit of concentration.
- [class var milligramsPerDeciliter: UnitConcentrationMass](unitconcentrationmass/milligramsperdeciliter.md)
  The milligrams per deciliter unit of concentration.
- [class func millimolesPerLiter(withGramsPerMole: Double) -> UnitConcentrationMass](unitconcentrationmass/millimolesperliter(withgramspermole:).md)
  Returns the millimoles per liter unit with the specified number of grams per mole.

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

- [class UnitDispersion](unitdispersion.md)
  A unit of measure for specific quantities of dispersion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconcentrationmass)*