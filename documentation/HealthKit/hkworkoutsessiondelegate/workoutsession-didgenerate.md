# workoutSession(_:didGenerate:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that the system generated a workout event.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func workoutSession(_ workoutSession: HKWorkoutSession, didGenerate event: HKWorkoutEvent)
```

## Mentions

- [Receiving Downhill Skiing and Snowboarding Data](receiving-downhill-skiing-and-snowboarding-data.md)

#### Discussion

You can save the generated events and use them when creating a [`HKWorkout`](hkworkout.md) object for the session.

## Parameters

- `workoutSession`: The workout session associated with the event.
- `event`: The event that the system generated. For a list of possible values, see  .

## See Also

- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](hkworkoutsessiondelegate/workoutsession(_:didfailwitherror:).md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:).md)
  Tells the delegate that a new workout session began.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:).md)
  Tells the session that the current workout activity ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didgenerate:))*