# splitTotalEnergy(_:start:end:resultsHandler:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Calculates the active and resting energy burned based on the total energy burned over the given duration.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: No longer supported

## Declaration

```swift
func splitTotalEnergy(_ totalEnergy: HKQuantity, start startDate: Date, end endDate: Date, resultsHandler: @escaping @Sendable (HKQuantity?, HKQuantity?, (any Error)?) -> Void)
```

```objc
- (void) splitTotalEnergy:(HKQuantity *) totalEnergy startDate:(NSDate *) startDate endDate:(NSDate *) endDate resultsHandler:(void (^)(HKQuantity *restingEnergy, HKQuantity *activeEnergy, NSError *error)) resultsHandler;
```

#### Discussion

This method operates asynchronously. As soon as the calculation is finished, it calls the completion block on a background queue.

This method splits the total calories into the active and resting calories, based on the user’s estimated resting metabolic rate and the activity’s duration. Use the resulting values to create samples representing both the active and resting energy burned.

Active energy samples contribute to Apple Watch’s activity monitoring.

## Parameters

- `totalEnergy`: A quantity object containing the total energy burned during the specified time period.
- `startDate`: A date object representing the activity’s start time.
- `endDate`: A date object representing the activity’s end time.
- `resultsHandler`: A block that is called as soon as the calculations are complete. This block is passed the following parameters:

  - **restingEnergy**: A quantity object containing the resting portion of the total energy.
  - **activeEnergy**: A quantity object containing the active portion of the total energy.
  - **error**: An error object. If an error occurred, this object contains information about the error; otherwise, it is set to `nil`.

## See Also

### Managing workouts
- [func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void)](./recoveractiveworkoutsession%28completion%29.md)
  Recovers an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/splittotalenergy(_:start:end:resultshandler:))*