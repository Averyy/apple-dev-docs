# com.apple.developer.automated-device-enrollment.add-devices

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether an app may add a device to Automated Device Enrollment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Details

- **Name**: `com.apple.developer.automated-device-enrollment.add-devices`
- **Type**: boolean

## Discussion

Use [`automatedDeviceEnrollmentAddition(isPresented:)`](../../SwiftUI/view/automateddeviceenrollmentaddition%28ispresented%29.md) to present a UI that allows users to add devices to their organization. To obtain permission for this entitlement, see [Automated Device Enrollment Entitlement Request](https://developer.apple.com/contact/request/automated-device-enrollment/).

## See Also

### Device Management
- [Enrollment Single Sign On](./com.apple.developer.enrollment-sso-capable.md)
  An entitlement that indicates the app participates in single sign-on (SSO) during enrollment into device management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.automated-device-enrollment.add-devices)*