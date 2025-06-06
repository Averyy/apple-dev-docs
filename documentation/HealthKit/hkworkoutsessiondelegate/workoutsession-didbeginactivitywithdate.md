# workoutSession(_:didBeginActivityWith:date:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that a new workout session began.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func workoutSession(_ workoutSession: HKWorkoutSession, didBeginActivityWith workoutConfiguration: HKWorkoutConfiguration, date: Date)
```

## Parameters

- `workoutSession`: The workout session that receives the new activity.
- `workoutConfiguration`: The workout configuration object for the new activity.
- `date`: The activity’s start date and time.

## See Also

- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](hkworkoutsessiondelegate/workoutsession(_:didfailwitherror:).md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](hkworkoutsessiondelegate/workoutsession(_:didgenerate:).md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:).md)
  Tells the session that the current workout activity ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:))*