# SoftwareUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure software updates.

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
object SoftwareUpdateSettings
```

#### Discussion

Specify `com.apple.configuration.softwareupdate.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | NA |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.softwareupdate.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Notifications": false,
        "Deferrals": {
            "MajorPeriodInDays": 30
        },
        "RecommendedCadence": "All",
        "AutomaticActions": {
            "Download": "AlwaysOn",
            "InstallOSUpdates": "AlwaysOn",
            "InstallSecurityUpdate": "AlwaysOn"
        },
        "RapidSecurityResponse": {
            "Enable": false
        },
        "AllowStandardUserOSUpdates": false,
        "Beta": {
            "ProgramEnrollment": "AlwaysOn"
        }
    }
}
```

## Topics

### Objects
- [object SoftwareUpdateSettingsAutomaticActionsObject](softwareupdatesettingsautomaticactionsobject.md)
  The object that configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  The object that configures overall beta program settings.
- [object SoftwareUpdateSettingsDeferralsObject](softwareupdatesettingsdeferralsobject.md)
  The object that configures update deferrals.
- [object SoftwareUpdateSettingsRapidSecurityResponseObject](softwareupdatesettingsrapidsecurityresponseobject.md)
  The object that configures Background Security Improvement settings.

## Properties

- `AllowStandardUserOSUpdates` (boolean): If set to `true`, a standard user can perform Major and Minor Software Updates. If set to `false`, only administrators can perform Major and Minor Software Updates.
- `AutomaticActions` (SoftwareUpdateSettingsAutomaticActionsObject): This object configures various automatic Software Update functionality.
- `Beta` (SoftwareUpdateSettingsBetaObject): This object configures the beta program settings for a device.
- `Deferrals` (SoftwareUpdateSettingsDeferralsObject): This object configures the deferral of software updates. Background Security Improvements aren’t considered in `Major`, `Minor`, or `System` deferral mechanism.
- `Notifications` (boolean): If set to `true`, the device shows all software update enforcement notifications. If set to `false`, the device only shows notifications triggered one hour before the enforcement deadline, and the restart countdown notification.
- `RapidSecurityResponse` (SoftwareUpdateSettingsRapidSecurityResponseObject): These configurations set user access to interacting with Background Security Improvement.
- `RecommendedCadence` (string): This string specifies how the device shows software updates to the user. When more than one update is available update, the device behaves as follows: - `All` - Shows all software update versions.
- `Oldest` - Shows only the oldest (lower numbered) software update version.
- `Newest` - Shows only the newest (highest numbered) software update version.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettings)*