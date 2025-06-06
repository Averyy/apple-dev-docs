# UnitSpeed

**Framework**: Foundation  
**Kind**: class

A unit of measure for speed.

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
class UnitSpeed
```

#### Overview

You typically use instances of [`UnitSpeed`](unitspeed.md) to represent specific quantities of speed using the [`NSMeasurement`](nsmeasurement.md) class.

##### Speed

Speed is the magnitude of velocity, or the rate of change of position. Speed can be expressed by SI derived units in terms of meters per second (m/s), and is also commonly expressed in terms of kilometers per hour (km/h) and miles per hour (mph).

The [`UnitSpeed`](unitspeed.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`metersPerSecond`](unitspeed/meterspersecond.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Meters Per Second | [`metersPerSecond`](unitspeed/meterspersecond.md) | m/s | `1.0` |
| Kilometers Per Hour | [`kilometersPerHour`](unitspeed/kilometersperhour.md) | km/h | `0.277778` |
| Miles Per Hour | [`milesPerHour`](unitspeed/milesperhour.md) | mph | `0.44704` |
| Knots | [`knots`](unitspeed/knots.md) | kn | `0.514444` |

The base unit is [`metersPerSecond`](unitspeed/meterspersecond.md) and is accessed via [`baseUnit()`](dimension/baseunit().md) on the [`Dimension`](dimension.md) protocol.

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var metersPerSecond: UnitSpeed](unitspeed/meterspersecond.md)
  The meter per second unit of speed.
- [class var kilometersPerHour: UnitSpeed](unitspeed/kilometersperhour.md)
  The kilometers per hour unit of speed.
- [class var milesPerHour: UnitSpeed](unitspeed/milesperhour.md)
  The miles per hour unit of speed.
- [class var knots: UnitSpeed](unitspeed/knots.md)
  The knots unit of speed.
### Initializers
- [convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitSpeed>)](unitspeed/init(forlocale:usage:).md)

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

- [class UnitAcceleration](unitacceleration.md)
  A unit of measure for acceleration.
- [class UnitDuration](unitduration.md)
  A unit of measure for a duration of time.
- [class UnitFrequency](unitfrequency.md)
  A unit of measure for frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitspeed)*