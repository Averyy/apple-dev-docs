# StatusAccountListCalDAV

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the devices’s Calendar accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListCalDAV
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
            "caldav": [
                {
                    "identifier": "C8AD8975-FC88-4B44-AE17-123456789012",
                    "declaration-identifier": "com.example.caldav-account",
                    "visible-name": "Work Calendar",
                    "hostname": "caldav.example.com",
                    "port": 443,
                    "username": "user@example.com",
                    "are-calendars-enabled": true,
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
            "caldav": [
                {
                    "identifier": "C8AD8975-FC88-4B44-AE17-123456789012",
                    "_removed": true
                }
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusAccountListCalDAVAccountObject](statusaccountlistcaldavaccountobject.md)
  A Calendar account.

## Properties

- `account.list.caldav` ([StatusAccountListCalDAVAccountObject]) *(required)*: A list of status values for the Calendar accounts.

## See Also

- [object StatusAccountListCardDAV](statusaccountlistcarddav.md)
  The status item that lists the devices’s Contacts accounts.
- [object StatusAccountListExchange](statusaccountlistexchange.md)
  The status item that lists the devices’s Exchange accounts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistcaldav)*