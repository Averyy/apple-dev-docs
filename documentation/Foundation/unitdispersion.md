# UnitDispersion

**Framework**: Foundation  
**Kind**: class

A unit of measure for specific quantities of dispersion.

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
class UnitDispersion
```

#### Overview

You typically use instances of [`UnitDispersion`](unitdispersion.md) to represent specific quantities of dispersion using the [`NSMeasurement`](nsmeasurement.md) class.

##### Dispersion

Dispersion describes the amount of a constituent divided by the amount of all other constituents in a mixture. Dispersion is a dimensionless quantity that is commonly expressed in “parts-per” notation, such as “parts per million” (ppm), to describe small relative quantities.

The [`UnitDispersion`](unitdispersion.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`partsPerMillion`](unitdispersion/partspermillion.md).

| Name | Method | Abbreviation |
| --- | --- | --- |
| Parts Per Million | [`partsPerMillion`](unitdispersion/partspermillion.md) | ppm |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var partsPerMillion: UnitDispersion](unitdispersion/partspermillion.md)
  The parts per million unit.

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

- [class UnitConcentrationMass](unitconcentrationmass.md)
  A unit of measure for concentration of mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitdispersion)*