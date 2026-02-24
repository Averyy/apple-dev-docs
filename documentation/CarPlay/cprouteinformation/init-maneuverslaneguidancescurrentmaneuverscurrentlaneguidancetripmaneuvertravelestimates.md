# init(maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:trip:maneuverTravelEstimates:)

**Framework**: CarPlay  
**Kind**: init

Initializes a new route information object with maneuvers, lane guidances, the current maneuvers, the current lane guidance, and trip and current maneuver travel estimates.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init(maneuvers: [CPManeuver], laneGuidances: [CPLaneGuidance], currentManeuvers: [CPManeuver], currentLaneGuidance: CPLaneGuidance, trip tripTravelEstimates: CPTravelEstimates, maneuverTravelEstimates: CPTravelEstimates)
```

## Parameters

- `maneuvers`: An array of [`CPManeuver`](cpmaneuver.md) objects.
- `laneGuidances`: An array of [`CPLaneGuidance`](cplaneguidance.md) objects.
- `currentManeuvers`: An array of `CPManeuver` objects that represent the current list of maneuvers.
- `currentLaneGuidance`: A [`CPLaneGuidance`](cplaneguidance.md) object that represents the guidance for the current lane.
- `maneuverTravelEstimates`: The `CPTravelEstimates` that present the estimates for the trip’s maneuvers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cprouteinformation/init(maneuvers:laneguidances:currentmaneuvers:currentlaneguidance:trip:maneuvertravelestimates:))*