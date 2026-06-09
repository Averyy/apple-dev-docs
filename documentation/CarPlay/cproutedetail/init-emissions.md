# init(emissions:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for emissions data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(emissions: Measurement<UnitMass>)
```

#### Return Value

A new @c CPRouteDetail instance representing emissions

#### Discussion

Use this method to display estimated emissions for the route. This differs from carbon footprint by potentially including other pollutants beyond CO₂, or representing total emissions using different measurement approaches.

This method provides flexibility for apps that want to display emissions data differently than the standard carbon footprint calculation. Use cases include displaying other greenhouse gases (methane, nitrous oxide), air pollutants (NOx, particulate matter), or alternative carbon accounting methodologies. Unlike @c carbonFootprint, this method does not automatically append “CO₂” to the display value, giving you control over how emissions are labeled.

> **Note**: Consider using @c routeDetailWithCarbonFootprint: for standard CO₂ measurements, as it provides optimized formatting with the CO₂ label. Reserve this method for comprehensive emissions reporting or alternative pollutant measurements where the generic “emissions” label is more appropriate.

## Parameters

- `emissions`: A measurement of emissions using @c NSUnitMass. The system formats with appropriate units and precision. Common units include: - @c NSUnitMass.grams for small emissions quantities
- @c NSUnitMass.kilograms for standard emissions display
- @c NSUnitMass.milligrams for particulate matter or trace pollutants


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(emissions:))*