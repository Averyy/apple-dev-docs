# SecurityInfoResponse.SecurityInfo.ManagementStatus

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the status of the device’s MDM enrollment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.13.2+
- tvOS 13.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.ManagementStatus
```

## Properties

- `EnrolledViaDEP` (boolean): If `true`, the device enrolled in MDM through the Device Enrollment Program (DEP). This value is available in macOS 10.13.2 and later.
- `IsActivationLockManageable` (boolean): If `true`, the type of enrollment allows the MDM to manage Activation Lock for this device. This value is available in macOS 10.15 and later.
- `IsUserEnrollment` (boolean): If `true`, the device is user-enrolled. This value is available in iOS 13 and later, and macOS 10.15 and later.
- `UserApprovedEnrollment` (boolean): If `true`, the enrollment was user-approved. If `false`, the device may reject certain security-sensitive payloads or commands. This value is available in macOS 10.13.2 and later.

## See Also

- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary.md)
  The response object for the secure boot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary)*