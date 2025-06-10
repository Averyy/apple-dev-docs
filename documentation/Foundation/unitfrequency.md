# UnitFrequency

**Framework**: Foundation  
**Kind**: class

A unit of measure for frequency.

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
class UnitFrequency
```

#### Overview

You typically use instances of [`UnitFrequency`](unitfrequency.md) to represent specific quantities of frequency using the [`NSMeasurement`](nsmeasurement.md) class.

##### Frequency

Frequency is a quantity of occurrences for a repeating event over time. The SI unit for frequency is the hertz (Hz), which is a derived as one occurrence per second (`1 Hz = 1 / 1s`).

The [`UnitFrequency`](unitfrequency.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`hertz`](unitfrequency/hertz.md), and provides the following units, which are initialized using [`UnitConverterLinear`](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
| --- | --- | --- | --- |
| Terahertz | [`terahertz`](unitfrequency/terahertz.md) | THz | `1e12` |
| Gigahertz | [`gigahertz`](unitfrequency/gigahertz.md) | GHz | `1e9` |
| Megahertz | [`megahertz`](unitfrequency/megahertz.md) | MHz | `1000000.0` |
| Kilohertz | [`kilohertz`](unitfrequency/kilohertz.md) | kHz | `1000.0` |
| Hertz | [`hertz`](unitfrequency/hertz.md) | Hz | `1` |
| Millihertz | [`millihertz`](unitfrequency/millihertz.md) | mHz | `0.001` |
| Microhertz | [`microhertz`](unitfrequency/microhertz.md) | µHz | `0.000001` |
| Nanohertz | [`nanohertz`](unitfrequency/nanohertz.md) | nHz | `1e-9` |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var terahertz: UnitFrequency](unitfrequency/terahertz.md)
  The terahertz unit of frequency.
- [class var gigahertz: UnitFrequency](unitfrequency/gigahertz.md)
  The gigahertz unit of frequency.
- [class var megahertz: UnitFrequency](unitfrequency/megahertz.md)
  The megahertz unit of frequency.
- [class var kilohertz: UnitFrequency](unitfrequency/kilohertz.md)
  The kilohertz unit of frequency.
- [class var hertz: UnitFrequency](unitfrequency/hertz.md)
  The hertz unit of frequency.
- [class var millihertz: UnitFrequency](unitfrequency/millihertz.md)
  The millihertz unit of frequency.
- [class var microhertz: UnitFrequency](unitfrequency/microhertz.md)
  The microhertz unit of frequency.
- [class var nanohertz: UnitFrequency](unitfrequency/nanohertz.md)
  The nanohertz unit of frequency.
- [class var framesPerSecond: UnitFrequency](unitfrequency/framespersecond.md)
  The frames per second unit of frequency.

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

- [class UnitAcceleration](unitacceleration.md)
  A unit of measure for acceleration.
- [class UnitDuration](unitduration.md)
  A unit of measure for a duration of time.
- [class UnitSpeed](unitspeed.md)
  A unit of measure for speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitfrequency)*