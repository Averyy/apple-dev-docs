# NetworkDNSSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure encrypted DNS settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkDNSSettings
```

#### Discussion

Specify `com.apple.configuration.network.dns-settings` as the declaration type.

The following rules determine which networks the settings apply to:

- For supervised enrollments, the settings apply to all networks.
- For device enrollments, the settings are limited to only managed networks.
- For local installs, the settings apply to all networks.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up encrypted DNS using DNS-over-HTTPS.

```json
{
    "Type": "com.apple.configuration.network.dns-settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "DNS Settings",
        "DNSSettings": {
            "DNSProtocol": "HTTPS",
            "ServerURL": "https://dns.example.com/dns-query",
            "ServerAddresses": [
                "12.12.12.12"
            ],
            "AllowFailover": false,
            "SupplementalMatchDomains": [
                "example.com"
            ]
        }
    }
}
```

## Topics

### Objects
- [object NetworkDNSSettingsDNSSettingsObject](networkdnssettingsdnssettingsobject.md)
  A dictionary that defines a configuration for an encrypted DNS server.
- [object NetworkDNSSettingsOnDemandRulesElementObject](networkdnssettingsondemandruleselementobject.md)
  An array of rules that define the DNS settings. If not set, the system always applies the DNS settings. These rules are identical to the `OnDemandRules` array in VPN payloads.

## Properties

- `DNSSettings` (NetworkDNSSettingsDNSSettingsObject) *(required)*: A dictionary that defines a configuration for an encrypted DNS server.
- `OnDemandRules` ([NetworkDNSSettingsOnDemandRulesElementObject]): An array of rules that define the DNS settings. If not set, the system always applies the DNS settings. These rules are identical to the `OnDemandRules` array in VPN payloads.
- `ProhibitDisablement` (boolean): If `true`, the system prohibits users from disabling DNS settings. Allowed enrollments: supervised
- `VisibleName` (string) *(required)*: The name of the DNS settings that the system displays on the device.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkdnssettings)*