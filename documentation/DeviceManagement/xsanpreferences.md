# XsanPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the Xsan preferences that define the volumes that automatically mount at startup.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object XsanPreferences
```

#### Discussion

Specify `com.apple.xsan.preferences` as the payload type.

For more information, see [`https://support.apple.com/en-us/HT205333`](https://developer.apple.comhttps://support.apple.com/en-us/HT205333).

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

##### Example Profile

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>useDLC</key>
            <true/>
            <key>denyMount</key>
            <array>
                <string>bob</string>
            </array>
            <key>denyDLC</key>
            <array>
                <string>bob</string>
            </array>
            <key>preferDLC</key>
            <array>
                <string>bob</string>
            </array>
            <key>onlyMount</key>
            <array>
                <string>bob</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myxsanpreferencespayload</string>
            <key>PayloadType</key>
            <string>com.apple.xsan.preferences</string>
            <key>PayloadUUID</key>
            <string>1addfbe1-d696-4143-bec1-7cfa4121fa76</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Xsan Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>63ebad99-1dbc-4b3b-a618-2789cda3eedd</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Xsan](xsan.md)
  The payload that configures an Xsan client system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/xsanpreferences)*