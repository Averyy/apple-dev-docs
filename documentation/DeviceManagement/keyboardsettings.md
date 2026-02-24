# KeyboardSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure keyboard settings.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- macOS 26.4+ (Beta)

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
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, macOS |
| Allowed in user scope | macOS, Shared iPad |

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

- `AllowAutoCorrection` (boolean): If `false`, disables auto-correction.
- `AllowDefinitionLookup` (boolean): If `false`, disables definition lookup.
- `AllowDictation` (boolean): If `false`, disables dictation.
- `AllowMathKeyboardSuggestions` (boolean): If `false`, disables keyboard suggestions that include math solutions. This key is also supported by the math.settings configuration.
- `AllowPredictiveText` (boolean): If `false`, disables predictive text.
- `AllowSlideToType` (boolean): If `false`, disables slide to type.
- `AllowSpellCheck` (boolean): If `false`, disables spell check.
- `AllowTextReplacement` (boolean): If `false`, disables text replacement.

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
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/keyboardsettings)*