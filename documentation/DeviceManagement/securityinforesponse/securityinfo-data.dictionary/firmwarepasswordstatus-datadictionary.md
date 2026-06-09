# SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the status of the EFI firmware password.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus
```

## Properties

- `AllowOroms` (boolean): If `true`, enable ROMs.
- `ChangePending` (boolean): If `true`, a firmware password change is pending. A device restart is necessary for this change to take effect. Until then, additional attempts to change the password fail. > **Note**:  If `true`, the other values show the current state of the device, not the state after a restart.
- `PasswordExists` (boolean): If `true`, the device has an EFI firmware password.

## See Also

- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.ManagementStatus](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md)
  A dictionary that contains the status of the device’s MDM enrollment.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary.md)
  The response object for the secure boot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary)*