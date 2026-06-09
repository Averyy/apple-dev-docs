# NetworkDNSProxy

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure DNS proxy settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkDNSProxy
```

#### Discussion

Specify `com.apple.configuration.network.dns-proxy` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | macOS |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up a DNS proxy using a Network Extension app.

```json
{
    "Type": "com.apple.configuration.network.dns-proxy",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "DNS Proxy",
        "AppBundleIdentifier": "com.example.mydnsproxyapp",
        "ProviderComposedIdentifier": "com.example.mydnsproxyapp.mydnsproxyprovider",
        "ProviderConfiguration": {
            "resolver": {
                "ipaddress": "9.9.9.9"
            }
        }
    }
}
```

## Topics

### Objects
- [object NetworkDNSProxyProviderConfigurationObject](networkdnsproxyproviderconfigurationobject.md)
  The dictionary of vendor-specific configuration items.

## Properties

- `AppBundleIdentifier` (string) *(required)*: The bundle identifier of the app containing the DNS proxy network extension.
- `DNSProxyUUID` (string): A globally unique identifier for this DNS proxy configuration. The proxy processes DNS lookups traffic for managed apps with the same `DNSProxyUUID` in their app attributes. This key is required for user enrollment. Available: iOS 27+ | iPadOS 27+ | visionOS 27+
- `ProviderComposedIdentifier` (string): The identifier of the provider to use for this configuration. Useful for apps that contain more than one DNS proxy extension. In iOS and visionOS, the identifier is a bundle ID, for example, “com.example.app”. In macOS, the identifier is a composed identifier. The format of the composed identifier is either “Bundle-ID” or “Bundle-ID {Designated-Requirement}”. “Bundle-ID” is the bundle identifier string of the provider. “Designated-Requirement” is the designated requirement string from the code signature of the provider. For example, “com.example.app” for the bundle ID format, or “com.example.app {anchor apple generic}” for the designated requirement format.
- `ProviderConfiguration` (NetworkDNSProxyProviderConfigurationObject): The dictionary of vendor-specific configuration items.
- `VisibleName` (string) *(required)*: The name of the DNS proxy configuration that the system displays on the device.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkdnsproxy)*