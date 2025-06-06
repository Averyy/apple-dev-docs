# Automated Device Enrollment

**Framework**: Automated Device Enrollment  
**Kind**: module

Allow users of third-party MDM apps to add macOS and iOS devices to their organization.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

#### Overview

This framework provides a user interface for device administrators to add macOS, iOS, and iPadOS devices to their Apple School Manager, Apple Business Manager, and Apple Business Essentials organizations. The provided SwiftUI view allows a user with device enrollment privileges to sign in with their Managed Apple ID and add devices to their organization.

This feature requires Bluetooth access to discover and pair with nearby devices, and camera access to scan visual pairing PIN codes. To use this feature, you must have the Automated Device Enrollment entitlement. To obtain permission for this entitlement, see [`Automated Device Enrollment Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/automated-device-enrollment/).

## Topics

### Essentials
- [@MainActor @preconcurrency func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View
](../SwiftUI/View/automatedDeviceEnrollmentAddition(isPresented:).md)
  Presents a modal view that enables users to add devices to their organization.
- [com.apple.developer.automated-device-enrollment.add-devices](../BundleResources/Entitlements/com.apple.developer.automated-device-enrollment.add-devices.md)
  A Boolean value that indicates whether an app may add a device to Automated Device Enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AutomatedDeviceEnrollment)*