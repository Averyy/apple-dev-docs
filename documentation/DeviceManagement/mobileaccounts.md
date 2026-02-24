# MobileAccounts

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures mobile accounts on the device.

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

## Properties

- `cachedaccounts.askForSecureTokenAuthBypass` (boolean): If `true`, the system bypasses the secure token authorization dialog. This dialog only appears on APFS volumes.
- `cachedaccounts.expiry.delete.disusedSeconds` (integer): The minimum number of seconds a mobile account can exist before the system makes an automatic attempt to remove the mobile account. Set to `0` to attempt removing it at the next login or logout. Set to `-1` to never attempt removing the mobile account.
- `cachedaccounts.WarnOnCreate.allowNever` (boolean): If `true`, the system allows the user to stop the prompts about mobile account creation every time the user logs in. This key is only valid if `com.apple.cachedaccounts.WarnOnCreate` is `true`.
- `com.apple.cachedaccounts.CreateAtLogin` (boolean): If `true`, the system creates the mobile account at login time.
- `com.apple.cachedaccounts.WarnOnCreate` (boolean): If `true`, the system asks the user whether to create the mobile account and it allows the user to not create it.

## See Also

- [object Accounts](accounts.md)
  The payload that configures guest accounts.
- [object CalDAV](caldav.md)
  The payload that configures a Calendar account.
- [object CardDAV](carddav.md)
  The payload that configures a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload that configures a Google account.
- [object LDAP](ldap.md)
  The payload that configures a Lightweight Directory Access Protocol (LDAP) account.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload that configures subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mobileaccounts)*