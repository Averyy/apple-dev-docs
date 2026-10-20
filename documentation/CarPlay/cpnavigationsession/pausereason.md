# CPNavigationSession.PauseReason

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

A set of reasons for pausing a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum PauseReason
```

```c
enum CPTripPauseReason : NSUInteger;
```

## Topics

### Reasons
- [CPNavigationSession.PauseReason.arrived](./pausereason/arrived.md)
  The user arrived at the destination.
- [CPNavigationSession.PauseReason.loading](./pausereason/loading.md)
  The system is loading the route.
- [CPNavigationSession.PauseReason.locating](./pausereason/locating.md)
  The system is locating the destination.
- [CPNavigationSession.PauseReason.proceedToRoute](./pausereason/proceedtoroute.md)
  The system is waiting for the user to proceed to the route.
- [CPNavigationSession.PauseReason.rerouting](./pausereason/rerouting.md)
  The system is rerouting the trip.
### Initializers
- [init?(rawValue: UInt)](./pausereason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Trip Navigation
- [func cancelTrip()](./canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./pausetrip%28for,description,turncardcolor%29.md)
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/pausereason)*