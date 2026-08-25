# SoftwareUpdate

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the software update policy. Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object SoftwareUpdate
```

#### Discussion

Specify `com.apple.SoftwareUpdate` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AutomaticallyInstallAppUpdates</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysoftwareupdatepayload</string>
            <key>PayloadType</key>
            <string>com.apple.SoftwareUpdate</string>
            <key>PayloadUUID</key>
            <string>af3c6efa-0dd3-4021-814b-6f2dba91428b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Software Update</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8b6061ab-31c6-4eee-ba5b-8a09ea8f5fa7</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `AllowPreReleaseInstallation` (boolean): Removed: macOS 27+
- `AutomaticallyInstallAppUpdates` (boolean): Removed: macOS 27+
- `AutomaticallyInstallMacOSUpdates` (boolean): Removed: macOS 27+
- `AutomaticCheckEnabled` (boolean): Removed: macOS 27+
- `AutomaticDownload` (boolean): Removed: macOS 27+
- `CatalogURL` (string): Removed: macOS 27+
- `ConfigDataInstall` (boolean): Removed: macOS 27+
- `CriticalUpdateInstall` (boolean): Removed: macOS 27+
- `restrict-software-update-require-admin-to-install` (boolean): Removed: macOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdate)*