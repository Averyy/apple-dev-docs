# CardDAV

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a Contacts account.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object CardDAV
```

#### Discussion

Specify `com.apple.carddav.account` as the payload type.

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
            <key>CardDAVAccountDescription</key>
            <string>My CardDAV Account</string>
            <key>CardDAVHostName</key>
            <string>server.example.com</string>
            <key>CardDAVPassword</key>
            <string>Password123</string>
            <key>CardDAVPort</key>
            <integer>443</integer>
            <key>CardDAVUseSSL</key>
            <true/>
            <key>CardDAVUsername</key>
            <string>juanchavez4</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycardavpayload</string>
            <key>PayloadType</key>
            <string>com.apple.carddav.account</string>
            <key>PayloadUUID</key>
            <string>b23d14e3-2f9d-4087-a819-747903fbb176</string>
            <key>PayloadVersion</key>
            <real>1</real>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>CardDAV</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>4fdb234d-8c58-48de-a76d-9ed9d241d273</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object CardDAV.CommunicationServiceRules](carddav/communicationservicerules-data.dictionary.md)
  The communication service handler rules for this account.

## See Also

- [object Accounts](accounts.md)
  The payload that configures guest accounts.
- [object CalDAV](caldav.md)
  The payload that configures a Calendar account.
- [object GoogleAccount](googleaccount.md)
  The payload that configures a Google account.
- [object LDAP](ldap.md)
  The payload that configures a Lightweight Directory Access Protocol (LDAP) account.
- [object MobileAccounts](mobileaccounts.md)
  The payload that configures mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload that configures subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/carddav)*