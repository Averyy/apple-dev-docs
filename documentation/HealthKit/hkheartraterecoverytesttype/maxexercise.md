# HKHeartRateRecoveryTestType.maxExercise

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

Measures a person’s actual heart-rate recovery.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case maxExercise
```

```c
HKHeartRateRecoveryTestTypeMaxExercise
```

## Discussion

In this test, a person exercises to their physical limit. The test measures their max heart rate during the workout, and then compares this with their heart rate after the workout ends. This lets the test calculate the actual heart rate recovery.

## See Also

### Heart-rate recovery tests
- [HKHeartRateRecoveryTestType.predictionNonExercise](./predictionnonexercise.md)
  A test that estimates a person’s heart-rate recovery without using exercise.
- [HKHeartRateRecoveryTestType.predictionSubMaxExercise](./predictionsubmaxexercise.md)
  A test that estimates a person’s heart-rate recovery using lower-intensity exercise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartraterecoverytesttype/maxexercise)*