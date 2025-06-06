# UnitFuelEfficiency

**Framework**: Foundation  
**Kind**: class

A unit of measure for fuel efficiency.

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
class UnitFuelEfficiency
```

#### Overview

You typically use instances of [`UnitFuelEfficiency`](unitfuelefficiency.md) to represent specific quantities of fuel efficiency using the [`NSMeasurement`](nsmeasurement.md) class.

##### Fuel Efficiency

Fuel efficiency corresponds to the thermal efficiency of a process that converts the chemical potential energy of a fuel into kinetic energy. Fuel efficiency can be expressed by SI derived units in terms of cubic meters per meter (m3/m), but is more commonly expressed in terms of liters per kilometer (L/km) and miles per gallon (mpg).

The [`UnitFuelEfficiency`](unitfuelefficiency.md) class defines its [`baseUnit()`](dimension/baseunit().md) as [`litersPer100Kilometers`](unitfuelefficiency/litersper100kilometers.md), and provides the following units:

| Name | Method | Symbol |
| --- | --- | --- |
| Liters Per 100 Kilometers | [`litersPer100Kilometers`](unitfuelefficiency/litersper100kilometers.md) | L/100km |
| Miles Per Gallon | [`milesPerGallon`](unitfuelefficiency/milespergallon.md) | mpg |
| Miles Per Imperial Gallon | [`milesPerImperialGallon`](unitfuelefficiency/milesperimperialgallon.md) | mpg |

## Topics

### Accessing the Base Unit
- [class func baseUnit() -> Self](dimension/baseunit.md)
  Returns the base unit.
### Accessing Predefined Units
- [class var milesPerImperialGallon: UnitFuelEfficiency](unitfuelefficiency/milesperimperialgallon.md)
  The miles per imperial gallon unit of fuel efficiency.
- [class var litersPer100Kilometers: UnitFuelEfficiency](unitfuelefficiency/litersper100kilometers.md)
  The liters per 100 kilometers unit of fuel efficiency.
- [class var milesPerGallon: UnitFuelEfficiency](unitfuelefficiency/milespergallon.md)
  The miles per gallon unit of fuel efficiency.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitfuelefficiency)*