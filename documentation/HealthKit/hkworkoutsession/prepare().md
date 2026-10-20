# prepare()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Prepares the workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func prepare()
```

```objc
- (void) prepare;
```

## See Also

### Related Documentation
- [HKWorkoutSessionState.prepared](../hkworkoutsessionstate/prepared.md)
  The session is ready but not yet running.
### Managing the workout
- [func startActivity(with: Date?)](./startactivity%28with%29.md)
  Starts the workout session activity, and sets the start date.
- [func pause()](./pause%28%29.md)
  Pauses the workout session.
- [func resume()](./resume%28%29.md)
  Resumes the workout session.
- [func stopActivity(with: Date?)](./stopactivity%28with%29.md)
  Stops the workout session activity, and sets the end date.
- [func end()](./end%28%29.md)
  Ends the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/prepare())*