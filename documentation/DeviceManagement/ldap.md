# LDAP

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure an LDAP account.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object LDAP
```

#### Discussion

Specify `com.apple.ldap.account` as the payload type.

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
            <key>LDAPAccountDescription</key>
            <string>Company LDAP Account</string>
            <key>LDAPAccountHostName</key>
            <string>com.apple.ldap.account</string>
            <key>LDAPAccountUseSSL</key>
            <true/>
            <key>LDAPAccountUserName</key>
            <string>JuanChavez4</string>
            <key>LDAPSearchSettings</key>
            <array>
                <dict>
                    <key>LDAPSearchSettingDescription</key>
                    <string>My Search</string>
                    <key>LDAPSearchSettingScope</key>
                    <string>LDAPSearchSettingScopeSubtree</string>
                    <key>LDAPSearchSettingSearchBase</key>
                    <string>o=My Company,ou=My Department</string>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myldappayload</string>
            <key>PayloadType</key>
            <string>com.apple.ldap.account</string>
            <key>PayloadUUID</key>
            <string>7f846724-1bf7-4501-b8cd-ce7026e95280</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>LDAP</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>c5208028-7e96-4669-8d83-4fbbeb48845a</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object LDAP.LDAPSearchSettingsItem](ldap/ldapsearchsettingsitem.md)
  An array of search settings dictionaries.

## See Also

- [object Accounts](accounts.md)
  The payload you use to configure guest accounts.
- [object CalDAV](caldav.md)
  The payload you use to configure a Calendar account.
- [object CardDAV](carddav.md)
  The payload you use to configure a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload you use to configure a Google account.
- [object MobileAccounts](mobileaccounts.md)
  The payload you use to configure mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload you use to configure subscribed calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/ldap)*