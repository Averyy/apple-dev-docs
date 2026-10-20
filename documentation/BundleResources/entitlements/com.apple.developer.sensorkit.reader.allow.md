# com.apple.developer.sensorkit.reader.allow

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The necessary entitlement to access sensor data that’s required by your app’s preapproved research study.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.sensorkit.reader.allow`
- **Type**: array of string 

## Possible Values

- `on-wrist`: A sensor that describes the watch’s position on the wrist.
- `ambient-light-sensor`: A sensor that provides ambient light information.
- `motion-accelerometer`: A sensor that provides acceleration motion data.
- `motion-rotation-rate`: A sensor that provides rotation motion data.
- `visits`: A sensor that provides information about the user’s frequently visited locations.
- `pedometer`: A sensor that provides information about the user’s steps.
- `device-usage`: A sensor that provides information about the user’s device usage.
- `messages-usage`: A sensor that provides information about the user’s Messages app usage.
- `phone-usage`: A sensor that reports the amount of time that the user is on phone calls.
- `keyboard-metrics`: A sensor that provides information about the user’s keyboard usage.
- `speech-metrics-telephony`: A sensor that provides data describing a user’s speech during phone calls.
- `speech-metrics-siri`: A sensor that provides data describing a user’s speech to Siri.
- `ambient-pressure`: A sensor that describes the pressure and temperature of the user’s environment.

#### Discussion

An app can read sensor data from devices on a per-team basis, and the system closes your app if its code signature lacks this entitlement. To attain it, submit your research study to Apple as described in [Accessing SensorKit Data](https://www.researchandcare.org/resources/accessing-sensorkit-data/). If Apple approves your study, you can create a provisioning profile that signs code with this entitlement. For more information, see [Configuring your project for sensor reading](../../SensorKit/configuring-your-project-for-sensor-reading.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sensorkit.reader.allow)*