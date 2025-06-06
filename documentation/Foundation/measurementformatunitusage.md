# MeasurementFormatUnitUsage

**Framework**: Foundation  
**Kind**: struct

A type that provides the generalized usage for a formatted measurement.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct MeasurementFormatUnitUsage<UnitType> where UnitType : Dimension
```

## Topics

### Selecting a General Format for a Measurement Unit
- [static var general: MeasurementFormatUnitUsage<UnitType>](measurementformatunitusage/general.md)
  A general usage of the formatted measurement.
- [static var asProvided: MeasurementFormatUnitUsage<UnitType>](measurementformatunitusage/asprovided.md)
  A usage of the formatted measurement that reflects the units that you used to create the measurement.
### Selecting a Format for an Energy Measurement
- [static var food: MeasurementFormatUnitUsage<UnitEnergy>](measurementformatunitusage/food.md)
  A usage of an energy measurement related to food.
- [static var workout: MeasurementFormatUnitUsage<UnitEnergy>](measurementformatunitusage/workout.md)
  A usage of a energy measurement related to a workout.
### Selecting a Format for a Length Measurement
- [static var person: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/person-8bfxd.md)
  A format usage of a length measurement for displaying a distance as it relates to people.
- [static var personHeight: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/personheight.md)
  A usage of a length measurement related to a person’s height.
- [static var road: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/road.md)
  A usage of a length measurement related to a road.
### Selecting a Format for a Mass Measurement
- [static var personWeight: MeasurementFormatUnitUsage<UnitMass>](measurementformatunitusage/personweight.md)
  A usage of a mass measurement related to a person’s weight.
### Selecting a Format for a Temperature Measurement
- [static var person: MeasurementFormatUnitUsage<UnitTemperature>](measurementformatunitusage/person-4ifk7.md)
  A format usage of a temperature measurement for displaying a temperature as it relates to people.
- [static var weather: MeasurementFormatUnitUsage<UnitTemperature>](measurementformatunitusage/weather.md)
  A usage of a temperature measurement related to the weather.
### Type Properties
- [static var barometric: MeasurementFormatUnitUsage<UnitPressure>](measurementformatunitusage/barometric.md)
- [static var focalLength: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/focallength.md)
- [static var liquid: MeasurementFormatUnitUsage<UnitVolume>](measurementformatunitusage/liquid.md)
- [static var rainfall: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/rainfall.md)
- [static var snowfall: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/snowfall.md)
- [static var visibility: MeasurementFormatUnitUsage<UnitLength>](measurementformatunitusage/visibility.md)
- [static var wind: MeasurementFormatUnitUsage<UnitSpeed>](measurementformatunitusage/wind.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatunitusage)*