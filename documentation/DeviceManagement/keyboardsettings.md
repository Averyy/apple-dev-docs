# KeyboardSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure keyboard settings.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
object KeyboardSettings
```

#### Discussion

Specify `com.apple.configuration.keyboard.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

This configuration restricts keyboard features.

```json
{
    "Type": "com.apple.configuration.keyboard.settings",
    "Identifier": "A1B2C3D4-E5F6-4A5B-9C8D-7E6F5A4B3C2D",
    "ServerToken": "F1E2D3C4-B5A6-4D5E-8F9A-0B1C2D3E4F5A",
    "Payload": {
        "AllowAutoCorrection": false,
        "AllowSlideToType": false,
        "AllowDefinitionLookup": false,
        "AllowDictation": false,
        "AllowMathKeyboardSuggestions": false,
        "AllowPredictiveText": false,
        "AllowTextReplacement": false,
        "AllowSpellCheck": false
    }
}
```

## Properties

- `AllowAutoCorrection` (boolean): If `false`, disables auto-correction. Available: iOS 26.4+ | iPadOS 26.4+
- `AllowDefinitionLookup` (boolean): If `false`, disables definition lookup.
- `AllowDictation` (boolean): If `false`, disables dictation.
- `AllowMathKeyboardSuggestions` (boolean): If `false`, disables keyboard suggestions that include math solutions. This key is also supported by the math.settings configuration.
- `AllowPredictiveText` (boolean): If `false`, disables predictive text. Available: iOS 26.4+ | iPadOS 26.4+
- `AllowSlideToType` (boolean): If `false`, disables slide to type. Available: iOS 26.4+ | iPadOS 26.4+
- `AllowSpellCheck` (boolean): If `false`, disables spell check. Available: iOS 26.4+ | iPadOS 26.4+
- `AllowTextReplacement` (boolean): If `false`, disables text replacement. Available: iOS 26.4+ | iPadOS 26.4+

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/keyboardsettings)*