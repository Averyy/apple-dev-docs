# UnitAngle

**Framework**: Foundation  
**Kind**: class

A unit of measure for planar angle and rotation.

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
class UnitAngle
```

#### Overview

You typically use instances of [`UnitAngle`](unitangle.md) to represent specific quantities of planar angle using the [`NSMeasurement`](nsmeasurement.md) class.

##### Angle

Angle is a quantity of rotation. The SI unit for angle is the radian (rad), which is dimensionless and defined to be the angle subtended by an arc that is equal in length to the radius of a circle. Angle is also commonly expressed in terms of degrees (°) and revolutions (rev).

The [`UnitAngle`](unitangle.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`degrees`](unitangle/degrees.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Definition |
| --- | --- | --- | --- |
| Degrees | [`degrees`](unitangle/degrees.md) | ° | `1.0` |
| Arc Minutes | [`arcMinutes`](unitangle/arcminutes.md) | ʹ | `0.016667` |
| Arc Seconds | [`arcSeconds`](unitangle/arcseconds.md) | ʺ | `0.00027778` |
| Radians | [`radians`](unitangle/radians.md) | rad | `57.2958` |
| Gradians | [`gradians`](unitangle/gradians.md) | grad | `0.9` |
| Revolutions | [`revolutions`](unitangle/revolutions.md) | rev | `360` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var degrees: UnitAngle](unitangle/degrees.md)
  The degrees unit of angle.
- [class var arcMinutes: UnitAngle](unitangle/arcminutes.md)
  The arc minutes unit of angle.
- [class var arcSeconds: UnitAngle](unitangle/arcseconds.md)
  The arc seconds unit of angle.
- [class var radians: UnitAngle](unitangle/radians.md)
  The radians unit of angle.
- [class var gradians: UnitAngle](unitangle/gradians.md)
  The gradians unit of angle.
- [class var revolutions: UnitAngle](unitangle/revolutions.md)
  The revolutions unit of angle.

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
- [class UnitVolume](unitvolume.md)
  A unit of measure for volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitangle)*