# ScreenSharingConnection

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a connection to a screen-sharing host.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object ScreenSharingConnection
```

#### Discussion

Specify `com.apple.configuration.screensharing.connection` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | macOS |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up a screen-sharing connection to a remote Mac.

```json
{
    "Type": "com.apple.configuration.screensharing.connection",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ConnectionUUID": "FA80E209-B31B-4862-B880-399F79E8FC35",
        "HostName": "example.com",
        "DisplayName": "Host1",
        "DisplayConfiguration": {
            "DisplayType": "Virtual1"
        }
    }
}
```

## Topics

### Objects
- [object ScreenSharingConnectionDisplayConfigurationObject](screensharingconnectiondisplayconfigurationobject.md)
  The display configuration for this connection.

## Properties

- `AuthenticationCredentialsAssetReference` (string): The identifier of an asset declaration that contains the required credentials for this connection to authenticate with the screen-sharing server. Set the corresponding asset type to `com.apple.asset.credential.userpassword`.
- `ConnectionUUID` (string) *(required)*: A unique identifier for this connection when it’s in a connection group.
- `DisplayConfiguration` (ScreenSharingConnectionDisplayConfigurationObject) *(required)*: The display configuration for this connection.
- `DisplayName` (string) *(required)*: The name of the connection.
- `HostName` (string) *(required)*: The host name or IP address of the Mac that hosts the screen-sharing connection.
- `Port` (integer): The TCP port number on the host to initiate the connection.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharingconnection)*