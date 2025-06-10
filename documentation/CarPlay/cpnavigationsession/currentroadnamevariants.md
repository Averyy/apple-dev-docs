# currentRoadNameVariants

**Framework**: CarPlay  
**Kind**: property

An array of strings that describe variants of the current road name.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@MainActor
var currentRoadNameVariants: [String] { get set }
```

#### Discussion

Set this property with variants of the current road name, from most to least verbose.

## See Also

- [var upcomingManeuvers: [CPManeuver]](cpnavigationsession/upcomingmaneuvers.md)
  The next set of maneuvers the user should perform while following the current route.
- [var maneuverState: CPManeuverState](cpnavigationsession/maneuverstate.md)
  The current maneuver state.
- [var currentLaneGuidance: CPLaneGuidance?](cpnavigationsession/currentlaneguidance.md)
  The current lane guidance to use for navigation metadata.
- [func add([CPManeuver])](cpnavigationsession/add(_:)-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](cpnavigationsession/add(_:)-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/currentroadnamevariants)*