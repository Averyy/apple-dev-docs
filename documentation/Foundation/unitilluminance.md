# UnitIlluminance

**Framework**: Foundation  
**Kind**: class

A unit of measure for illuminance.

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
class UnitIlluminance
```

#### Overview

You typically use instances of [`UnitIlluminance`](unitilluminance.md) to represent specific quantities of illuminance using the [`NSMeasurement`](nsmeasurement.md) class.

##### Illuminance

Illuminance is the luminous flux incident on a surface. The SI unit for illuminance is the lux (lx), which is derived as one lumen per square meter (1lm / 1m2).

The [`UnitIlluminance`](unitilluminance.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`lux`](unitilluminance/lux.md).

| Name | Method | Symbol |
| --- | --- | --- |
| Lux | [`lux`](unitilluminance/lux.md) | lx |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accesing Predefined Units
- [class var lux: UnitIlluminance](unitilluminance/lux.md)
  The lux unit of illuminance.

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

- [class UnitEnergy](unitenergy.md)
  A unit of measure for energy.
- [class UnitPower](unitpower.md)
  A unit of measure for power.
- [class UnitTemperature](unittemperature.md)
  A unit of measure for temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitilluminance)*