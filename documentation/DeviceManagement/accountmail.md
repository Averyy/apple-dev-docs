# AccountMail

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a Mail account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object AccountMail
```

#### Discussion

Specify `com.apple.configuration.account.mail` as the declaration type.

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

This configuration sets up an IMAP email account with SMTP outgoing mail.

```json
{
    "Type": "com.apple.configuration.account.mail",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Work Mail",
        "UserIdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4",
        "IncomingServer": {
            "ServerType": "IMAP",
            "HostName": "imap.example.com",
            "AuthenticationMethod": "Password",
            "AuthenticationCredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100"
        },
        "OutgoingServer": {
            "HostName": "smtp.example.com",
            "AuthenticationMethod": "Password",
            "AuthenticationCredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100"
        }
    }
}
```

## Topics

### Objects
- [object AccountMailIncomingServerObject](accountmailincomingserverobject.md)
  The settings for the incoming mail server for this account.
- [object AccountMailOutgoingServerObject](accountmailoutgoingserverobject.md)
  The settings for the outgoing mail server for this account.
- [object AccountMailSMIMEObject](accountmailsmimeobject.md)
  Settings for S/MIME.

## Properties

- `IncomingServer` (AccountMailIncomingServerObject) *(required)*: The settings for the incoming mail server for this account.
- `OutgoingServer` (AccountMailOutgoingServerObject) *(required)*: The settings for the outgoing mail server for this account.
- `SMIME` (AccountMailSMIMEObject): Settings for S/MIME. Available: iOS 17+ | iPadOS 17+ | visionOS 1.1+
- `UserIdentityAssetReference` (string): The identifier of an asset declaration that contains the user identity for this account. Set the corresponding asset type to `UserIdentity`.
- `VisibleName` (string): The name that apps show to the user for this mail account. If not present, the system generates a suitable default.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountmail)*