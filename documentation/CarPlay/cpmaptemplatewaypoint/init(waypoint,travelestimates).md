# init(waypoint:travelEstimates:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initializes a new CPMapTemplateWaypoint with the specified waypoint and travel estimates.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(waypoint: CPNavigationWaypoint, travelEstimates: CPTravelEstimates)
```

```objc
- (instancetype) initWithWaypoint:(CPNavigationWaypoint *) waypoint travelEstimates:(CPTravelEstimates *) travelEstimates;
```

#### Return Value

A new CPMapTemplateWaypoint instance ready for use with CarPlay templates

## Parameters

- `waypoint`: The navigation waypoint
- `travelEstimates`: The calculated travel estimates for reaching this waypoint


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint/init(waypoint:travelestimates:))*