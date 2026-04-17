# MigrationAssistantSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Migration Assistant settings.

**Availability**:
- macOS 26.4+

## Declaration

```swift
object MigrationAssistantSettings
```

#### Discussion

Specify `com.apple.configuration.migration-assistant.settings` as the declaration type.

This declaration allows the device management service to configure Migration Assistant when it runs during Setup Assistant on a Mac. This makes it easy for users to do Mac-to-Mac migrations of enterprise devices when they setup a new Mac.

Configure the device to use the `AwaitingConfiguration` state after it enrolls with the server. The server needs to send the configuration and verify the configuration as both active and valid using the Declarative Device Management status, before it sends the [`DeviceConfiguredCommand`](deviceconfiguredcommand.md) command to exit that state.

The device reports Migration Assistant progress using the [`StatusMigrationAssistantState`](statusmigrationassistantstate.md) status item, and provides a report when migration completes using the [`StatusMigrationAssistantReport`](statusmigrationassistantreport.md) status item.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | macOS |
| Allowed in user scope | NA |

##### Configuration Example

This configuration provides settings for a Mac to Mac migration.

```json
{
    "Type": "com.apple.configuration.migration-assistant.settings",
    "Identifier": "F3CD2AD7-85AA-4FF3-9264-A737259FB55E",
    "ServerToken": "5AB2B98C-FCE9-4A33-88B3-ADB05F081F77",
    "Payload": {
        "ShouldDoManagedMigration": true,
        "ExcludedAccounts": [
            "admin"
        ],
        "ExcludedPaths": [
            "Documents/Personal Items/"
        ],
        "RequiredPaths": [
            "Documents/Work Items/"
        ],
        "ShouldMigrateSecurityPrivacySettings": false
    }
}
```

## Properties

- `ExcludedAccounts` ([string]): An array of strings that represent the user account short names the system excludes from migration.
- `ExcludedPaths` ([string]): An array of strings that represent files and directories relative to the user’s home directory that the system excludes from migration. Directory paths need to include a trailing “/”. For example, to exclude the “Excluded” directory in the “Documents” folder of a user’s home directory, use “Documents/Excluded/”.
- `RequiredPaths` ([string]): An array of strings that represent files and directories relative to the user’s home directory that the system needs to migrate. Directory paths need to include a trailing “/”. For example, to require the “Required” directory in the “Documents” folder of a user’s home directory, use “Documents/Required/”.
- `ShouldDoManagedMigration` (boolean) *(required)*: If `true`, the device manages Migration Assistant.
- `ShouldMigrateSecurityPrivacySettings` (boolean) *(required)*: If `true`, the system migrates Security & Privacy settings.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/migrationassistantsettings)*