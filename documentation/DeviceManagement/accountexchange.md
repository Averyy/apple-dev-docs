# AccountExchange

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure an Exchange account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up a Microsoft Exchange account.

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
  The configuration settings for OAuth for this account.
- [object AccountExchangeSMIMEObject](accountexchangesmimeobject.md)
  Settings for S/MIME.

## Properties

- `AuthenticationCredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials for this account to authenticate with an Exchange server. Set the corresponding asset type to `CredentialUserNameAndPassword`.
- `AuthenticationIdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that this account requires to authenticate with the Exchange server.
- `CalendarServiceActive` (boolean): If `true`, activates the calendar service for this account.
- `ContactsServiceActive` (boolean): If `true`, activates the address book service for this account.
- `EnabledProtocolTypes` ([string]) *(required)*: The set of protocol types to enable on the Exchange server, in order of preference. This is an array of unique strings with possible values: - `EAS:` Exchange ActiveSync
- `EWS:` Exchange Web Services If the device supports one or more of the listed protocol types, it sets up an account for the first supported type. If the device doesn’t support any of the listed protocol types, it doesn’t set up an account and the system reports an error.
- `External Path` (string): The external path of the EWS server. The system uses this only when this declaration has a `ExternalHostName` value. Available: macOS 13+
- `ExternalHostName` (string): The external hostname of the EWS server (or IP address). Available: macOS 13+
- `ExternalPort` (integer): The external port number of the EWS server. The system uses this only when this declaration has a `ExternalHostName` value. Available: macOS 13+
- `HostName` (string): The IP address or fully qualified domain name (FQDN) of the Exchange host.
- `LockCalendarService` (boolean): If `true`, the system prevents the user from changing the status of the calendar service for this account. Available: iOS 15+ | iPadOS 15+ | visionOS 1.1+
- `LockContactsService` (boolean): If `true`, the system prevents the user from changing the status of the address book service for this account. Available: iOS 15+ | iPadOS 15+ | visionOS 1.1+
- `LockMailService` (boolean): If `true`, the system prevents the user from changing the status of the mail service for this account. Available: iOS 15+ | iPadOS 15+ | visionOS 1.1+
- `LockNotesService` (boolean): If `true`, the system prevents the user from changing the status of the notes service for this account. Available: iOS 15+ | iPadOS 15+ | visionOS 1.1+
- `LockRemindersService` (boolean): If `true`, the system prevents the user from changing the status of the reminders service for this account. Available: iOS 15+ | iPadOS 15+ | visionOS 1.1+
- `MailServiceActive` (boolean): If `true`, the system activates the mail service for this account.
- `NotesServiceActive` (boolean): If `true`, the system activates the notes service for this account.
- `OAuth` (AccountExchangeOAuthObject): The configuration settings for OAuth for this account.
- `Path` (string): The path of the EWS server. The system uses this only when this declaration has a `HostName` value. Available: macOS 13+
- `Port` (integer): The port number of the EWS server. The system uses this only when this declaration has a `HostName` value. Available: macOS 13+
- `RemindersServiceActive` (boolean): If `true`, the system activates the reminders service for this account.
- `SMIME` (AccountExchangeSMIMEObject): Settings for S/MIME. Available: iOS 17+ | iPadOS 17+ | visionOS 1.1+
- `UserIdentityAssetReference` (string): The identifier of an asset declaration that contains the user identity for this account. The corresponding asset must be of type `UserIdentity`.
- `VisibleName` (string): The name that apps show to the user for this Exchange account. If not present, the system generates a suitable default.

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
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountexchange)*