# pauseTrip(for:description:turnCardColor:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func pauseTrip(for reason: CPNavigationSession.PauseReason, description: String?, turnCardColor: UIColor?)
```

```objc
- (void) pauseTripForReason:(CPTripPauseReason) reason description:(NSString *) description turnCardColor:(UIColor *) turnCardColor;
```

## See Also

### Managing Trip Navigation
- [func cancelTrip()](./canceltrip%28%29.md)
  Tells the navigation session to cancel the trip.
- [func finishTrip()](./finishtrip%28%29.md)
  Tells the navigation session to finish the trip.
- [func pauseTrip(for: CPNavigationSession.PauseReason, description: String?)](./pausetrip%28for,description%29.md)
  Tells the navigation session to pause the trip for the specified reason.
- [CPNavigationSession.PauseReason](./pausereason.md)
  A set of reasons for pausing a trip.
- [func resumeTrip(updatedRouteInformation: CPRouteInformation)](./resumetrip%28updatedrouteinformation%29.md)
  Resumes the current trip with updated route information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/pausetrip(for:description:turncardcolor:))*