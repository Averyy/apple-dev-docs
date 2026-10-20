# startActivity(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Starts the workout session activity, and sets the start date.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func startActivity(with date: Date?)
```

```objc
- (void) startActivityWithDate:(NSDate *) date;
```

## Parameters

- `date`: The start date for the workout session.

## See Also

### Related Documentation
- [HKWorkoutSessionState.running](../hkworkoutsessionstate/running.md)
  The workout session is running.
### Managing the workout
- [func prepare()](./prepare%28%29.md)
  Prepares the workout session.
- [func pause()](./pause%28%29.md)
  Pauses the workout session.
- [func resume()](./resume%28%29.md)
  Resumes the workout session.
- [func stopActivity(with: Date?)](./stopactivity%28with%29.md)
  Stops the workout session activity, and sets the end date.
- [func end()](./end%28%29.md)
  Ends the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/startactivity(with:))*