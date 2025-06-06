# com.apple.developer.sensorkit.reader.allow

**Framework**: Bundle Resources  
**Kind**: typealias

The necessary entitlement to access sensor data that’s required by your app’s preapproved research study.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

#### Discussion

An app can read sensor data from devices on a per-team basis, and the system closes your app if its code signature lacks this entitlement. To attain it, submit your research study to Apple as described in [`Accessing SensorKit Data`](https://developer.apple.comhttps://www.researchandcare.org/resources/accessing-sensorkit-data/). If Apple approves your study, you can create a provisioning profile that signs code with this entitlement. For more information, see [`Configuring your project for sensor reading`](https://developer.apple.com/documentation/SensorKit/configuring-your-project-for-sensor-reading).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sensorkit.reader.allow)*