# SoftwareUpdate

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the software update policy.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

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
| User channel | NA |
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

- `AllowPreReleaseInstallation` (boolean): If `true`, prerelease software can be installed on this computer.
- `AutomaticallyInstallAppUpdates` (boolean): If `false`, deselects the “Install app updates from the App Store” option and prevents the user from changing the option.
- `AutomaticallyInstallMacOSUpdates` (boolean): If `false`, restricts the “Install macOS Updates” option and prevents the user from changing the option.
- `AutomaticCheckEnabled` (boolean): If `false`, deselects the “Check for updates” option and prevents the user from changing the option.
- `AutomaticDownload` (boolean): If `false`, deselects the “Download new updates when available from the App Store” option and prevents the user from changing the option.
- `CatalogURL` (string): The URL of the software update catalog. This property is not supported in macOS 11 and later.
- `ConfigDataInstall` (boolean): If `false`, restricts the automatic installation of configuration data.
- `CriticalUpdateInstall` (boolean): If `false`, disables the automatic installation of critical updates and prevents the user from changing the “Install system data files and security updates” option.
- `restrict-software-update-require-admin-to-install` (boolean): If `true`, restrict app installations to admin users. This key has the same function as the  `restrict-store-require-admin-to-install` key in the `com.apple.appstore` payload.

## See Also

- [object SystemMigration](systemmigration.md)
  The payload that configures system migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdate)*