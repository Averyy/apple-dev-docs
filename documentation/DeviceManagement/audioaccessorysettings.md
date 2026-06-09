# AudioAccessorySettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure audio accessory settings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
object AudioAccessorySettings
```

#### Discussion

Specify `com.apple.configuration.audio-accessory.settings` as the declaration type.

Setting `TemporaryPairing` to `false` disables only the temporary pairing feature, without impacting any other use of audio accessories, so users can still:

- Pair and use audio accessories - the device records the pairing and synchronizes it to their iCloud account.
- Use the audio accessory AirPods Sharing feature.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, Shared iPad |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Example

This configuration enables temporary pairing and sets an unpairing time of 6 pm.

```json
{
    "Type": "com.apple.configuration.audio-accessory.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "TemporaryPairing": {
            "Configuration": {
                "UnpairingTime": {
                    "Policy": "Hour",
                    "Hour": 18
                }
            }
        }
    }
}
```

## Topics

### Objects
- [object AudioAccessorySettingsTemporaryPairingObject](audioaccessorysettingstemporarypairingobject.md)
  A dictionary that describes audio accessory temporary pairing behavior. The device enables temporary pairing when this key is present and the `Disabled` key isn’t `false`. The device doesn’t synchronize pairing information with iCloud when temporary pairing is active.

## Properties

- `TemporaryPairing` (AudioAccessorySettingsTemporaryPairingObject): A dictionary that describes audio accessory temporary pairing behavior. The device enables temporary pairing when this key is present and the `Disabled` key isn’t `false`. The device doesn’t synchronize pairing information with iCloud when temporary pairing is active.

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
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/audioaccessorysettings)*