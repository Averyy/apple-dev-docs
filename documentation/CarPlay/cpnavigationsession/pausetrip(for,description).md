# pauseTrip(for:description:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the navigation session to pause the trip for the specified reason.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func pauseTrip(for reason: CPNavigationSession.PauseReason, description: String?)
```

```objc
- (void) pauseTripForReason:(CPTripPauseReason) reason description:(NSString *) description;
```

## Parameters

- `reason`: The reason for pausing the trip.
- `description`: An optional description of the pause reason. To use a system-provided value, set this parameter to `nil`.

## See Also

### Managing Trip Navigation
- [func cancelTrip()](./canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./pausetrip%28for,description,turncardcolor%29.md)
- [CPNavigationSession.PauseReason](./pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/pausetrip(for:description:))*