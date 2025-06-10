# MobileAccounts

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure mobile accounts on the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object MobileAccounts
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>com.apple.cachedaccounts.CreateAtLogin</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mymobileccountpayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>93aa2058-4fe5-4f8b-a409-80f05b7fb2f0</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Mobility</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b89ce975-801b-4994-8f68-dc5cad408ad1</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Accounts](accounts.md)
  The payload you use to configure guest accounts.
- [object CalDAV](caldav.md)
  The payload you use to configure a Calendar account.
- [object CardDAV](carddav.md)
  The payload you use to configure a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload you use to configure a Google account.
- [object LDAP](ldap.md)
  The payload you use to configure an LDAP account.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload you use to configure subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mobileaccounts)*