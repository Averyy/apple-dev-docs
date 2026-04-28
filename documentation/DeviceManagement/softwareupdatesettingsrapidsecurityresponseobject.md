# SoftwareUpdateSettingsRapidSecurityResponseObject

**Framework**: Device Management  
**Kind**: dictionary

The object that configures Background Security Improvement settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SoftwareUpdateSettingsRapidSecurityResponseObject
```

## Properties

- `Enable` (boolean): If set to `false`, Background Security Improvements aren’t offered for user installation. The system can still install Background Security Improvements with `com.apple.configuration.softwareupdate.enforcement.specific` configurations. If set to `true`, the system offers Background Security Improvements to the user.
- `EnableRollback` (boolean): If set to `false`, the system doesn’t offer Background Security Improvement rollbacks to the user. If set to `true`, the system offers Background Security Improvement rollbacks to the user.

## See Also

- [object SoftwareUpdateSettingsAutomaticActionsObject](softwareupdatesettingsautomaticactionsobject.md)
  The object that configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  The object that configures overall beta program settings.
- [object SoftwareUpdateSettingsDeferralsObject](softwareupdatesettingsdeferralsobject.md)
  The object that configures update deferrals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsrapidsecurityresponseobject)*