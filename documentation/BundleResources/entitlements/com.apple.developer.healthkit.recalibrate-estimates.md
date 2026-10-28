# com.apple.developer.healthkit.recalibrate-estimates

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Details

- **Name**: `com.apple.developer.healthkit.recalibrate-estimates`
- **Type**: boolean

## Discussion

Apps can recalibrate HealthKitʼs prediction algorithms after an event that may significantly affect their results. For example, you can recalibrate the [`sixMinuteWalkTestDistance`](../../HealthKit/hkquantitytypeidentifier/sixminutewalktestdistance.md) type to use only data collected after a mobility-impacting health event, such as surgery or an injury.

To check whether a sample type supports recalibration, see [`allowsRecalibrationForEstimates`](../../HealthKit/hksampletype/allowsrecalibrationforestimates.md). To recalibrate the sample, see [`recalibrateEstimates(sampleType:date:completion:)`](../../HealthKit/hkhealthstore/recalibrateestimates%28sampletype,date,completion%29.md).

## See Also

### Health
- [HealthKit Entitlement](./com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](./com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [com.apple.developer.healthkit.background-delivery](./com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [Fall Detection Notifications](./com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.research](./com.apple.developer.healthkit.research.md)
  A Boolean value that indicates whether an approved health research app offers only Full Access when it requests HealthKit read access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.recalibrate-estimates)*