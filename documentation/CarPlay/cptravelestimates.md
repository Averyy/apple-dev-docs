# CPTravelEstimates

**Framework**: CarPlay  
**Kind**: class

An object that describes the time and distance remaining for a maneuver in a navigation session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTravelEstimates
```

## Topics

### Getting the trip
- [class CPTrip](cptrip.md)
  An object that represents a journey between an origin and a destination.
### Managing upcoming maneuvers
- [func add([CPManeuver])](cpnavigationsession/add(_:)-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](cpnavigationsession/add(_:)-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.
### Creating a Travel Estimates Object
- [init(distanceRemaining: Measurement<UnitLength>, timeRemaining: TimeInterval)](cptravelestimates/init(distanceremaining:timeremaining:).md)
  Creates travel estimates with the remaining distance and time.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval)](cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:).md)
  Creates a travel estimates instance with the distance remaining that the framework displays to a person.
### Updating travel estimates
- [func updateEstimates(CPTravelEstimates, for: CPManeuver)](cpnavigationsession/updateestimates(_:for:).md)
  Updates the travel estimates for the specified maneuver.
### Managing trip navigation
- [func cancelTrip()](cpnavigationsession/canceltrip.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](cpnavigationsession/finishtrip.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](cpnavigationsession/pausetrip(for:description:).md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](cpnavigationsession/pausetrip(for:description:turncardcolor:).md)
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](cpnavigationsession/resumetrip(updatedrouteinformation:).md)
  Resumes the current trip with updated route information.
- [CPNavigationSession.PauseReason](cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.
### Getting Travel Estimates
- [var distanceRemaining: Measurement<UnitLength>](cptravelestimates/distanceremaining.md)
  The remaining distance for the travel estimate.
- [var distanceRemainingToDisplay: Measurement<UnitLength>](cptravelestimates/distanceremainingtodisplay.md)
  The distance remaining that the framework displays to a person, in the default units of measurement.
- [var timeRemaining: TimeInterval](cptravelestimates/timeremaining.md)
  The remaining time for the travel estimate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func updateEstimates(CPTravelEstimates, for: CPManeuver)](cpnavigationsession/updateestimates(_:for:).md)
  Updates the travel estimates for the specified maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates)*