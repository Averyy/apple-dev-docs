# AccountSettings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The declaration to configure account settings.

**Availability**:
- macOS 27.2+

## Declaration

```
object AccountSettings
```

#### Discussion

Specify `com.apple.configuration.account.settings` as the declaration type.

##### Configuration availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration example

This configuration prevents alerts about the retirement of Exchange Web Services.

```json
{
    "Type": "com.apple.configuration.account.settings",
    "Identifier": "D699D1DB-28B3-4899-8554-1630D201EF55",
    "ServerToken": "62EA7624-7603-4C15-B747-7334476C1BDE",
    "Payload": {
        "Exchange": {
            "AllowEWSRetirementAlerts": false
        }
    }
}
```

## Topics

### Objects
- [object AccountSettingsExchangeObject](./accountsettingsexchangeobject.md)
  If present, configures settings for Exchange accounts.

## Properties

- `Exchange` (AccountSettingsExchangeObject): If present, configures settings for Exchange accounts.

## See Also

### Configurations
- [object AccessibilitySettings](./accessibilitysettings.md)
  The declaration to configure accessibility settings.
- [object AccountCalDAV](./accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](./accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](./accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](./accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](./accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](./accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](./accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](./appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](./appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](./audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](./contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](./diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](./extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](./externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountsettings)*