# SoftwareUpdateSettingsAutomaticActionsObject

**Framework**: Device Management  
**Kind**: dictionary

The object that configures various automatic Software Update functionality.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.4+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SoftwareUpdateSettingsAutomaticActionsObject
```

## Properties

- `Download` (string): Specifies whether the user can control automatic downloads of available updates: - `Allowed` - the user can enable or disable automatic downloads.
- `AlwaysOn` - automatic downloads are always enabled.
- `AlwaysOff` - automatic downloads are always disabled.
- `InstallOSUpdates` (string): Specifies whether the user can control automatic installation of available updates: - `Allowed` - the user can enable or disable automatic installation.
- `AlwaysOn` - automatic installations are always enabled.
- `AlwaysOff` - automatic installations are always disabled.
- `InstallSecurityUpdate` (string): Specifies whether the user can control automatic installation of available security updates: - `Allowed` - the user can enable or disable automatic installation.
- `AlwaysOn` - automatic installations are always enabled.
- `AlwaysOff` - automatic installations are always disabled.

## See Also

- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  The object that configures overall beta program settings.
- [object SoftwareUpdateSettingsDeferralsObject](softwareupdatesettingsdeferralsobject.md)
  The object that configures update deferrals.
- [object SoftwareUpdateSettingsRapidSecurityResponseObject](softwareupdatesettingsrapidsecurityresponseobject.md)
  The object that configures Background Security Improvement settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsautomaticactionsobject)*