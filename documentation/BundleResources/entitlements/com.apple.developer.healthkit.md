# HealthKit Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.healthkit` (HealthKit)
- **Type**: boolean

#### Discussion

To add this entitlement to your app, enable the HealthKit capability in Xcode.

## See Also

### Health
- [HealthKit Capabilities Entitlement](./com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [com.apple.developer.healthkit.background-delivery](./com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [Fall Detection Notifications](./com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.recalibrate-estimates](./com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.
- [com.apple.developer.healthkit.research](./com.apple.developer.healthkit.research.md)
  A Boolean value that indicates whether an approved health research app offers only Full Access when it requests HealthKit read access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit)*