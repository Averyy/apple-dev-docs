# CPNavigationSession

**Framework**: CarPlay  
**Kind**: class

An object that represents an active route guidance session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPNavigationSession
```

#### Overview

To start a navigation session, you call [`startNavigationSession(for:)`](cpmaptemplate/startnavigationsession(for:).md) on the map template, passing the trip the user selected. The map template’s delegate receives the selected trip via [`mapTemplate(_:startedTrip:using:)`](cpmaptemplatedelegate/maptemplate(_:startedtrip:using:).md).

When calculating the initial set of maneuvers, you set [`pauseTrip(for:description:)`](cpnavigationsession/pausetrip(for:description:).md) to [`CPNavigationSession.PauseReason.loading`](cpnavigationsession/pausereason/loading.md) so that CarPlay displays the correct state to the user.

During turn-by-turn guidance, you create [`CPManeuver`](cpmaneuver.md) objects that contain information about upcoming turns, and then update [`upcomingManeuvers`](cpnavigationsession/upcomingmaneuvers.md). Maintain at least one maneuver in the array at all times. You should call [`updateEstimates(_:for:)`](cpnavigationsession/updateestimates(_:for:).md) regularly to update the remaining time and distance for each maneuver.

When CarPlay pauses, finishes, or cancels route guidance, you must call the corresponding method on the active navigation session.

## Topics

### Getting the Trip
- [var trip: CPTrip](cpnavigationsession/trip.md)
  The trip associated with the navigation session.
- [class CPTrip](cptrip.md)
  An object that represents a journey between an origin and a destination.
### Managing Trip Navigation
- [func cancelTrip()](cpnavigationsession/canceltrip.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](cpnavigationsession/finishtrip.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](cpnavigationsession/pausetrip(for:description:).md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](cpnavigationsession/pausetrip(for:description:turncardcolor:).md)
- [CPNavigationSession.PauseReason](cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](cpnavigationsession/resumetrip(updatedrouteinformation:).md)
  Resumes the current trip with updated route information.
### Managing Upcoming Maneuvers
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
- [func add([CPLaneGuidance])](cpnavigationsession/add(_:)-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.
### Updating Travel Estimates
- [func updateEstimates(CPTravelEstimates, for: CPManeuver)](cpnavigationsession/updateestimates(_:for:).md)
  Updates the travel estimates for the specified maneuver.
- [class CPTravelEstimates](cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func startNavigationSession(for: CPTrip) -> CPNavigationSession](cpmaptemplate/startnavigationsession(for:).md)
  Begins navigational guidance for a trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession)*