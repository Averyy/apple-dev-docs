# StatusAccountListMailIncoming

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the devices’s incoming Mail accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListMailIncoming
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
            "mail": {
                "incoming": [
                    {
                        "identifier": "H3F23410-KH33-9G99-FJ62-678901234567",
                        "declaration-identifier": "com.example.mail-account",
                        "visible-name": "Work Mail",
                        "hostname": "imap.example.com",
                        "port": 993,
                        "username": "user@example.com",
                        "is-mail-enabled": true,
                        "are-notes-enabled": true
                    }
                ]
            }
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
            "mail": {
                "incoming": [
                    {
                        "identifier": "H3F23410-KH33-9G99-FJ62-678901234567",
                        "_removed": true
                    }
                ]
            }
        }
    }
}
```

## Topics

### Objects
- [object StatusAccountListMailIncomingAccountObject](statusaccountlistmailincomingaccountobject.md)
  An incoming Mail account.

## Properties

- `account.list.mail.incoming` ([StatusAccountListMailIncomingAccountObject]) *(required)*: A list of status values for the incoming Mail accounts.

## See Also

- [object StatusAccountListCalDAV](statusaccountlistcaldav.md)
  The status item that lists the devices’s Calendar accounts.
- [object StatusAccountListCardDAV](statusaccountlistcarddav.md)
  The status item that lists the devices’s Contacts accounts.
- [object StatusAccountListExchange](statusaccountlistexchange.md)
  The status item that lists the devices’s Exchange accounts.
- [object StatusAccountListGoogle](statusaccountlistgoogle.md)
  The status item that lists the client’s Google accounts.
- [object StatusAccountListLDAP](statusaccountlistldap.md)
  The status item that lists the devices’s Lightweight Directory Access Protocol (LDAP) accounts.
- [object StatusAccountListMailOutgoing](statusaccountlistmailoutgoing.md)
  The status item that lists the devices’s outgoing Mail accounts.
- [object StatusAccountListSubscribedCalendar](statusaccountlistsubscribedcalendar.md)
  The status item that lists the devices’s subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistmailincoming)*