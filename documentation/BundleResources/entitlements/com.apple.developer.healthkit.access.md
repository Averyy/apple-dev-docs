# HealthKit Capabilities Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

Health data types that require additional permission.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.healthkit.access` (HealthKit Capabilities)
- **Type**: array of string 

## Possible Values

- `health-records`: The app can request access to FHIR-backed clinical records.

#### Discussion

The [HealthKit Entitlement](./com.apple.developer.healthkit.md) provides access to most HealthKit data types. However, because of their highly sensitive nature, some data types require additional entitlements. The [HealthKit Capabilities Entitlement](./com.apple.developer.healthkit.access.md) provides access to these data types.

To add this entitlement to your app, first enable the HealthKit capability in Xcode, and then check any values that you want to add to the [HealthKit Capabilities Entitlement](./com.apple.developer.healthkit.access.md).

Only add values for data types that your app needs to access. App Review may reject apps that don’t use the data appropriately. For more information, see the [Health and Health Research](https://developer.apple.com/app-store/review/guidelines/#health-and-health-research) section of the [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

## See Also

### Related Documentation
- [Accessing Health Records](../../HealthKit/accessing-health-records.md)
  Read clinical record data from the HealthKit store.
### Health
- [HealthKit Entitlement](./com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [com.apple.developer.healthkit.background-delivery](./com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [Fall Detection Notifications](./com.apple.developer.health.fall-detection.md)
  An entitlement that permits an app to receive fall-detection notifications from Apple Watch.
- [com.apple.developer.healthkit.recalibrate-estimates](./com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.
- [com.apple.developer.healthkit.research](./com.apple.developer.healthkit.research.md)
  A Boolean value that indicates whether an approved health research app offers only Full Access when it requests HealthKit read access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit.access)*