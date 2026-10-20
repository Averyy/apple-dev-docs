# cancelTrip()

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the navigation session to cancel the trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func cancelTrip()
```

```objc
- (void) cancelTrip;
```

## See Also

### Managing Trip Navigation
- [func finishTrip()](./finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)](./pausetrip%28for,description,turncardcolor%29.md)
- [CPNavigationSession.PauseReason](./pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/canceltrip())*