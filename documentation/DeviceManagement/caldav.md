# CalDAV

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a Calendar account.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object CalDAV
```

#### Discussion

Specify `com.apple.caldav.account` as the payload type.

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
            <key>CalDAVAccountDescription</key>
            <string>My CalDAV Account</string>
            <key>CalDAVHostName</key>
            <string>server.example.com</string>
            <key>CalDAVPassword</key>
            <string>Password123</string>
            <key>CalDAVPort</key>
            <integer>443</integer>
            <key>CalDAVUseSSL</key>
            <true/>
            <key>CalDAVUsername</key>
            <string>juanchavez4@example.com</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycaldavpayload</string>
            <key>PayloadType</key>
            <string>com.apple.caldav.account</string>
            <key>PayloadUUID</key>
            <string>603409f1-b611-459d-9584-0ed12bc25b5b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>CalDAV</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>5c8bb406-a74c-4338-93c6-b403a040cc91</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Accounts](accounts.md)
  The payload that configures guest accounts.
- [object CardDAV](carddav.md)
  The payload that configures a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload that configures a Google account.
- [object LDAP](ldap.md)
  The payload that configures a Lightweight Directory Access Protocol (LDAP) account.
- [object MobileAccounts](mobileaccounts.md)
  The payload that configures mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload that configures subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/caldav)*