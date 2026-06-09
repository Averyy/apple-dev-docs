# init(fuelEnergy:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for fuel energy content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(fuelEnergy: Measurement<UnitEnergy>)
```

#### Return Value

A new @c CPRouteDetail instance representing the fuel energy

#### Discussion

Use this method to display fuel levels for hydrogen fuel cell vehicles or other vehicles where fuel is measured in energy units rather than volume or mass.

Hydrogen fuel cell vehicles often express fuel capacity in kilowatt-hours of energy content. The system formats this appropriately for user display.

> **Note**: This method is distinct from battery energy (@c routeDetailWithKilowattHours:) and should be used specifically for fuel-based energy storage systems.

## Parameters

- `fuelEnergy`: A measurement representing the fuel energy using @c NSUnitEnergy. Common units: - @c NSUnitEnergy.kilowattHours for hydrogen fuel cells
- @c NSUnitEnergy.megajoules for alternative energy measurements


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(fuelenergy:))*