# startActivity(with:)

**Framework**: HealthKit  
**Kind**: method

Starts the workout session activity, and sets the start date.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func startActivity(with date: Date?)
```

## Parameters

- `date`: The start date for the workout session.

## See Also

- [HKWorkoutSessionState.running](hkworkoutsessionstate/running.md)
  The workout session is running.
- [func prepare()](hkworkoutsession/prepare.md)
  Prepares the workout session.
- [func pause()](hkworkoutsession/pause.md)
  Pauses the workout session.
- [func resume()](hkworkoutsession/resume.md)
  Resumes the workout session.
- [func stopActivity(with: Date?)](hkworkoutsession/stopactivity(with:).md)
  Stops the workout session activity, and sets the end date.
- [func end()](hkworkoutsession/end.md)
  Ends the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/startactivity(with:))*