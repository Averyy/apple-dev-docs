# init(kilowattHours:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for battery energy in kilowatt-hours.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(kilowattHours: Measurement<UnitEnergy>)
```

#### Return Value

A new @c CPRouteDetail instance representing the battery energy

#### Discussion

Use this method to display battery levels for electric vehicles using absolute energy measurements rather than percentages. This provides more meaningful information for users familiar with their vehicle’s battery capacity.

Displaying battery in kilowatt-hours helps users better understand range and charging needs, particularly for long trips or when comparing vehicles with different battery capacities. A 10% battery in a 100 kWh vehicle (10 kWh) provides very different range than 10% in a 40 kWh vehicle (4 kWh).

> **Note**: Most electric vehicles use kilowatt-hours as the standard unit for battery capacity. The system automatically formats this with the “kWh” abbreviation.

## Parameters

- `kilowattHours`: A measurement of battery energy using @c NSUnitEnergy.kilowattHours


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(kilowatthours:))*