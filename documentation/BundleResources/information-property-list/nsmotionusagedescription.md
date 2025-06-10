# NSMotionUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells the user why the app is requesting access to the device’s motion data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.15+
- visionOS 1.0+

#### Discussion

> ❗ **Important**:  This key is required if your app uses APIs that access the device’s motion data, including [`CMSensorRecorder`](https://developer.apple.com/documentation/CoreMotion/CMSensorRecorder), [`CMPedometer`](https://developer.apple.com/documentation/CoreMotion/CMPedometer), [`CMMotionActivityManager`](https://developer.apple.com/documentation/CoreMotion/CMMotionActivityManager), and [`CMMovementDisorderManager`](https://developer.apple.com/documentation/CoreMotion/CMMovementDisorderManager). If you don’t include this key, your app will crash when it attempts to access motion data.

## See Also

- [NSFallDetectionUsageDescription](information-property-list/nsfalldetectionusagedescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmotionusagedescription)*