# workoutSession(_:didFailWithError:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the session failed with an error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func workoutSession(_ workoutSession: HKWorkoutSession, didFailWithError error: any Error)
```

```objc
- (void) workoutSession:(HKWorkoutSession *) workoutSession didFailWithError:(NSError *) error;
```

## Discussion

When the state of the workout session changes due to an error, HealthKit always calls this method before calling the [`workoutSession(_:didChangeTo:from:date:)`](./workoutsession%28_,didchangeto,from,date%29.md) method.

For example, if a second app starts a workout session, HealthKit calls the current session’s [`workoutSession(_:didFailWithError:)`](./workoutsession%28_,didfailwitherror%29.md) method. Next, it changes current session’s state to the [`HKWorkoutSessionState.ended`](../hkworkoutsessionstate/ended.md) value. Finally, HealthKit calls the current session’s [`workoutSession(_:didChangeTo:from:date:)`](./workoutsession%28_,didchangeto,from,date%29.md) method.

## Parameters

- `workoutSession`: The workout session that failed.
- `error`: An error object describing the failure.

## See Also

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](./workoutsession%28_,didchangeto,from,date%29.md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](./workoutsession%28_,didgenerate%29.md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didbeginactivitywith,date%29.md)
  Tells the delegate that a new workout session began.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didendactivitywith,date%29.md)
  Tells the session that the current workout activity ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didfailwitherror:))*