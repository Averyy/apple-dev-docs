# StatusAccountListSubscribedCalendar

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the devices’s subscribed calendars.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListSubscribedCalendar
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
            "subscribed-calendar": [
                {
                    "identifier": "J5H45632-MJ55-1I11-HL84-890123456789",
                    "declaration-identifier": "com.example.subscribed-calendar",
                    "visible-name": "Company Holidays",
                    "calendar-url": "https://calendar.example.com/holidays.ics",
                    "username": "user@example.com",
                    "is-enabled": true
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
            "subscribed-calendar": [
                {
                    "identifier": "J5H45632-MJ55-1I11-HL84-890123456789",
                    "_removed": true
                }
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusAccountListSubscribedCalendarAccountObject](statusaccountlistsubscribedcalendaraccountobject.md)
  A subscribed calendar.

## Properties

- `account.list.subscribed-calendar` ([StatusAccountListSubscribedCalendarAccountObject]) *(required)*: A list of status values for the subscribed calendars.

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
- [object StatusAccountListMailIncoming](statusaccountlistmailincoming.md)
  The status item that lists the devices’s incoming Mail accounts.
- [object StatusAccountListMailOutgoing](statusaccountlistmailoutgoing.md)
  The status item that lists the devices’s outgoing Mail accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistsubscribedcalendar)*