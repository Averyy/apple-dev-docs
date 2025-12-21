# Fall Detection Notifications

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that permits an app to receive fall-detection notifications from Apple Watch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- watchOS 6.0+

#### Discussion

Use the data you receive from [`CMFallDetectionManager`](https://developer.apple.com/documentation/CoreMotion/CMFallDetectionManager) to provide assistance, or initiate communication with emergency services, in the event that someone falls.

To request this entitlement for your app, [`fill out the request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/fall-detection-api/).

## See Also

- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](entitlements/com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [com.apple.developer.healthkit.background-delivery](entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [com.apple.developer.healthkit.recalibrate-estimates](entitlements/com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.health.fall-detection)*