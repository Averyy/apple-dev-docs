# SecurityInfoResponse.SecurityInfo.SecureBoot

**Framework**: Device Management  
**Kind**: dictionary

The response object for the secure boot settings.

**Availability**:
- macOS 10.15+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.SecureBoot
```

## Topics

### Objects
- [object SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary/reducedsecurity-data.dictionary.md)
  Reports which security features the user disables in `recoveryOS`. This property is only present for Apple silicon when `SecureBootLevel` is `medium`.

## See Also

- [object SecurityInfoResponse.SecurityInfo.FirewallSettings](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary.md)
  A dictionary that contains the firewall settings.
- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.ManagementStatus](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md)
  A dictionary that contains the status of the device’s MDM enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary)*