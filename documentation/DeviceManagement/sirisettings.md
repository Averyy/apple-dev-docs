# SiriSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Siri settings.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 27.0+ (Beta)
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
object SiriSettings
```

#### Discussion

Specify `com.apple.configuration.siri.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

This configuration restricts Siri features.

```json
{
    "Type": "com.apple.configuration.siri.settings",
    "Identifier": "A1B2C3D4-E5F6-4A5B-9C8D-7E6F5A4B3C2D",
    "ServerToken": "F1E2D3C4-B5A6-4D5E-8F9A-0B1C2D3E4F5A",
    "Payload": {
        "Enabled": false,
        "AllowUserGeneratedContent": false,
        "AllowWhileLocked": false,
        "ForceProfanityFilter": true
    }
}
```

## Properties

- `AllowUserGeneratedContent` (boolean): If `false`, disables Siri user-generated content. Available: iOS 26.4+ | iPadOS 26.4+ | watchOS 26.4+
- `AllowWhileLocked` (boolean): If `false`, disables Siri while locked. Available: iOS 26.4+ | iPadOS 26.4+ | watchOS 26.4+
- `Enabled` (boolean): If `false`, disables Siri. Available: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+ | tvOS 27+ | visionOS 26.4+
- `ForceProfanityFilter` (boolean): If `true`, forces Siri profanity filter. Available: iOS 26.4+ | iPadOS 26.4+ | macOS 26.4+

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/sirisettings)*