# resumeTrip(updatedRouteInformation:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Resumes the current trip with updated route information.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
func resumeTrip(updatedRouteInformation routeInformation: CPRouteInformation)
```

```objc
- (void) resumeTripWithUpdatedRouteInformation:(CPRouteInformation *) routeInformation;
```

## Parameters

- `routeInformation`: The updated route information for the current trip.

## See Also

### Managing Trip Navigation
- [func cancelTrip()](./canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./pausetrip%28for,description,turncardcolor%29.md)
- [CPNavigationSession.PauseReason](./pausereason.md)
  A set of reasons for pausing a trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/resumetrip(updatedrouteinformation:))*