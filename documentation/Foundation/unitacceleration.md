# UnitAcceleration

**Framework**: Foundation  
**Kind**: class

A unit of measure for acceleration.

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
class UnitAcceleration
```

#### Overview

You typically use instances of [`UnitAcceleration`](unitacceleration.md) to represent specific quantities of acceleration using the [`NSMeasurement`](nsmeasurement.md) class.

##### Acceleration

Acceleration is the rate of change of velocity. Acceleration can be expressed by SI derived units in terms of meters per second squared (m/s2).

The [`UnitAcceleration`](unitacceleration.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`metersPerSecondSquared`](unitacceleration/meterspersecondsquared.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Meters Per Second Squared | [`metersPerSecondSquared`](unitacceleration/meterspersecondsquared.md) | m/s² | `1.0` |
| Gravity | [`gravity`](unitacceleration/gravity.md) | g | `9.81` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var metersPerSecondSquared: UnitAcceleration](unitacceleration/meterspersecondsquared.md)
  Returns the meter per second squared unit of acceleration.
- [class var gravity: UnitAcceleration](unitacceleration/gravity.md)
  Returns the gravity unit of acceleration.

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

- [class UnitDuration](unitduration.md)
  A unit of measure for a duration of time.
- [class UnitFrequency](unitfrequency.md)
  A unit of measure for frequency.
- [class UnitSpeed](unitspeed.md)
  A unit of measure for speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitacceleration)*