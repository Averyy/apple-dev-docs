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

## Declaration

```swift
object SoftwareUpdateSettings
```

## Mentions

- [Deploying software updates using declarative management](deploying-software-updates-using-declarative-management.md)
- [Enrolling a device in a beta program](enrolling-a-device-in-a-beta-program.md)

#### Discussion

Specify `com.apple.configuration.softwareupdate.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Example

This configuration manages software update behavior and deferral settings.

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
  This object configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  This object configures the beta program settings for a device.
- [object SoftwareUpdateSettingsDeferralsObject](softwareupdatesettingsdeferralsobject.md)
  This object configures the deferral of software updates. Background Security Improvements aren’t considered in `Major`, `Minor`, or `System` deferral mechanism.
- [object SoftwareUpdateSettingsRapidSecurityResponseObject](softwareupdatesettingsrapidsecurityresponseobject.md)
  These configurations set user access to interacting with Background Security Improvement.

## Properties

- `AllowStandardUserOSUpdates` (boolean): If set to `true`, a standard user can perform Major and Minor Software Updates. If set to `false`, only administrators can perform Major and Minor Software Updates. Available: macOS 15+
- `AutomaticActions` (SoftwareUpdateSettingsAutomaticActionsObject): This object configures various automatic Software Update functionality. Allowed enrollments: supervised
- `Beta` (SoftwareUpdateSettingsBetaObject): This object configures the beta program settings for a device. Available: iOS 18+ | iPadOS 18+ | macOS 15.4+
- `Deferrals` (SoftwareUpdateSettingsDeferralsObject): This object configures the deferral of software updates. Background Security Improvements aren’t considered in `Major`, `Minor`, or `System` deferral mechanism. Allowed enrollments: supervised
- `Notifications` (boolean): If set to `true`, the device shows all software update enforcement notifications. If set to `false`, the device only shows notifications triggered one hour before the enforcement deadline, and the restart countdown notification.
- `RapidSecurityResponse` (SoftwareUpdateSettingsRapidSecurityResponseObject): These configurations set user access to interacting with Background Security Improvement. Available: iOS 18+ | iPadOS 18+ | macOS 15+
Allowed enrollments: supervised
- `RecommendedCadence` (string): This string specifies how the device shows software updates to the user. When more than one update is available update, the device behaves as follows: - `All` - Shows all software update versions.
- `Oldest` - Shows only the oldest (lower numbered) software update version.
- `Newest` - Shows only the newest (highest numbered) software update version. Available: iOS 18+ | iPadOS 18+ | visionOS 26+

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
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettings)*