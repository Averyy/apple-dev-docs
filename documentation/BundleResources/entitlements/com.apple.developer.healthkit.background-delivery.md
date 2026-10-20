# com.apple.developer.healthkit.background-delivery

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether observer queries receive updates while running in the background.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Details

- **Name**: `com.apple.developer.healthkit.background-delivery` (HealthKit Observer Query Background Delivery)
- **Type**: boolean

#### Discussion

If this key is [`true`](../../Swift/true.md), your app can enable background delivery of [`HKObserverQuery`](../../HealthKit/hkobserverquery.md) instances by calling the HealthKit store’s [`enableBackgroundDelivery(for:frequency:withCompletion:)`](../../HealthKit/hkhealthstore/enablebackgrounddelivery%28for,frequency,withcompletion%29.md) method. By default, the value is [`false`](../../Swift/false.md).

## See Also

### Health
- [HealthKit Entitlement](./com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](./com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [Fall Detection Notifications](./com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.recalibrate-estimates](./com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.
- [com.apple.developer.healthkit.research](./com.apple.developer.healthkit.research.md)
  A Boolean value that indicates whether an approved health research app offers only Full Access when it requests HealthKit read access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.background-delivery)*