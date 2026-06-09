# SoftwareUpdateSettingsRapidSecurityResponseObject

**Framework**: Device Management  
**Kind**: dictionary

These configurations set user access to interacting with Background Security Improvement.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object SoftwareUpdateSettingsRapidSecurityResponseObject
```

## Properties

- `Enable` (boolean): If set to `false`, Background Security Improvements aren’t offered for user installation. The system can still install Background Security Improvements with `com.apple.configuration.softwareupdate.enforcement.specific` configurations. If set to `true`, the system offers Background Security Improvements to the user.
- `EnableRollback` (boolean): If set to `false`, the system doesn’t offer Background Security Improvement rollbacks to the user. If set to `true`, the system offers Background Security Improvement rollbacks to the user.

## See Also

- [object SoftwareUpdateSettingsAutomaticActionsObject](softwareupdatesettingsautomaticactionsobject.md)
  This object configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  This object configures the beta program settings for a device.
- [object SoftwareUpdateSettingsDeferralsObject](softwareupdatesettingsdeferralsobject.md)
  This object configures the deferral of software updates. Background Security Improvements aren’t considered in `Major`, `Minor`, or `System` deferral mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsrapidsecurityresponseobject)*