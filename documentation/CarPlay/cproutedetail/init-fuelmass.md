# init(fuelMass:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for fuel mass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(fuelMass: Measurement<UnitMass>)
```

#### Return Value

A new @c CPRouteDetail instance representing the fuel mass

#### Discussion

Use this method to display fuel levels for vehicles that measure fuel by mass, such as compressed natural gas (CNG) vehicles.

CNG and similar compressed gas systems often measure fuel in mass units rather than volume due to the variable density under pressure. The system formats the mass measurement according to the user’s preferred units.

## Parameters

- `fuelMass`: A measurement representing the fuel mass using @c NSUnitMass. Common units: - @c NSUnitMass.kilograms for compressed natural gas
- @c NSUnitMass.pounds for CNG in regions using imperial units


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(fuelmass:))*