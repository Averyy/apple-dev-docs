# MathSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the math and calculator apps.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettings
```

#### Discussion

Specify `com.apple.configuration.math.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Example

This configuration prevents the use of scientific and programmer modes in calculator app.

```json
{
    "Type": "com.apple.configuration.math.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Calculator": {
            "ScientificMode": {
                "Enabled": false
            },
            "ProgrammerMode": {
                "Enabled": false
            }
        }
    }
}
```

## Topics

### Objects
- [object MathSettingsCalculatorObject](mathsettingscalculatorobject.md)
  If present, configures the built-in Calculator app.
- [object MathSettingsSystemBehaviorObject](mathsettingssystembehaviorobject.md)
  If present, configures math behavior in the system.

## Properties

- `Calculator` (MathSettingsCalculatorObject): If present, configures the built-in Calculator app.
- `SystemBehavior` (MathSettingsSystemBehaviorObject): If present, configures math behavior in the system.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettings)*