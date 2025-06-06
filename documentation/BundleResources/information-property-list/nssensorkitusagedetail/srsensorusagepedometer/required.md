# Required

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app’s study relies on this sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

The system checks the value for this property when the user declines the access prompt for this sensor. If you set the value of this property to `true`, the system forgoes installing your app. If `false`, the system withholds the sensor’s data but installs your app assuming your study can continue at a limited capacity without the sensor’s data.

## See Also

- [Description](information-property-list/nssensorkitusagedetail/srsensorusagepedometer/description.md)
  An explanatory string that details the manner in which your study uses the sensor’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail/srsensorusagepedometer/required)*