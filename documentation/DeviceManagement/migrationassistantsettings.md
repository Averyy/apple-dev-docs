# MigrationAssistantSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Migration Assistant settings.

**Availability**:
- macOS 26.4+ (Beta)

## Declaration

```swift
object MigrationAssistantSettings
```

#### Discussion

Specify `com.apple.configuration.migration-assistant.settings` as the declaration type.

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
            "Documents/Personal Items"
        ],
        "RequiredPaths": [
            "Documents/Work Items"
        ],
        "ShouldMigrateSecurityPrivacySettings": false
    }
}
```

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