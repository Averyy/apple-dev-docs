# HKAppleWalkingSteadinessClassification

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

A classification of a score based on the steadiness of the user’s gait.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum HKAppleWalkingSteadinessClassification
```

```c
enum HKAppleWalkingSteadinessClassification : NSInteger;
```

## Overview

Walking Steadiness classifications measures the ability of the user to move with a steady, even gait. You can use the [`HKAppleWalkingSteadinessClassificationForQuantity`](./hkapplewalkingsteadinessclassificationforquantity.md), [`HKAppleWalkingSteadinessMaximumQuantityForClassification`](./hkapplewalkingsteadinessmaximumquantityforclassification.md), and [`HKAppleWalkingSteadinessMinimumQuantityForClassification`](./hkapplewalkingsteadinessminimumquantityforclassification.md) methods to convert between Walking Steadiness scores and the [`HKAppleWalkingSteadinessClassification.low`](./hkapplewalkingsteadinessclassification/low.md), [`HKAppleWalkingSteadinessClassification.veryLow`](./hkapplewalkingsteadinessclassification/verylow.md), or [`HKAppleWalkingSteadinessClassification.ok`](./hkapplewalkingsteadinessclassification/ok.md) classifications.

## Topics

### Accessing classifications
- [HKAppleWalkingSteadinessClassification.ok](./hkapplewalkingsteadinessclassification/ok.md)
  A classification indicating that the stability of the user’s gait is within the normal range.
- [HKAppleWalkingSteadinessClassification.low](./hkapplewalkingsteadinessclassification/low.md)
  A classification indicating that the stability of the user’s gate is below normal.
- [HKAppleWalkingSteadinessClassification.veryLow](./hkapplewalkingsteadinessclassification/verylow.md)
  A classification indicating that the stability of the user’s gate is considerably below normal.
### Accessing extremes
- [var minimum: HKQuantity](./hkapplewalkingsteadinessclassification/minimum.md)
  The maximum walking steadiness percentage for the classification.
- [var maximum: HKQuantity](./hkapplewalkingsteadinessclassification/maximum.md)
  The minimum walking steadiness percentage for the classification.
### Initializers
- [init(for: HKQuantity) throws](./hkapplewalkingsteadinessclassification/init%28for%29.md)
  Creates a new classification for the provided percentage.
- [init?(rawValue: Int)](./hkapplewalkingsteadinessclassification/init%28rawvalue%29.md)
### Default Implementations
- [CaseIterable Implementations](./hkapplewalkingsteadinessclassification/caseiterable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Walking steadiness classifications
- [HKAppleWalkingSteadinessClassificationForQuantity](./hkapplewalkingsteadinessclassificationforquantity.md)
  Provides a classification for a score that measures the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessMaximumQuantityForClassification](./hkapplewalkingsteadinessmaximumquantityforclassification.md)
  Returns the maximum score for the steadiness of the user’s gait based on the provided classification.
- [HKAppleWalkingSteadinessMinimumQuantityForClassification](./hkapplewalkingsteadinessminimumquantityforclassification.md)
  Returns the minimum score for the steadiness of the user’s gait based on the provided classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplewalkingsteadinessclassification)*