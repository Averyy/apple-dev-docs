# SecurityInfoResponse.SecurityInfo.ManagementStatus

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the status of the device’s MDM enrollment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.13.2+
- tvOS 13.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.ManagementStatus
```

## Properties

- `EnrolledViaDEP` (boolean): If `true`, the device enrolled in MDM through Automated Device Enrollment (ADE). Available: macOS 10.13.2+
- `IsActivationLockManageable` (boolean): If `true`, the type of enrollment allows the MDM to manage Activation Lock for this device. Available: macOS 10.15+
- `IsUserEnrollment` (boolean): If `true`, the device is user-enrolled. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | tvOS 13+ | visionOS 1.1+ | watchOS 10+
- `UserApprovedEnrollment` (boolean): If `true`, the enrollment was user-approved. If `false`, the device may reject certain security-sensitive payloads or commands. Available: macOS 10.13.2+

## See Also

- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary.md)
  The response object for the secure boot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary)*