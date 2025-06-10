# add(_:)

**Framework**: CarPlay  
**Kind**: method

Adds one or more lane guidance instances to the navigation session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@MainActor
func add(_ laneGuidances: [CPLaneGuidance])
```

#### Discussion

Use this method to add [`CPLaneGuidance`](cplaneguidance.md) elements in chronological order to the navigation session. Add [`CPLaneGuidance`](cplaneguidance.md) objects as soon as they are available.

## See Also

- [var upcomingManeuvers: [CPManeuver]](cpnavigationsession/upcomingmaneuvers.md)
  The next set of maneuvers the user should perform while following the current route.
- [var maneuverState: CPManeuverState](cpnavigationsession/maneuverstate.md)
  The current maneuver state.
- [var currentRoadNameVariants: [String]](cpnavigationsession/currentroadnamevariants.md)
  An array of strings that describe variants of the current road name.
- [var currentLaneGuidance: CPLaneGuidance?](cpnavigationsession/currentlaneguidance.md)
  The current lane guidance to use for navigation metadata.
- [func add([CPManeuver])](cpnavigationsession/add(_:)-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/add(_:)-93qpu)*