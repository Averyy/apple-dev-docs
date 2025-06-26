# stopActivity(with:)

**Framework**: HealthKit  
**Kind**: method

Stops the workout session activity, and sets the end date.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func stopActivity(with date: Date?)
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## Parameters

- `date`: The end date for the workout session. This must be equal to or after the start date.

## See Also

- [HKWorkoutSessionState.stopped](hkworkoutsessionstate/stopped.md)
  The session has stopped.
- [func prepare()](hkworkoutsession/prepare.md)
  Prepares the workout session.
- [func startActivity(with: Date?)](hkworkoutsession/startactivity(with:).md)
  Starts the workout session activity, and sets the start date.
- [func pause()](hkworkoutsession/pause.md)
  Pauses the workout session.
- [func resume()](hkworkoutsession/resume.md)
  Resumes the workout session.
- [func end()](hkworkoutsession/end.md)
  Ends the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/stopactivity(with:))*