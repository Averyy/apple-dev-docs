# com.apple.developer.healthkit.recalibrate-estimates

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

#### Discussion

Apps can recalibrate HealthKitʼs prediction algorithms after an event that may significantly affect their results. For example, you can recalibrate the [`sixMinuteWalkTestDistance`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/sixMinuteWalkTestDistance) type to use only data collected after a mobility-impacting health event, such as surgery or an injury.

To check whether a sample type supports recalibration, see [`allowsRecalibrationForEstimates`](https://developer.apple.com/documentation/HealthKit/HKSampleType/allowsRecalibrationForEstimates). To recalibrate the sample, see [`recalibrateEstimates(sampleType:date:completion:)`](https://developer.apple.com/documentation/HealthKit/HKHealthStore/recalibrateEstimates(sampleType:date:completion:)).

## See Also

- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](entitlements/com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [com.apple.developer.healthkit.background-delivery](entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [Fall Detection Notifications](entitlements/com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.recalibrate-estimates)*