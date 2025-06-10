# GoogleAccount

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a Google account.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- visionOS 1.1+

## Declaration

```swift
object GoogleAccount
```

#### Discussion

Specify `com.apple.google-oauth` as the payload type.

You can install multiple Google payloads. Each sets up a Google email address and any other Google services the user enables after authentication.

> **Note**:  For supervised devices, the system requires installation of Google accounts through MDM or Apple Configurator 2.

The payload never contains credentials; the system prompts the user to enter credentials shortly after installation of the payload.

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
            <key>AccountDescription</key>
            <string>Google Account</string>
            <key>AccountName</key>
            <string>Juan Chavez</string>
            <key>EmailAddress</key>
            <string>juanchavez4@example.com</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mygoogleaccountpayload</string>
            <key>PayloadType</key>
            <string>com.apple.google-oauth</string>
            <key>PayloadUUID</key>
            <string>0fe8f4dc-8cf0-4da3-9d5b-f734efb98a59</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>GoogleAccount</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>80141025-50d3-4a38-9387-ca610ff3a247</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object GoogleAccount.CommunicationServiceRules](googleaccount/communicationservicerules-data.dictionary.md)
  The communication service handler rules for this account.

## See Also

- [object Accounts](accounts.md)
  The payload you use to configure guest accounts.
- [object CalDAV](caldav.md)
  The payload you use to configure a Calendar account.
- [object CardDAV](carddav.md)
  The payload you use to configure a Contacts account.
- [object LDAP](ldap.md)
  The payload you use to configure an LDAP account.
- [object MobileAccounts](mobileaccounts.md)
  The payload you use to configure mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload you use to configure subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/googleaccount)*