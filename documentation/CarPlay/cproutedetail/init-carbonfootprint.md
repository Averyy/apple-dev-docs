# init(carbonFootprint:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for carbon footprint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(carbonFootprint: Measurement<UnitMass>)
```

#### Return Value

A new @c CPRouteDetail instance representing the carbon footprint

#### Discussion

Use this method to display the estimated carbon emissions for the route. This helps environmentally-conscious users evaluate and compare the environmental impact of different route options.

The system formats the measurement with appropriate units and precision. Measurements in grams display with the ‘g’ suffix, while measurements in kilograms use ‘kg’. The measurement is automatically formatted as CO₂ in the UI (e.g., “2.5 kg CO₂”). The system may round values for display clarity.

> **Note**: Apps should calculate carbon footprint based on vehicle type, fuel efficiency, route distance, terrain, and traffic conditions. Electric vehicles may show reduced or zero emissions compared to combustion vehicles, depending on the regional electricity generation mix. Consider providing methodology information in your app’s settings or help documentation.

## Parameters

- `carbonFootprint`: A measurement of carbon emissions using @c NSUnitMass. Typical units include: - @c NSUnitMass.grams for small emissions (e.g., short trips, efficient vehicles)
- @c NSUnitMass.kilograms for larger emissions (e.g., long journeys, less efficient vehicles)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(carbonfootprint:))*