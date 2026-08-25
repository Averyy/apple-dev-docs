# AccessibilitySettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure accessibility settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object AccessibilitySettings
```

#### Discussion

Specify `com.apple.configuration.accessibility.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, visionOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, visionOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Example

This configuration prevents the use of Live Recognition.

```json
{
    "Type": "com.apple.configuration.accessibility.settings",
    "Identifier": "119D31F8-E3A2-454A-A019-FD3F05A008D3",
    "ServerToken": "DC31F056-0ADE-4D01-8E63-A7CA093EC7CD",
    "Payload": {
        "Vision": {
            "AllowLiveRecognition": false
        }
    }
}
```

## Topics

### Objects
- [object AccessibilitySettingsVisionObject](accessibilitysettingsvisionobject.md)
  If present, configures vision accessibility settings.

## Properties

- `Vision` (AccessibilitySettingsVisionObject): If present, configures vision accessibility settings.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accessibilitysettings)*