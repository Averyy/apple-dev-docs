# CPNavigationSession

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

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

```objc
@interface CPNavigationSession : NSObject
```

## Overview

To start a navigation session, you call [`startNavigationSession(for:)`](./cpmaptemplate/startnavigationsession%28for%29.md) on the map template, passing the trip the user selected. The map template’s delegate receives the selected trip via [`mapTemplate(_:startedTrip:using:)`](./cpmaptemplatedelegate/maptemplate%28_,startedtrip,using%29.md).

When calculating the initial set of maneuvers, you set [`pauseTrip(for:description:)`](./cpnavigationsession/pausetrip%28for,description%29.md) to [`CPNavigationSession.PauseReason.loading`](./cpnavigationsession/pausereason/loading.md) so that CarPlay displays the correct state to the user.

During turn-by-turn guidance, you create [`CPManeuver`](./cpmaneuver.md) objects that contain information about upcoming turns, and then update [`upcomingManeuvers`](./cpnavigationsession/upcomingmaneuvers.md). Maintain at least one maneuver in the array at all times. You should call [`updateEstimates(_:for:)`](./cpnavigationsession/updateestimates%28_,for%29.md) regularly to update the remaining time and distance for each maneuver.

When CarPlay pauses, finishes, or cancels route guidance, you must call the corresponding method on the active navigation session.

## Topics

### Getting the Trip
- [var trip: CPTrip](./cpnavigationsession/trip.md)
  The trip associated with the navigation session.
- [class CPTrip](./cptrip.md)
  An object that represents a journey between an origin and a destination.
### Managing Trip Navigation
- [func cancelTrip()](./cpnavigationsession/canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./cpnavigationsession/finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./cpnavigationsession/pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./cpnavigationsession/pausetrip%28for,description,turncardcolor%29.md)
- [CPNavigationSession.PauseReason](./cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./cpnavigationsession/resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.
### Managing Upcoming Maneuvers
- [var upcomingManeuvers: [CPManeuver]](./cpnavigationsession/upcomingmaneuvers.md)
  The next set of maneuvers the user should perform while following the current route.
- [var maneuverState: CPManeuverState](./cpnavigationsession/maneuverstate.md)
  The current maneuver state.
- [var currentRoadNameVariants: [String]](./cpnavigationsession/currentroadnamevariants.md)
  An array of strings that describe variants of the current road name.
- [var currentLaneGuidance: CPLaneGuidance?](./cpnavigationsession/currentlaneguidance.md)
  The current lane guidance to use for navigation metadata.
- [func add([CPManeuver])](./cpnavigationsession/add%28_%29-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](./cpnavigationsession/add%28_%29-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
### Updating Travel Estimates
- [func updateEstimates(CPTravelEstimates, for: CPManeuver)](./cpnavigationsession/updateestimates%28_,for%29.md)
  Updates the travel estimates for the specified maneuver.
- [class CPTravelEstimates](./cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.
### Instance Properties
- [var currentSegment: CPRouteSegment](./cpnavigationsession/currentsegment.md)
  The current route segment.
- [var isRouteSharingEnabled: Bool](./cpnavigationsession/isroutesharingenabled.md)
  Whether the vehicle is presently using route data for any features in its built-in navigation system.
- [var isRouteSharingSupported: Bool](./cpnavigationsession/isroutesharingsupported.md)
  Whether the connected vehicle supports the route sharing feature.
- [var optionsPanel: CPMapPanel?](./cpnavigationsession/optionspanel.md)
  The options panel to display when the ellipsis button on the travel estimates is tapped.
- [var routeSegments: [CPRouteSegment]](./cpnavigationsession/routesegments.md)
  The route segments associated with this navigation session.
### Instance Methods
- [func addRouteSegments([CPRouteSegment])](./cpnavigationsession/addroutesegments%28_%29.md)
  Use this method to add CPRouteSegments in chronological order to the navigation session. CPRouteSegment objects must be added as soon as they are available.
- [func resumeNavigation(updatedTrip: CPTrip, routeSegments: [CPRouteSegment], currentSegment: CPRouteSegment, rerouteReason: CPRerouteReason)](./cpnavigationsession/resumenavigation%28updatedtrip,routesegments,currentsegment,reroutereason%29.md)
  Resume navigation with an updated trip and route segments for cases such as the trip destination changing.
- [func resumeTrip(updatedRouteSegments: [CPRouteSegment], currentSegment: CPRouteSegment, rerouteReason: CPRerouteReason)](./cpnavigationsession/resumetrip%28updatedroutesegments,currentsegment,reroutereason%29.md)
  Resume the current trip with updated route segments

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Navigating a Trip
- [func startNavigationSession(for: CPTrip) -> CPNavigationSession](./cpmaptemplate/startnavigationsession%28for%29.md)
  Begins navigational guidance for a trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession)*