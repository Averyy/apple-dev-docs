# HKAppleWalkingSteadinessMaximumQuantityForClassification

**Framework**: HealthKit  
**Kind**: func

Returns the maximum score for the steadiness of the user’s gait based on the provided classification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
extern HKQuantity * HKAppleWalkingSteadinessMaximumQuantityForClassification(HKAppleWalkingSteadinessClassification classification);
```

#### Discussion

Call this method to look up the maximum Walking Steadiness value for a given classification. It returns an [`HKQuantity`](hkquantity.md) instance that contains a percentage value between `0.0` and `1.0`.

## Parameters

- `classification`: The classification to look up.

## See Also

- [enum HKAppleWalkingSteadinessClassification](hkapplewalkingsteadinessclassification.md)
  A classification of a score based on the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessClassificationForQuantity](hkapplewalkingsteadinessclassificationforquantity.md)
  Provides a classification for a score that measures the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessMinimumQuantityForClassification](hkapplewalkingsteadinessminimumquantityforclassification.md)
  Returns the minimum score for the steadiness of the user’s gait based on the provided classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplewalkingsteadinessmaximumquantityforclassification)*