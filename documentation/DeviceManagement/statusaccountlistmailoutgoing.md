# StatusAccountListMailOutgoing

**Framework**: Device Management  
**Kind**: dictionary

The status item that lists the devices’s outgoing Mail accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListMailOutgoing
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
                "outgoing": [
                    {
                        "identifier": "I4G34521-LI44-0H00-GK73-789012345678",
                        "declaration-identifier": "com.example.mail-account",
                        "visible-name": "Work Mail (SMTP)",
                        "hostname": "smtp.example.com",
                        "port": 587,
                        "username": "user@example.com"
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
                "outgoing": [
                    {
                        "identifier": "I4G34521-LI44-0H00-GK73-789012345678",
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
- [object StatusAccountListMailOutgoingAccountObject](statusaccountlistmailoutgoingaccountobject.md)
  An outgoing Mail account.

## Properties

- `account.list.mail.outgoing` ([StatusAccountListMailOutgoingAccountObject]) *(required)*: A list of status values for the outgoing Mail accounts.

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
- [object StatusAccountListSubscribedCalendar](statusaccountlistsubscribedcalendar.md)
  The status item that lists the devices’s subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistmailoutgoing)*