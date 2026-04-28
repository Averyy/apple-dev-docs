# XsanPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the Xsan preferences that define the volumes that automatically mount at startup.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

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

## Properties

- `denyDLC` ([string]): An array of StorNext volume names. If the Xsan client is attempting to mount a volume named in this array, the client only mounts the volume if its logical units (LUNs) are available through Fibre Channel. It doesn’t attempt to mount the volume using Distributed LAN Client (DLC).
- `denyMount` ([string]): An array of Xsan or StorNext volume names. If no `onlyMount` array is present, the Xsan client automatically attempts to mount all SAN volumes except the volumes in this array. The system administrator can mount those volumes manually by using the `xsanctl(8)` mount command.
- `onlyMount` ([string]): An array of Xsan or StorNext volume names. The Xsan client attempts to automatically mount these volumes at startup. The system administrator can mount additional volumes manually by using the `xsanctl(8)` mount command.
- `preferDLC` ([string]): An array of StorNext volume names. If the Xsan client is attempting to mount a volume named in this array, the Xsan client attempts to mount the volume using DLC. If DLC isn’t available, the client attempts to mount the volume if its LUNs are available through Fibre Channel. The volume name must not also appear in `denyDLC`.
- `useDLC` (boolean): If `true`, use the DLC for all volumes.

## See Also

- [object Xsan](xsan.md)
  The payload that configures an Xsan client system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/xsanpreferences)*