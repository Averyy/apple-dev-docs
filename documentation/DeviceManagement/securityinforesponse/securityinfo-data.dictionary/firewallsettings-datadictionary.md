# SecurityInfoResponse.SecurityInfo.FirewallSettings

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the firewall settings.

**Availability**:
- macOS 10.12+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.FirewallSettings
```

## Topics

### Objects
- [object SecurityInfoResponse.SecurityInfo.FirewallSettings.ApplicationsItem](securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary/applicationsitem.md)
  A dictionary that describes the allowed apps.

## Properties

- `Applications` ([SecurityInfoResponse.SecurityInfo.FirewallSettings.ApplicationsItem]): An array of dictionaries that describes the allowed applications.
- `BlockAllIncoming` (boolean): If `true`, the firewall blocks all incoming connections.
- `FirewallEnabled` (boolean): If `true`, the firewall is on.
- `LoggingEnabled` (boolean): If `true`, logging is enabled. Available: macOS 12+
- `LoggingOption` (string): The type of logging emitted by the firewall. Available: macOS 12+
- `StealthMode` (boolean): If true, stealth mode is active for the firewall.

## See Also

- [object SecurityInfoResponse.SecurityInfo.FirmwarePasswordStatus](securityinforesponse/securityinfo-data.dictionary/firmwarepasswordstatus-data.dictionary.md)
  A dictionary that contains the status of the EFI firmware password.
- [object SecurityInfoResponse.SecurityInfo.ManagementStatus](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md)
  A dictionary that contains the status of the device’s MDM enrollment.
- [object SecurityInfoResponse.SecurityInfo.SecureBoot](securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary.md)
  The response object for the secure boot settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary)*