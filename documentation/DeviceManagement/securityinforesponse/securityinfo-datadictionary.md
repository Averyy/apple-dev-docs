# SecurityInfoResponse.SecurityInfo

**Framework**: Devicemanagement  
**Kind**: dictionary

A dictionary that contains security-related information.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo
```

#### Overview

> **Note**: For a device to have data protection, `HardwareEncryptionCaps` must be `3` and `PasscodePresent` must `true`.

```None
This value is available in iOS 4 and later, and tvOS 6 and later.
```

- IsRecoveryLockEnabled: If `true`, a password is required to enter recovery (see [`SetRecoveryLockCommand`](setrecoverylockcommand.md)). Available in macOS 11.5 and later and only on Apple silicon devices.
- ManagementStatus: A dictionary that contains the status of the device’s MDM enrollment.
- PasscodeCompliant: If `true`, the user’s passcode is compliant with all requirements on the device, including Exchange and other accounts. This value is available in iOS 4 and later, and tvOS 6 and later.
- PasscodeCompliantWithProfiles: If `true`, the user’s passcode is compliant with requirements from profiles. This key doesn’t apply to User-Enrolled devices. This value is available in iOS 4 and later, and tvOS 6 and later.
- PasscodeLockGracePeriod: The user preference for the number of seconds before a locked screen requires the device passcode to unlock it. This value is only available for Shared iPad.
- PasscodeLockGracePeriodEnforced: The enforced value for the number of seconds before a locked screen requires the device passcode to unlock it. If a device has a passcode, changing `PasscodeLockGracePeriod` to a larger value doesn’t take effect until the user logs out or removes the passcode. This value is only available for Shared iPad.
- PasscodePresent: If `true`, the device has a passcode. This key doesn’t apply to User-Enrolled devices. This value is available in iOS 4 and later, and tvOS 6 and later.
- RemoteDesktopEnabled: If `true`, Remote Desktop is active on the device. This value is available in macOS 10.14.4 and later.
- SystemIntegrityProtectionEnabled: If `true`, System Integrity Protection (SIP) is active on the device. This value is available in macOS 10.12 and later.
- SecureBoot: A dictionary that contains the device’s Secure Boot settings. This value is available in macOS 10.15 and later.

## Topics

### Commands
- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.ManagementStatus](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md)
  A dictionary that contains the status of the device’s MDM enrollment.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary.md)
  The response object for the secure boot settings.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary/reducedsecurity-data.dictionary.md)
  A dictionary that contains the device’s reduced security settings.

## See Also

- [object SecurityInfoResponse.ErrorChainItem](securityinforesponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary)*