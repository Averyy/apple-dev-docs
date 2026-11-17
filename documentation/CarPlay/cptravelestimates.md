# CPTravelEstimates

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that describes the time and distance remaining for a maneuver in a navigation session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTravelEstimates
```

```objc
@interface CPTravelEstimates : NSObject
```

## Topics

### Creating travel estimates
- [init(distanceRemaining: Measurement<UnitLength>, timeRemaining: TimeInterval)](./cptravelestimates/init%28distanceremaining,timeremaining%29.md)
  Creates travel estimates with the remaining distance and time.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval)](./cptravelestimates/init%28distanceremaining,distanceremainingtodisplay,timeremaining%29.md)
  Creates a travel estimates instance with the distance remaining that the framework displays to a person.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval, routeDetails: [CPRouteDetail])](./cptravelestimates/init%28distanceremaining,distanceremainingtodisplay,timeremaining,routedetails%29.md)
  Initialize a @c CPTravelEstimates with distance, distance to display, time remaining, and additional trip information.
- [init?(coder: NSCoder)](./cptravelestimates/init%28coder%29.md)
### Managing upcoming maneuvers
- [func add([CPManeuver])](./cpnavigationsession/add%28_%29-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](./cpnavigationsession/add%28_%29-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
### Updating travel estimates
- [func updateEstimates(CPTravelEstimates, for: CPManeuver)](./cpnavigationsession/updateestimates%28_,for%29.md)
  Updates the travel estimates for the specified maneuver.
### Managing trip navigation
- [func cancelTrip()](./cpnavigationsession/canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./cpnavigationsession/finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./cpnavigationsession/pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./cpnavigationsession/pausetrip%28for,description,turncardcolor%29.md)
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./cpnavigationsession/resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.
- [CPNavigationSession.PauseReason](./cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.
### Getting travel estimates
- [var distanceRemaining: Measurement<UnitLength>](./cptravelestimates/distanceremaining.md)
  The remaining distance for the travel estimate.
- [var distanceRemainingToDisplay: Measurement<UnitLength>](./cptravelestimates/distanceremainingtodisplay.md)
  The distance remaining that the framework displays to a person, in the default units of measurement.
- [var timeRemaining: TimeInterval](./cptravelestimates/timeremaining.md)
  The remaining time for the travel estimate.
- [var routeDetails: [CPRouteDetail]](./cptravelestimates/routedetails.md)
  Additional trip information such as battery, fuel, or toll information to display with travel estimates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Maneuvers
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
- [enum CPManeuverState](./cpmaneuverstate.md)
  Values that describe the state of a maneuver.
- [enum CPManeuverType](./cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.
- [class CPTripPreviewTextConfiguration](./cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
- [func NSStringFromCPManeuverType(CPManeuverType) -> String!](./nsstringfromcpmaneuvertype%28_%29.md)
- [struct CPLocationCoordinate3D](./cplocationcoordinate3d.md)
  CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates)*