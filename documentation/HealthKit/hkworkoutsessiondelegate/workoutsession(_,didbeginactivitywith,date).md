# workoutSession(_:didBeginActivityWith:date:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) workoutSession:(HKWorkoutSession *) workoutSession didBeginActivityWithConfiguration:(HKWorkoutConfiguration *) workoutConfiguration date:(NSDate *) date;
```

## Parameters

- `workoutSession`: The workout session that receives the new activity.
- `workoutConfiguration`: The workout configuration object for the new activity.
- `date`: The activity’s start date and time.

## See Also

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](./workoutsession%28_,didchangeto,from,date%29.md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](./workoutsession%28_,didfailwitherror%29.md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](./workoutsession%28_,didgenerate%29.md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didendactivitywith,date%29.md)
  Tells the session that the current workout activity ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:))*