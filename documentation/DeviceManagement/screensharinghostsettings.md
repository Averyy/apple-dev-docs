# ScreenSharingHostSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure screen-sharing host settings and restrictions.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object ScreenSharingHostSettings
```

#### Discussion

Specify `com.apple.configuration.screensharing.host.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |
| Apply | Only a single configuration is applied |

##### Configuration Example

This configuration manages screen-sharing host settings and restrictions.

```json
{
    "Type": "com.apple.configuration.screensharing.host.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "MaximumVirtualDisplays": 1,
        "PortBase": 1100,
        "PreventCopyFilesFromHost": true,
        "PreventCopyFilesToHost": true,
        "PreventHighPerformanceConnections": true
    }
}
```

## Properties

- `MaximumVirtualDisplays` (integer): The maximum number of virtual displays to make available to clients.
- `PortBase` (integer): The initial UDP port number to connect to the host. Screen sharing requires multiple connections, so the system increments this value by 1 for each additional connection. This doesn’t change the port number that the system uses to initially establish a connection with a host, which is always TCP port 5900.
- `PreventCopyFilesFromHost` (boolean): If `true`, the system prevents users from copying files from the screen-sharing host.
- `PreventCopyFilesToHost` (boolean): If `true`, the system prevents users from copying files to the screen-sharing host.
- `PreventHighPerformanceConnections` (boolean): If `true`, the system prevents clients from establishing high-performance connections to the host.

## See Also

- [object AccessibilitySettings](accessibilitysettings.md)
  The declaration to configure accessibility settings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharinghostsettings)*