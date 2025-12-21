# UnitPressure

**Framework**: Foundation  
**Kind**: class

A unit of measure for pressure.

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
class UnitPressure
```

#### Overview

You typically use instances of [`UnitPressure`](unitpressure.md) to represent specific quantities of pressure using the [`NSMeasurement`](nsmeasurement.md) class.

##### Pressure

Pressure is the normal force over a surface. The SI unit for pressure is the pascal (Pa), which is derived as one newton of force over one square meter (`1 Pa = 1 N / 1 m`2).

The [`UnitPressure`](unitpressure.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`newtonsPerMetersSquared`](unitpressure/newtonspermeterssquared.md) and provides the following units, which [`UnitConverterLinear`](unitconverterlinear.md) converters initialize with the given coefficients:

| Name | Method | Symbol | Definition |
| --- | --- | --- | --- |
| Newtons Per Meter Squared (Equivalent to Pascals) | [`newtonsPerMetersSquared`](unitpressure/newtonspermeterssquared.md) | N/m² | `1.0` |
| Gigapascals | [`gigapascals`](unitpressure/gigapascals.md) | GPa | `1e9` |
| Megapascals | [`megapascals`](unitpressure/megapascals.md) | MPa | `1000000.0` |
| Kilopascals | [`kilopascals`](unitpressure/kilopascals.md) | kPa | `1000.0` |
| Hectopascals | [`hectopascals`](unitpressure/hectopascals.md) | hPa | `100.0` |
| Inches of Mercury | [`inchesOfMercury`](unitpressure/inchesofmercury.md) | inHg | `3386.39` |
| Bars | [`bars`](unitpressure/bars.md) | bar | `100000` |
| Millibars | [`millibars`](unitpressure/millibars.md) | mbar | `100` |
| Millimeters of Mercury | [`millimetersOfMercury`](unitpressure/millimetersofmercury.md) | mmHg | `133.322` |
| Pounds Per Square Inch | [`poundsForcePerSquareInch`](unitpressure/poundsforcepersquareinch.md) | psi | `6894.76` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var gigapascals: UnitPressure](unitpressure/gigapascals.md)
  The gigapascals unit of pressure.
- [class var megapascals: UnitPressure](unitpressure/megapascals.md)
  The megapascals unit of pressure.
- [class var kilopascals: UnitPressure](unitpressure/kilopascals.md)
  The kilopascals unit of pressure.
- [class var hectopascals: UnitPressure](unitpressure/hectopascals.md)
  The hectopascals unit of pressure.
- [class var inchesOfMercury: UnitPressure](unitpressure/inchesofmercury.md)
  The inches of mercury unit of pressure.
- [class var bars: UnitPressure](unitpressure/bars.md)
  The bars unit of pressure.
- [class var millibars: UnitPressure](unitpressure/millibars.md)
  The millibars unit of pressure.
- [class var millimetersOfMercury: UnitPressure](unitpressure/millimetersofmercury.md)
  The millimeters of mercury unit of pressure.
- [class var newtonsPerMetersSquared: UnitPressure](unitpressure/newtonspermeterssquared.md)
  The newtons per square meter unit of pressure.
- [class var poundsForcePerSquareInch: UnitPressure](unitpressure/poundsforcepersquareinch.md)
  The pounds per square inch unit of pressure.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitPressure>)](unitpressure/init(forlocale:usage:).md)
  Creates a `UnitPressure` which the specified `locale` prefers for the specific `usage`.

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

- [class UnitMass](unitmass.md)
  A unit of measure for mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitpressure)*