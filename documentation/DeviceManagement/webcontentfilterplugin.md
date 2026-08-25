# WebContentFilterPlugin

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a WebContent Filter that uses a plugin.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object WebContentFilterPlugin
```

#### Discussion

Specify `com.apple.configuration.webcontent-filter.plugin` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up a web content filter using a Network Extension plugin bundle.

```json
{
    "Type": "com.apple.configuration.webcontent-filter.plugin",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Content Filter",
        "PluginBundleID": "com.example.contentfilter",
        "ServerAddress": "filter.example.com",
        "ContentFilterUUID": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890"
    }
}
```

## Topics

### Objects
- [object WebContentFilterPluginAuthenticationObject](webcontentfilterpluginauthenticationobject.md)
  Settings that control authentication.
- [object WebContentFilterPluginFilterObject](webcontentfilterpluginfilterobject.md)
  Settings that control authentication.
- [object WebContentFilterPluginVendorConfigObject](webcontentfilterpluginvendorconfigobject.md)
  The custom dictionary that the filtering service plug-in needs.

## Properties

- `Authentication` (WebContentFilterPluginAuthenticationObject): Settings that control authentication.
- `ContentFilterUUID` (string): A globally unique identifier for this content filter configuration. The content filter processes network traffic for managed apps with the same `ContentFilterUUID` in their app attributes. This key must be present for unsupervised devices and user enrollment. Available: iOS 27+ | iPadOS 27+ | visionOS 27+
- `Filter` (WebContentFilterPluginFilterObject): Settings that control authentication.
- `Organization` (string): The organization string to pass to the third-party plug-in.
- `PluginBundleID` (string) *(required)*: The bundle ID of the plug-in that provides filtering service. Consult your filtering solution vendor to determine what to specify for this value.
- `ServerAddress` (string): The server address, which may be the IP address, hostname, or URL.
- `VendorConfig` (WebContentFilterPluginVendorConfigObject): The custom dictionary that the filtering service plug-in needs.
- `VisibleName` (string) *(required)*: The name of the web content filter that the system displays on the device.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilterplugin)*