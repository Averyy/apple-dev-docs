# HKMetadataKeyCoachedWorkout

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether the workout was performed with a coach or personal trainer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyCoachedWorkout: String
```

```c
extern NSString * const HKMetadataKeyCoachedWorkout;
```

## Discussion

Set this key’s value to [`true`](../Swift/true.md) if the workout was performed with a coach or personal trainer; otherwise, set it to [`false`](../Swift/false.md).

## See Also

### Workout Type
- [let HKMetadataKeyActivityType: String](./hkmetadatakeyactivitytype.md)
- [let HKMetadataKeyAppleFitnessPlusSession: String](./hkmetadatakeyapplefitnessplussession.md)
- [let HKMetadataKeyGroupFitness: String](./hkmetadatakeygroupfitness.md)
  A key that indicates whether the workout was performed as part of a group fitness class.
- [let HKMetadataKeyIndoorWorkout: String](./hkmetadatakeyindoorworkout.md)
  A key that indicates whether the workout was performed indoors.
- [let HKMetadataKeyWorkoutBrandName: String](./hkmetadatakeyworkoutbrandname.md)
  The brand name of a particular workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeycoachedworkout)*