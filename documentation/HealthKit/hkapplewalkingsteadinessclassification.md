# HKAppleWalkingSteadinessClassification

**Framework**: HealthKit  
**Kind**: enum

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

#### Overview

Walking Steadiness classifications measures the ability of the user to move with a steady, even gait. You can use the [`HKAppleWalkingSteadinessClassificationForQuantity`](hkapplewalkingsteadinessclassificationforquantity.md), [`HKAppleWalkingSteadinessMaximumQuantityForClassification`](hkapplewalkingsteadinessmaximumquantityforclassification.md), and [`HKAppleWalkingSteadinessMinimumQuantityForClassification`](hkapplewalkingsteadinessminimumquantityforclassification.md) methods to convert between Walking Steadiness scores and the [`HKAppleWalkingSteadinessClassification.low`](hkapplewalkingsteadinessclassification/low.md), [`HKAppleWalkingSteadinessClassification.veryLow`](hkapplewalkingsteadinessclassification/verylow.md), or [`HKAppleWalkingSteadinessClassification.ok`](hkapplewalkingsteadinessclassification/ok.md) classifications.

## Topics

### Accessing Classifications
- [HKAppleWalkingSteadinessClassification.ok](hkapplewalkingsteadinessclassification/ok.md)
  A classification indicating that the stability of the user’s gait is within the normal range.
- [HKAppleWalkingSteadinessClassification.low](hkapplewalkingsteadinessclassification/low.md)
  A classification indicating that the stability of the user’s gate is below normal.
- [HKAppleWalkingSteadinessClassification.veryLow](hkapplewalkingsteadinessclassification/verylow.md)
  A classification indicating that the stability of the user’s gate is considerably below normal.
### Initializers
- [init(for: HKQuantity) throws](hkapplewalkingsteadinessclassification/init(for:).md)
  Creates a new classification for the provided percentage.
- [init?(rawValue: Int)](hkapplewalkingsteadinessclassification/init(rawvalue:).md)
### Instance Properties
- [var maximum: HKQuantity](hkapplewalkingsteadinessclassification/maximum.md)
  The minimum walking steadiness percentage for the classification.
- [var minimum: HKQuantity](hkapplewalkingsteadinessclassification/minimum.md)
  The maximum walking steadiness percentage for the classification.
### Default Implementations
- [CaseIterable Implementations](hkapplewalkingsteadinessclassification/caseiterable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplewalkingsteadinessclassification)*