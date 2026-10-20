# workoutSession(_:didEndActivityWith:date:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) workoutSession:(HKWorkoutSession *) workoutSession didEndActivityWithConfiguration:(HKWorkoutConfiguration *) workoutConfiguration date:(NSDate *) date;
```

## Parameters

- `workoutSession`: The workout session for the activity that just ended.
- `workoutConfiguration`: The workout configuration object for the activity.
- `date`: The end date and time for the activity.

## See Also

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](./workoutsession%28_,didchangeto,from,date%29.md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](./workoutsession%28_,didfailwitherror%29.md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](./workoutsession%28_,didgenerate%29.md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didbeginactivitywith,date%29.md)
  Tells the delegate that a new workout session began.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:))*