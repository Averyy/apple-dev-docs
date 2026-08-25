# IntelligenceSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Apple Intelligence settings.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
object IntelligenceSettings
```

#### Discussion

Specify `com.apple.configuration.intelligence.settings` as the declaration type.

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

This configuration restricts several Apple Intelligence features.

```json
{
    "Type": "com.apple.configuration.intelligence.settings",
    "Identifier": "A1B2C3D4-E5F6-4A5B-9C8D-7E6F5A4B3C2D",
    "ServerToken": "F1E2D3C4-B5A6-4D5E-8F9A-0B1C2D3E4F5A",
    "Payload": {
        "AllowAppleIntelligenceReport": false,
        "AllowGenmoji": false,
        "AllowImagePlayground": false,
        "AllowImageWand": false,
        "Apps": {
            "Mail": {
                "AllowSmartReplies": false,
                "AllowSummary": false
            },
            "Notes": {
                "AllowTranscription": false,
                "AllowTranscriptionSummary": false
            },
            "Safari": {
                "AllowSummary": false
            }
        },
        "AllowPersonalizedHandwritingResults": false,
        "AllowVisualIntelligenceSummary": false,
        "AllowWritingTools": false,
        "ForceOnDeviceOnlyDictation": true,
        "ForceOnDeviceOnlyTranslation": true
    }
}
```

## Topics

### Objects
- [object IntelligenceSettingsAppsObject](intelligencesettingsappsobject.md)
  If present, configures app-specific Intelligence features.

## Properties

- `AllowAppleIntelligenceReport` (boolean): If `false`, disables Apple Intelligence Report.
- `AllowGenmoji` (boolean): If `false`, disables Genmoji.
- `AllowImagePlayground` (boolean): If `false`, disables Image Playground.
- `AllowImageWand` (boolean): If `false`, disables Image Wand. Available: iOS 26.4+ | iPadOS 26.4+ | visionOS 26.4+
- `AllowPersonalizedHandwritingResults` (boolean): If `false`, disables Personalized Handwriting Results. Available: iOS 26.4+ | iPadOS 26.4+
- `AllowVisualIntelligence` (boolean): If `false`, disables Visual Intelligence. Available: iOS 27+ | iPadOS 27+ | macOS 27+
- `AllowVisualIntelligenceSummary` (boolean): If `false`, disables Visual Intelligence Summary. Deprecated: use the `AllowVisualIntelligence` key. Available: iOS 26.4+ | iPadOS 26.4+
Deprecated: iOS 27+ | iPadOS 27+
- `AllowWritingTools` (boolean): If `false`, disables Writing Tools.
- `Apps` (IntelligenceSettingsAppsObject): If present, configures app-specific Intelligence features.
- `ForceOnDeviceOnlyDictation` (boolean): If `true`, forces On-Device Only Dictation.
- `ForceOnDeviceOnlyTranslation` (boolean): If `true`, forces On-Device Only Translation. Available: iOS 26.4+ | iPadOS 26.4+

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/intelligencesettings)*