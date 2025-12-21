# Downlink time difference of arrival ranging

**Framework**: Nearby Interaction

Use anchor devices to improve the accuracy of indoor positioning.

#### Overview

Downlink Time-Difference-of-Arrival (DL-DTOA) is a system that allows the Nearby Interaction framework to interact with fixed Ultra-wide band (UWB) devices — known as  — in an indoor space to increase the accuracy of positioning by measuring the time difference of arrival of signals from multiple anchors to an iOS device.

#### Add the Entitlement to Your App

To use DL-DTOA, the system requires your app to have the `com.apple.developer.nearbyinteraction.dltdoa` entitlement with a value of `true`. Add this entitlement by enabling the Nearby Interaction DL-TDoA capability on your app’s target in Xcode. For more information, see  [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app) to your app.

> **Note**: The Nearby Interaction DL-TDoA entitlement only supports development builds and Ad Hoc testing. App Store submission and Test Flight for apps using this capability isn’t currently available.

## Topics

### Configuration
- [class NIDLTDOAConfiguration](nidltdoaconfiguration.md)
  A configuration that enables Downlink Time-Difference-of-Arrival ranging.
### Measurements
- [class NIDLTDOAMeasurement](nidltdoameasurement.md)
  Information from a Downlink Time-Difference-of-Arrival anchor that you use to derive a range estimate.
- [enum NIDLTDOACoordinatesType](nidltdoacoordinatestype.md)
  The possible coordinate types for Downlink Time-Difference-of-Arrival measurement updates.
- [enum NIDLTDOAMeasurementType](nidltdoameasurementtype.md)
  The possible phases of downlink positioning signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/dl-tdoa-ranging)*