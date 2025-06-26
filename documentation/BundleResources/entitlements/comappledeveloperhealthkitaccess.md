# HealthKit Capabilities Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

Health data types that require additional permission.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

#### Discussion

The [`HealthKit Entitlement`](entitlements/com.apple.developer.healthkit.md) provides access to most HealthKit data types. However, because of their highly sensitive nature, some data types require additional entitlements. The [`HealthKit Capabilities Entitlement`](entitlements/com.apple.developer.healthkit.access.md) provides access to these data types.

To add this entitlement to your app, first enable the HealthKit capability in Xcode, and then check any values that you want to add to the [`HealthKit Capabilities Entitlement`](entitlements/com.apple.developer.healthkit.access.md).

Only add values for data types that your app needs to access. App Review may reject apps that don’t use the data appropriately. For more information, see the [`Health and Health Research`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/#health-and-health-research) section of the [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/).

## See Also

- [Accessing Health Records](../HealthKit/accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [com.apple.developer.healthkit.background-delivery](entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [Fall Detection Notifications](entitlements/com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.recalibrate-estimates](entitlements/com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.access)*