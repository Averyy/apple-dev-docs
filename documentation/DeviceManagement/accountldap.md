# AccountLDAP

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountLDAP
```

#### Discussion

Specify `com.apple.configuration.account.ldap` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.account.ldap",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Work Directory",
        "HostName": "ldap.example.com",
        "SearchSettings": [
            {
                "VisibleName": "Search Work",
                "SearchBase": "dc=example,dc=com",
                "Scope": "Subtree"
            }
        ]
    }
}
```

## Topics

### Objects
- [object AccountLDAPSearchSettingsItemObject](accountldapsearchsettingsitemobject.md)
  The settings for configuring the search behavior with an LDAP server.

## Properties

- `AuthenticationCredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials for this account. Set the corresponding asset type to `CredentialUserNameAndPassword`.
- `HostName` (string) *(required)*: The hostname or IP address of the LDAP server.
- `Port` (integer): The port number or IP address of the LDAP server.
- `SearchSettings` ([AccountLDAPSearchSettingsItemObject]): The array of nodes to start LDAP searches from. There must be at least one node for this account to be useful. macOS only searches one node and ignores other items in the array.
- `VisibleName` (string): The name that apps show to the user for this LDAP account. If not present, the system generates a suitable default.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
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
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountldap)*