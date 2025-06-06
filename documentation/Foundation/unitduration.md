# UnitDuration

**Framework**: Foundation  
**Kind**: class

A unit of measure for a duration of time.

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
class UnitDuration
```

#### Overview

You typically use instances of [`UnitDuration`](unitduration.md) to represent specific quantities of planar angle using the [`NSMeasurement`](nsmeasurement.md) class.

##### Duration

Duration is a quantity of time. The SI unit for time is the second (sec), which is defined in terms of the radioactivity of a cesium-133 atom. Duration is also commonly expressed in terms of minutes (min) and hours (hr).

> **Note**:  Use the [`NSDateComponents`](nsdatecomponents.md) class to represent quantities of calendrical units, such as days, weeks, months, and years.

The [`UnitDuration`](unitduration.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`seconds`](unitduration/seconds.md), and provides the following units, which [`UnitConverterLinear`](unitconverterlinear.md) converters initialize with the given coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Seconds | [`seconds`](unitduration/seconds.md) | sec | `1` |
| Minutes | [`minutes`](unitduration/minutes.md) | min | `60` |
| Hours | [`hours`](unitduration/hours.md) | hr | `3600` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var hours: UnitDuration](unitduration/hours.md)
  The hour unit of duration.
- [class var minutes: UnitDuration](unitduration/minutes.md)
  The minute unit of duration.
- [class var seconds: UnitDuration](unitduration/seconds.md)
  The second unit of duration.
- [class var milliseconds: UnitDuration](unitduration/milliseconds.md)
  The millisecond unit of duration.
- [class var microseconds: UnitDuration](unitduration/microseconds.md)
  The microsecond unit of duration.
- [class var nanoseconds: UnitDuration](unitduration/nanoseconds.md)
  The nanosecond unit of duration.
- [class var picoseconds: UnitDuration](unitduration/picoseconds.md)
  The picosecond unit of duration.

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
- [class UnitFrequency](unitfrequency.md)
  A unit of measure for frequency.
- [class UnitSpeed](unitspeed.md)
  A unit of measure for speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/unitduration)*