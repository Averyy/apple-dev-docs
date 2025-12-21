# ExchangeActiveSync

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Exchange ActiveSync accounts.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+

## Declaration

```swift
object ExchangeActiveSync
```

#### Discussion

Specify `com.apple.eas.account` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS |
| User channel | Shared iPad |
| Allow manual install | iOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | iOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EmailAddress</key>
            <string>juanchavez4@companyemail.com</string>
            <key>EnableCalendars</key>
            <true/>
            <key>EnableCalendarsUserOverridable</key>
            <true/>
            <key>EnableContacts</key>
            <true/>
            <key>EnableContactsUserOverridable</key>
            <true/>
            <key>EnableMail</key>
            <true/>
            <key>EnableMailUserOverridable</key>
            <true/>
            <key>EnableNotes</key>
            <true/>
            <key>EnableNotesUserOverridable</key>
            <true/>
            <key>EnableReminders</key>
            <true/>
            <key>EnableRemindersUserOverridable</key>
            <true/>
            <key>Host</key>
            <string>host.companyemail.com</string>
            <key>MailNumberOfPastDaysToSync</key>
            <integer>7</integer>
            <key>OAuth</key>
            <false/>
            <key>OverridePreviousPassword</key>
            <false/>
            <key>SMIMEEnabled</key>
            <false/>
            <key>SMIMEEncryptionEnabled</key>
            <false/>
            <key>SMIMESigningEnabled</key>
            <false/>
            <key>SSL</key>
            <true/>
            <key>UserName</key>
            <string>juanchavez4@companyemail.com</string>
            <key>disableMailRecentsSyncing</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myeaspayload</string>
            <key>PayloadType</key>
            <string>com.apple.eas.account</string>
            <key>PayloadUUID</key>
            <string>de789252-dcf2-42e7-91c8-0ab9f50aafc5</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Exchange Active Sync</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b8fd6fd7-a55e-4eb1-96af-d9c4d8562e38'</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ExchangeActiveSync.CommunicationServiceRules](exchangeactivesync/communicationservicerules-data.dictionary.md)
  The communication service rules.

## See Also

- [object ExchangeWebServices](exchangewebservices.md)
  The payload that configures an Exchange Web Services accounts.
- [object Mail](mail.md)
  The payload that configures a Mail account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/exchangeactivesync)*