# workoutSession(_:didEndActivityWith:date:)

**Framework**: HealthKit  
**Kind**: method

Tells the session that the current workout activity ended.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func workoutSession(_ workoutSession: HKWorkoutSession, didEndActivityWith workoutConfiguration: HKWorkoutConfiguration, date: Date)
```

## Parameters

- `workoutSession`: The workout session for the activity that just ended.
- `workoutConfiguration`: The workout configuration object for the activity.
- `date`: The end date and time for the activity.

## See Also

- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](hkworkoutsessiondelegate/workoutsession(_:didfailwitherror:).md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](hkworkoutsessiondelegate/workoutsession(_:didgenerate:).md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:).md)
  Tells the delegate that a new workout session began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:))*