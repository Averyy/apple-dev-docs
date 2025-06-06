# SubscribedCalendars

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure subscribed calendars.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SubscribedCalendars
```

#### Discussion

Specify `com.apple.subscribedcalendar.account` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS |
| User Channel | Shared iPad |
| Allow Manual Install | iOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS |
| Allow Multiple Payloads | iOS, Shared iPad |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>SubCalAccountDescription</key>
            <string>US Holiday Calendar</string>
            <key>SubCalAccountHostName</key>
            <string>http://ical.mac.com/ical/US32Holidays.ics</string>
            <key>SubCalAccountUseSSL</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysubscribedcalpayload</string>
            <key>PayloadType</key>
            <string>com.apple.subscribedcalendar.account</string>
            <key>PayloadUUID</key>
            <string>c23dd040-6f68-4af2-b840-62d1943236b5</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Subscribed Calendars</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>c360335c-3cfd-43d5-88c3-7e58e92821a9</string>
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
- [object MobileAccounts](mobileaccounts.md)
  The payload you use to configure mobile accounts on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/subscribedcalendars)*