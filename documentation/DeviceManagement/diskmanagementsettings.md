# DiskManagementSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure disk management settings on the device.

**Availability**:
- macOS 15.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DiskManagementSettings
```

#### Discussion

Specify `com.apple.configuration.diskmanagement.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | NA |

##### Configuration Example

This configuration prevents the use of external and network storage devices.

```json
{
    "Type": "com.apple.configuration.diskmanagement.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Restrictions": {
            "ExternalStorage": "Disallowed",
            "NetworkStorage": "Disallowed"
        }
    }
}
```

## Topics

### Objects
- [object DiskManagementSettingsRestrictionsObject](diskmanagementsettingsrestrictionsobject.md)
  The restrictions for the disk.

## Properties

- `Restrictions` (DiskManagementSettingsRestrictionsObject): The restrictions for the disk.

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
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/diskmanagementsettings)*