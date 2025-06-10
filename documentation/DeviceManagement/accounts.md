# Accounts

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure guest accounts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object Accounts
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EnableGuestAccount</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myaccountpayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>5d4e377c-108c-44af-a46e-97a5aac1e270</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Accounts</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8cd28a9d-625e-4056-bbd0-43617bb8efb7</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object CalDAV](caldav.md)
  The payload you use to configure a Calendar account.
- [object CardDAV](carddav.md)
  The payload you use to configure a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload you use to configure a Google account.
- [object LDAP](ldap.md)
  The payload you use to configure an LDAP account.
- [object MobileAccounts](mobileaccounts.md)
  The payload you use to configure mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload you use to configure subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accounts)*