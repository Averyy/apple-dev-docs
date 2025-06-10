# upcomingManeuvers

**Framework**: CarPlay  
**Kind**: property

The next set of maneuvers the user should perform while following the current route.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var upcomingManeuvers: [CPManeuver] { get set }
```

#### Discussion

The system displays multiple maneuvers at the same time. However, the system may limit the number of visible maneuvers.

## See Also

- [var maneuverState: CPManeuverState](cpnavigationsession/maneuverstate.md)
  The current maneuver state.
- [var currentRoadNameVariants: [String]](cpnavigationsession/currentroadnamevariants.md)
  An array of strings that describe variants of the current road name.
- [var currentLaneGuidance: CPLaneGuidance?](cpnavigationsession/currentlaneguidance.md)
  The current lane guidance to use for navigation metadata.
- [func add([CPManeuver])](cpnavigationsession/add(_:)-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](cpnavigationsession/add(_:)-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/upcomingmaneuvers)*