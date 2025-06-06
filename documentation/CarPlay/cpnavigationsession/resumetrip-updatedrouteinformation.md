# resumeTrip(updatedRouteInformation:)

**Framework**: CarPlay  
**Kind**: method

Resumes the current trip with updated route information.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
func resumeTrip(updatedRouteInformation routeInformation: CPRouteInformation)
```

## Parameters

- `routeInformation`: The updated route information for the current trip.

## See Also

- [func cancelTrip()](cpnavigationsession/canceltrip.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](cpnavigationsession/finishtrip.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](cpnavigationsession/pausetrip(for:description:).md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](cpnavigationsession/pausetrip(for:description:turncardcolor:).md)
- [CPNavigationSession.PauseReason](cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/resumetrip(updatedrouteinformation:))*