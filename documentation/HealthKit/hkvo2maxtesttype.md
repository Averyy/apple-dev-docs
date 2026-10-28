# HKVO2MaxTestType

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKVO2MaxTestType : NSInteger;
```

## Overview

VO2 max represents the maximal oxygen consumption during incremental exercise. VO2 max is an important indicator of fitness and endurance.

## Topics

### Test Types
- [HKVO2MaxTestType.maxExercise](./hkvo2maxtesttype/maxexercise.md)
  A test that measures VO2 max rate by monitoring exercise to the user’s physical limit.
- [HKVO2MaxTestType.predictionSubMaxExercise](./hkvo2maxtesttype/predictionsubmaxexercise.md)
  A calculation that estimates VO2 max rate based on low-intensity exercise.
- [HKVO2MaxTestType.predictionNonExercise](./hkvo2maxtesttype/predictionnonexercise.md)
  A calculation that estimates VO2 max rate without any exercise.
### Enumeration Cases
- [HKVO2MaxTestType.predictionStepTest](./hkvo2maxtesttype/predictionsteptest.md)
### Initializers
- [init?(rawValue: Int)](./hkvo2maxtesttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvo2maxtesttype)*