# com.apple.developer.healthkit.background-delivery

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether observer queries receive updates while running in the background.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

#### Discussion

If this key is [`true`](https://developer.apple.com/documentation/Swift/true), your app can enable background delivery of [`HKObserverQuery`](https://developer.apple.com/documentation/HealthKit/HKObserverQuery) instances by calling the HealthKit store’s [`enableBackgroundDelivery(for:frequency:withCompletion:)`](https://developer.apple.com/documentation/HealthKit/HKHealthStore/enableBackgroundDelivery(for:frequency:withCompletion:)) method. By default, the value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](entitlements/com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [Fall Detection Notifications](entitlements/com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.recalibrate-estimates](entitlements/com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.background-delivery)*