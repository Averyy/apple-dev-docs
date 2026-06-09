# StatusAccountListExchange

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the devices’s Exchange accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListExchange
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
            "exchange": [
                {
                    "identifier": "E0CF0187-HE00-6D66-CG39-345678901234",
                    "declaration-identifier": "com.example.exchange-account",
                    "visible-name": "Work Exchange",
                    "hostname": "mail.example.com",
                    "port": 443,
                    "username": "user@example.com",
                    "is-mail-enabled": true,
                    "are-calendars-enabled": true,
                    "are-contacts-enabled": true,
                    "are-notes-enabled": true,
                    "are-reminders-enabled": true
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
            "exchange": [
                {
                    "identifier": "E0CF0187-HE00-6D66-CG39-345678901234",
                    "_removed": true
                }
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusAccountListExchangeAccountObject](statusaccountlistexchangeaccountobject.md)
  An Exchange account.

## Properties

- `account.list.exchange` ([StatusAccountListExchangeAccountObject]) *(required)*: A list of status values for the Exchange accounts.

## See Also

- [object StatusAccountListCalDAV](statusaccountlistcaldav.md)
  The status item that lists the devices’s Calendar accounts.
- [object StatusAccountListCardDAV](statusaccountlistcarddav.md)
  The status item that lists the devices’s Contacts accounts.
- [object StatusAccountListGoogle](statusaccountlistgoogle.md)
  The status item that lists the client’s Google accounts.
- [object StatusAccountListLDAP](statusaccountlistldap.md)
  The status item that lists the devices’s Lightweight Directory Access Protocol (LDAP) accounts.
- [object StatusAccountListMailIncoming](statusaccountlistmailincoming.md)
  The status item that lists the devices’s incoming Mail accounts.
- [object StatusAccountListMailOutgoing](statusaccountlistmailoutgoing.md)
  The status item that lists the devices’s outgoing Mail accounts.
- [object StatusAccountListSubscribedCalendar](statusaccountlistsubscribedcalendar.md)
  The status item that lists the devices’s subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistexchange)*