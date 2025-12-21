# finishWorkout(completion:)

**Framework**: HealthKit  
**Kind**: method

Creates the workout, using the samples and events added to the builder, and saves it to the HealthKit store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func finishWorkout() async throws -> HKWorkout?
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Discussion

You must call [`endCollection(withEnd:completion:)`](hkworkoutbuilder/endcollection(withend:completion:).md) before calling this method. This function returns `nil` if finishing the workout succeeded but the workout sample is not available because the device is locked.

## Parameters

- `completion`: A completion handler that the system calls after the HKWorkout object has been created and saved. This handler takes the following parameters:

## See Also

- [func endCollection(withEnd: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/endcollection(withend:completion:).md)
  Stops the collection of data, sets the workout’s end date, and deactivates the workout builder.
- [var endDate: Date?](hkworkoutbuilder/enddate.md)
  The workout’s end date and time.
- [func discardWorkout()](hkworkoutbuilder/discardworkout.md)
  Stops the collection of data and discards the current results without saving the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/finishworkout(completion:))*