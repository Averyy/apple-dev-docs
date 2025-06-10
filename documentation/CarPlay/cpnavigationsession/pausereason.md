# CPNavigationSession.PauseReason

**Framework**: CarPlay  
**Kind**: enum

A set of reasons for pausing a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum PauseReason
```

## Topics

### Reasons
- [CPNavigationSession.PauseReason.arrived](cpnavigationsession/pausereason/arrived.md)
  The user arrived at the destination.
- [CPNavigationSession.PauseReason.loading](cpnavigationsession/pausereason/loading.md)
  The system is loading the route.
- [CPNavigationSession.PauseReason.locating](cpnavigationsession/pausereason/locating.md)
  The system is locating the destination.
- [CPNavigationSession.PauseReason.proceedToRoute](cpnavigationsession/pausereason/proceedtoroute.md)
  The system is waiting for the user to proceed to the route.
- [CPNavigationSession.PauseReason.rerouting](cpnavigationsession/pausereason/rerouting.md)
  The system is rerouting the trip.
### Initializers
- [init?(rawValue: UInt)](cpnavigationsession/pausereason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func cancelTrip()](cpnavigationsession/canceltrip.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](cpnavigationsession/finishtrip.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](cpnavigationsession/pausetrip(for:description:).md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](cpnavigationsession/pausetrip(for:description:turncardcolor:).md)
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](cpnavigationsession/resumetrip(updatedrouteinformation:).md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/pausereason)*