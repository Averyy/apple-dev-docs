# endCollection(withEnd:completion:)

**Framework**: HealthKit  
**Kind**: method

Stops the collection of data, sets the workout’s end date, and deactivates the workout builder.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func endCollection(at endDate: Date) async throws
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## See Also

- [var endDate: Date?](hkworkoutbuilder/enddate.md)
  The workout’s end date and time.
- [func finishWorkout(completion: (HKWorkout?, (any Error)?) -> Void)](hkworkoutbuilder/finishworkout(completion:).md)
  Creates the workout, using the samples and events added to the builder, and saves it to the HealthKit store.
- [func discardWorkout()](hkworkoutbuilder/discardworkout.md)
  Stops the collection of data and discards the current results without saving the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/endcollection(withend:completion:))*