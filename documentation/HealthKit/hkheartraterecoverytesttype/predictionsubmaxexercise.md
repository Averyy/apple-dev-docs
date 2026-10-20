# HKHeartRateRecoveryTestType.predictionSubMaxExercise

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

A test that estimates a person’s heart-rate recovery using lower-intensity exercise.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case predictionSubMaxExercise
```

```c
HKHeartRateRecoveryTestTypePredictionSubMaxExercise
```

#### Discussion

In this test, a person performs lower-intensity exercise, staying below their physical limit. The test then estimates their actual heart rate recovery based on the difference between their exercising heart rate, and the rate of recovery after the exercise ends.

## See Also

### Heart-rate recovery tests
- [HKHeartRateRecoveryTestType.maxExercise](./maxexercise.md)
  Measures a person’s actual heart-rate recovery.
- [HKHeartRateRecoveryTestType.predictionNonExercise](./predictionnonexercise.md)
  A test that estimates a person’s heart-rate recovery without using exercise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartraterecoverytesttype/predictionsubmaxexercise)*