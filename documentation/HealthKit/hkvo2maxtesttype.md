# HKVO2MaxTestType

**Framework**: HealthKit  
**Kind**: enum

Methods for calculating the user’s VO2 max rate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HKVO2MaxTestType
```

#### Overview

VO2 max represents the maximal oxygen consumption during incremental exercise. VO2 max is an important indicator of fitness and endurance.

## Topics

### Test Types
- [HKVO2MaxTestType.maxExercise](hkvo2maxtesttype/maxexercise.md)
  A test that measures VO2 max rate by monitoring exercise to the user’s physical limit.
- [HKVO2MaxTestType.predictionSubMaxExercise](hkvo2maxtesttype/predictionsubmaxexercise.md)
  A calculation that estimates VO2 max rate based on low-intensity exercise.
- [HKVO2MaxTestType.predictionNonExercise](hkvo2maxtesttype/predictionnonexercise.md)
  A calculation that estimates VO2 max rate without any exercise.
### Initializers
- [init?(rawValue: Int)](hkvo2maxtesttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvo2maxtesttype)*