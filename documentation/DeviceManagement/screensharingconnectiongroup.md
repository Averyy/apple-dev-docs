# ScreenSharingConnectionGroup

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a group of screen-sharing connections.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScreenSharingConnectionGroup
```

#### Discussion

Specify `com.apple.configuration.screensharing.connection.group` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | macOS |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | macOS |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.screensharing.connection.group",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ConnectionGroupUUID": "4BF32552-6F85-4F67-999B-7B2494C4DD99",
        "GroupName": "Lab Devices",
        "Members": [
            "7F8F28A5-C024-470B-8166-EC6669A12C3A",
            "EDF04C7F-F9B0-4204-A5EE-34AE094CA7BB"
        ]
    }
}
```

## Properties

- `ConnectionGroupUUID` (string) *(required)*: A unique identifier for this connection group.
- `GroupName` (string) *(required)*: The name of the connection group.
- `Members` ([string]) *(required)*: An array of `ConnectionUUID`s that represent connections declared in `ScreenSharingConnection` configurations that are members of this group.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharingconnectiongroup)*