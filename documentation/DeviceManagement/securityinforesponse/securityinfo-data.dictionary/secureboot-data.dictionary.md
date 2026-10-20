# SecurityInfoResponse.SecurityInfo.SecureBoot

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response object for the secure boot settings.

**Availability**:
- macOS 10.15+

## Declaration

```
object SecurityInfoResponse.SecurityInfo.SecureBoot
```

## Topics

### Objects
- [object SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity](./secureboot-data.dictionary/reducedsecurity-data.dictionary.md)
  Reports which security features the user disables in `recoveryOS`. This property is only present for a Mac with Apple silicon when `SecureBootLevel` is `medium`.

## Properties

- `ExternalBootLevel` (string): The device’s external boot level, which indicates whether it allows booting from an external device, disallows it, or doesn’t support it.

  **Allowed Values**: `allowed`, `disallowed`, `not supported`
- `ReducedSecurity` ([SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity]): Reports which security features the user disables in `recoveryOS`. This property is only present for a Mac with Apple silicon when `SecureBootLevel` is `medium`.

  Available: macOS 11+
- `SecureBootLevel` (string): The security level for the bootable operating system versions.

  **Allowed Values**: `off`, `medium`, `full`, `not supported`

## See Also

### Objects
- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](./firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](./firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.ManagementStatus](./managementstatus-data.dictionary.md)
  A dictionary that contains the status of the device’s MDM enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary)*