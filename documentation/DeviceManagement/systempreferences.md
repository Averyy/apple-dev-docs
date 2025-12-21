# SystemPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the preference panes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object SystemPreferences
```

#### Discussion

Specify `com.apple.systempreferences` as the payload type.

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
            <key>EnabledPreferencePanes</key>
            <array>
                <string>com.apple.preferences.users</string>
            </array>
            <key>DisabledPreferencePanes</key>
            <array>
                <string>com.apple.preference.dock</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempayload</string>
            <key>PayloadType</key>
            <string>com.apple.systempreferences</string>
            <key>PayloadUUID</key>
            <string>6e7d6ddc-70fc-4126-a0a3-c312c4e16e06</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>28114fac-d230-484f-8747-4f3f1077f95c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object AIMAccount](aimaccount.md)
  The payload that configures an AIM account on the device.
- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload that configures a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload that configures a macOS Server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload that configures allowed dashboard widgets.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempreferences)*