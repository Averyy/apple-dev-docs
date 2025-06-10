# Mail

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a mail account on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object Mail
```

#### Discussion

Specify `com.apple.mail.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EmailAccountDescription</key>
            <string>Company Mail Account</string>
            <key>EmailAccountName</key>
            <string>Juan Chavez</string>
            <key>EmailAccountType</key>
            <string>EmailTypeIMAP</string>
            <key>EmailAddress</key>
            <string>juanchavez4@example.com</string>
            <key>IncomingMailServerAuthentication</key>
            <string>EmailAuthPassword</string>
            <key>IncomingMailServerHostName</key>
            <string>imap.example.com</string>
            <key>IncomingMailServerPortNumber</key>
            <integer>993</integer>
            <key>IncomingMailServerUseSSL</key>
            <true/>
            <key>IncomingMailServerUsername</key>
            <string>juanchavez4@example.com</string>
            <key>IncomingPassword</key>
            <string>Password123</string>
            <key>OutgoingMailServerAuthentication</key>
            <string>EmailAuthPassword</string>
            <key>OutgoingMailServerHostName</key>
            <string>smtp.example.com</string>
            <key>OutgoingMailServerPortNumber</key>
            <integer>587</integer>
            <key>OutgoingMailServerUseSSL</key>
            <true/>
            <key>OutgoingMailServerUsername</key>
            <string>juanchavez4@example.com</string>
            <key>OutgoingPassword</key>
            <string>Password123</string>
            <key>OutgoingPasswordSameAsIncomingPassword</key>
            <false/>
            <key>SMIMEEnablePerMessageSwitch</key>
            <false/>
            <key>SMIMEEnabled</key>
            <false/>
            <key>SMIMEEncryptionEnabled</key>
            <false/>
            <key>SMIMESigningEnabled</key>
            <false/>
            <key>allowMailDrop</key>
            <false/>
            <key>disableMailRecentsSyncing</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mymailpayload</string>
            <key>PayloadType</key>
            <string>com.apple.mail.managed</string>
            <key>PayloadUUID</key>
            <string>d6379d8d-9e05-4d99-80bc-0865f1fe0aca</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Mail</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8e1961d8-898e-4d79-986f-c7a61af4103c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ExchangeActiveSync](exchangeactivesync.md)
  The payload you use to configure Exchange ActiveSync accounts.
- [object ExchangeWebServices](exchangewebservices.md)
  The payload you use to configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mail)*