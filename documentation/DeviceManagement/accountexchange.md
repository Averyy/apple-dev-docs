# AccountExchange

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure an Exchange account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object AccountExchange
```

#### Discussion

Specify `com.apple.configuration.account.exchange` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.account.exchange",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Work Exchange",
        "HostName": "exchange.example.com",
        "EnabledProtocolTypes": [
            "EAS",
            "EWS"
        ],
        "UserIdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4",
        "AuthenticationCredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100",
        "LockMailService": true,
        "NotesServiceActive": false,
        "LockNotesService": true
    }
}
```

## Topics

### Objects
- [object AccountExchangeOAuthObject](accountexchangeoauthobject.md)
  The declaration for configuring OAuth authentication of an Exchange account.
- [object AccountExchangeSMIMEObject](accountexchangesmimeobject.md)
  Settings for S/MIME.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
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
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test declarative device management.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object Package](package.md)
  The declaration to install a package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountexchange)*