# recoverActiveWorkoutSession(completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Recovers an active workout session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- watchOS 5.0+

## Declaration

```swift
func recoverActiveWorkoutSession(completion: @escaping @Sendable (HKWorkoutSession?, (any Error)?) -> Void)
```

```swift
func recoverActiveWorkoutSession() async throws -> HKWorkoutSession?
```

```objc
- (void) recoverActiveWorkoutSessionWithCompletion:(void (^)(HKWorkoutSession *session, NSError *error)) completion;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

#### Discussion

If your app crashes during an active workout session, the system calls your extension delegate’s [`handleActiveWorkoutRecovery()`](../../WatchKit/wkextensiondelegate/handleactiveworkoutrecovery%28%29.md) method the next time your app launches. To recover the workout session, call [`recoverActiveWorkoutSession(completion:)`](./recoveractiveworkoutsession%28completion%29.md) from your extension delegate’s [`handleActiveWorkoutRecovery()`](../../WatchKit/wkextensiondelegate/handleactiveworkoutrecovery%28%29.md) method. HealthKit then attempts to restore the previous workout session, returning either a new session object or an error to the completion block.

As soon as you receive the session object, you must access its builder and set up your data source and delegates again, as described in [Start a session](../running-workout-sessions.md#Start-a-session).

## See Also

### Managing workouts
- [func splitTotalEnergy(HKQuantity, start: Date, end: Date, resultsHandler: (HKQuantity?, HKQuantity?, (any Error)?) -> Void)](./splittotalenergy%28_,start,end,resultshandler%29.md)
  Calculates the active and resting energy burned based on the total energy burned over the given duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/recoveractiveworkoutsession(completion:))*