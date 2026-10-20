# SoftwareUpdate

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The payload that configures the software update policy. Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration.

**Availability**:
- macOS 10.7+ - Deprecated in 26.0

## Declaration

```
object SoftwareUpdate
```

#### Discussion

Specify `com.apple.SoftwareUpdate` as the payload type.

##### Profile availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile example

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

- `AllowPreReleaseInstallation` (boolean) *(deprecated)*: ~~If `true`, prerelease software can be installed on this computer.~~

  ~~Available: macOS 10.9+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `AutomaticallyInstallAppUpdates` (boolean) *(deprecated)*: ~~If `false`, deselects the “Install app updates from the App Store” option and prevents the user from changing the option.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `AutomaticallyInstallMacOSUpdates` (boolean) *(deprecated)*: ~~If `false`, restricts the “Install macOS Updates” option and prevents the user from changing the option.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `AutomaticCheckEnabled` (boolean) *(deprecated)*: ~~If `false`, deselects the “Check for updates” option and prevents the user from changing the option.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `AutomaticDownload` (boolean) *(deprecated)*: ~~If `false`, deselects the “Download new updates when available from the App Store” option and prevents the user from changing the option.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `CatalogURL` (string) *(deprecated)*: ~~The URL of the software update catalog. This property isn’t supported in macOS 11 and later.~~

  ~~Deprecated: macOS 11+~~
  Removed: macOS 27+
- `ConfigDataInstall` (boolean) *(deprecated)*: ~~If `false`, restricts the automatic installation of configuration data.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `CriticalUpdateInstall` (boolean) *(deprecated)*: ~~If `false`, disables the automatic installation of critical updates and prevents the user from changing the “Install system data files and security updates” option.~~

  ~~Available: macOS 10.15+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `true`
- `restrict-software-update-require-admin-to-install` (boolean) *(deprecated)*: ~~If `true`, restrict app installations to admin users. This key has the same function as the  `restrict-store-require-admin-to-install` key in the `com.apple.appstore` payload.~~

  ~~Available: macOS 10.14+~~
  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `false`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdate)*