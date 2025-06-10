# currentLaneGuidance

**Framework**: CarPlay  
**Kind**: property

The current lane guidance to use for navigation metadata.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@NSCopying
@MainActor var currentLaneGuidance: CPLaneGuidance? { get set }
```

#### Discussion

First, add the required [`CPLaneGuidance`](cplaneguidance.md) objects to the session using [`add(_:)`](CPNavigationSession/add(_:)-93qpu.md), then set this property with the current lane guidance.

Set this property to `nil` if there’s no current lane guidance.

## See Also

- [var upcomingManeuvers: [CPManeuver]](cpnavigationsession/upcomingmaneuvers.md)
  The next set of maneuvers the user should perform while following the current route.
- [var maneuverState: CPManeuverState](cpnavigationsession/maneuverstate.md)
  The current maneuver state.
- [var currentRoadNameVariants: [String]](cpnavigationsession/currentroadnamevariants.md)
  An array of strings that describe variants of the current road name.
- [func add([CPManeuver])](cpnavigationsession/add(_:)-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](cpnavigationsession/add(_:)-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/currentlaneguidance)*