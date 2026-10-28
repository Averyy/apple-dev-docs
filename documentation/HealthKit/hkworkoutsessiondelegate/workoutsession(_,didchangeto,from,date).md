# workoutSession(_:didChangeTo:from:date:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the session’s state changed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.10+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func workoutSession(_ workoutSession: HKWorkoutSession, didChangeTo toState: HKWorkoutSessionState, from fromState: HKWorkoutSessionState, date: Date)
```

```objc
- (void) workoutSession:(HKWorkoutSession *) workoutSession didChangeToState:(HKWorkoutSessionState) toState fromState:(HKWorkoutSessionState) fromState date:(NSDate *) date;
```

## Discussion

If your application is suspended, the delegate receives this call after the application resumes. This means you may receive the notification long after the state changed. Check the `date` parameter to determine when the state change actually occurred.

For a list of possible session states, see [`HKWorkoutSessionState`](../hkworkoutsessionstate.md).

## Parameters

- `workoutSession`: The workout session that changed.
- `toState`: The session’s new state. For a list of possible values, see [`HKWorkoutSessionState`](../hkworkoutsessionstate.md).
- `fromState`: The session’s previous state. For a list of possible values, see [`HKWorkoutSessionState`](../hkworkoutsessionstate.md).
- `date`: A date object indicating when the state change occurred.

## See Also

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](./workoutsession%28_,didfailwitherror%29.md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](./workoutsession%28_,didgenerate%29.md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didbeginactivitywith,date%29.md)
  Tells the delegate that a new workout session began.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](./workoutsession%28_,didendactivitywith,date%29.md)
  Tells the session that the current workout activity ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:))*