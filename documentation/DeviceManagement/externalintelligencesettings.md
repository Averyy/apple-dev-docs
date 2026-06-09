# ExternalIntelligenceSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure External Intelligence Integrations settings.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
object ExternalIntelligenceSettings
```

#### Discussion

Specify `com.apple.configuration.external-intelligence.settings` as the declaration type.

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

##### Configuration Examples

This configuration restricts external intelligence integrations.

```json
{
    "Type": "com.apple.configuration.external-intelligence.settings",
    "Identifier": "A1B2C3D4-E5F6-4A5B-9C8D-7E6F5A4B3C2D",
    "ServerToken": "F1E2D3C4-B5A6-4D5E-8F9A-0B1C2D3E4F5A",
    "Payload": {
        "Enabled": false,
        "AllowSignIn": false,
        "AllowedWorkspaceIDs": [
            "ABCDEFGH"
        ]
    }
}
```

## Properties

- `AllowedWorkspaceIDs` ([string]): An array of strings, but currently restricted to a single element. If present, Apple Intelligence allows use of only the given external integration workspace ID, and requires a sign-in to make requests. The user is required to sign in to integrations that support signing in. Multiple values combine using an intersect operation.
- `AllowSignIn` (boolean): If `false`, disables sign-in for external intelligence integrations.
- `Enabled` (boolean): If `false`, disables external intelligence integrations.

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
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/externalintelligencesettings)*