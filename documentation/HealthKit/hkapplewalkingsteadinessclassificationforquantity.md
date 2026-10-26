# HKAppleWalkingSteadinessClassificationForQuantity

**Framework**: HealthKit  
**Kind**: func  
**Role**: Function

Provides a classification for a score that measures the steadiness of the user’s gait.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```c
extern BOOL HKAppleWalkingSteadinessClassificationForQuantity(HKQuantity *value, HKAppleWalkingSteadinessClassification *classificationOut, NSError **errorOut);
```

#### Return Value

Returns [`true`](../Swift/true.md) if the method successfully classified the value. If an error occurred, it returns [`false`](../Swift/false.md).

#### Discussion

Use this method to get the Walking Steadiness classification for an [`appleWalkingSteadiness`](./hkquantitytypeidentifier/applewalkingsteadiness.md) sample.

## Parameters

- `value`: An [`HKQuantity`](./hkquantity.md) instance that contains a percentage value between `0.0` and `1.0`. Use the [`HKUnit`](./hkunit.md) class’s [`percent()`](./hkunit/percent%28%29.md) method to define the units for these values.
- `classificationOut`: A [`HKAppleWalkingSteadinessClassificationForQuantity`](./hkapplewalkingsteadinessclassificationforquantity.md) reference, which the method sets if the classification is successful.
- `errorOut`: A [`NSError`](../Foundation/nserror.md) reference, which the method sets if it can’t convert the `value` parameter into a classification. You can pass `nil` if you don’t want to receive error information.

## See Also

### Walking steadiness classifications
- [enum HKAppleWalkingSteadinessClassification](./hkapplewalkingsteadinessclassification.md)
  A classification of a score based on the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessMaximumQuantityForClassification](./hkapplewalkingsteadinessmaximumquantityforclassification.md)
  Returns the maximum score for the steadiness of the user’s gait based on the provided classification.
- [HKAppleWalkingSteadinessMinimumQuantityForClassification](./hkapplewalkingsteadinessminimumquantityforclassification.md)
  Returns the minimum score for the steadiness of the user’s gait based on the provided classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplewalkingsteadinessclassificationforquantity)*