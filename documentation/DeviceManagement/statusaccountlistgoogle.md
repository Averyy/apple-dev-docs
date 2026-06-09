# StatusAccountListGoogle

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the client’s Google accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListGoogle
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

**New or updated account**:

Reports a new or updated account.

```json
{
    "account": {
        "list": {
            "google": [
                {
                    "identifier": "F1D01298-IF11-7E77-DH40-456789012345",
                    "declaration-identifier": "com.example.google-account",
                    "visible-name": "Work Google",
                    "username": "user@example.com",
                    "is-mail-enabled": true,
                    "are-calendars-enabled": true,
                    "are-contacts-enabled": true,
                    "are-notes-enabled": false
                }
            ]
        }
    }
}
```

**Removed account**:

Reports a removed account.

```json
{
    "account": {
        "list": {
            "google": [
                {
                    "identifier": "F1D01298-IF11-7E77-DH40-456789012345",
                    "_removed": true
                }
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusAccountListGoogleAccountObject](statusaccountlistgoogleaccountobject.md)
  A Google account.

## Properties

- `account.list.google` ([StatusAccountListGoogleAccountObject]) *(required)*: A list of status values for the Google accounts.

## See Also

- [object StatusAccountListCalDAV](statusaccountlistcaldav.md)
  The status item that lists the devices’s Calendar accounts.
- [object StatusAccountListCardDAV](statusaccountlistcarddav.md)
  The status item that lists the devices’s Contacts accounts.
- [object StatusAccountListExchange](statusaccountlistexchange.md)
  The status item that lists the devices’s Exchange accounts.
- [object StatusAccountListLDAP](statusaccountlistldap.md)
  The status item that lists the devices’s Lightweight Directory Access Protocol (LDAP) accounts.
- [object StatusAccountListMailIncoming](statusaccountlistmailincoming.md)
  The status item that lists the devices’s incoming Mail accounts.
- [object StatusAccountListMailOutgoing](statusaccountlistmailoutgoing.md)
  The status item that lists the devices’s outgoing Mail accounts.
- [object StatusAccountListSubscribedCalendar](statusaccountlistsubscribedcalendar.md)
  The status item that lists the devices’s subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistgoogle)*