# recoverActiveWorkoutSession(completion:)

**Framework**: HealthKit  
**Kind**: method

Recovers an active workout session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- watchOS 5.0+

## Declaration

```swift
func recoverActiveWorkoutSession() async throws -> HKWorkoutSession?
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

#### Discussion

If your app crashes during an active workout session, the system calls your extension delegate’s [`handleActiveWorkoutRecovery()`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handleActiveWorkoutRecovery()) method the next time your app launches. To recover the workout session, call [`recoverActiveWorkoutSession(completion:)`](hkhealthstore/recoveractiveworkoutsession(completion:).md) from your extension delegate’s [`handleActiveWorkoutRecovery()`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handleActiveWorkoutRecovery()) method. HealthKit then attempts to restore the previous workout session, returning either a new session object or an error to the completion block.

As soon as you receive the session object, you must access its builder and set up your data source and delegates again, as described in [`Start a session`](running-workout-sessions#Start-a-session.md).

## See Also

- [func splitTotalEnergy(HKQuantity, start: Date, end: Date, resultsHandler: (HKQuantity?, HKQuantity?, (any Error)?) -> Void)](hkhealthstore/splittotalenergy(_:start:end:resultshandler:).md)
  Calculates the active and resting energy burned based on the total energy burned over the given duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/recoveractiveworkoutsession(completion:))*