# pauseTrip(for:description:)

**Framework**: CarPlay  
**Kind**: method

Tells the navigation session to pause the trip for the specified reason.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func pauseTrip(for reason: CPNavigationSession.PauseReason, description: String?)
```

## Parameters

- `reason`: The reason for pausing the trip.
- `description`: An optional description of the pause reason. To use a system-provided value, set this parameter to  .

## See Also

- [func cancelTrip()](cpnavigationsession/canceltrip.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](cpnavigationsession/finishtrip.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](cpnavigationsession/pausetrip(for:description:turncardcolor:).md)
- [CPNavigationSession.PauseReason](cpnavigationsession/pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](cpnavigationsession/resumetrip(updatedrouteinformation:).md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/pausetrip(for:description:))*