# AppStore

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures macOS App Store restrictions.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object AppStore
```

#### Discussion

Specify `com.apple.appstore` as the payload type.

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
            <key>DisableSoftwareUpdateNotifications</key>
            <true/>
            <key>restrict-store-disable-app-adoption</key>
            <true/>
            <key>restrict-store-softwareupdate-only</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myappstorepayload</string>
            <key>PayloadType</key>
            <string>com.apple.appstore</string>
            <key>PayloadUUID</key>
            <string>44561b1a-c66c-42b8-80cd-c30a29766e34</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>App Store</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>61c30df8-92e8-4fc5-8623-8cfc294452ce</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `DisableSoftwareUpdateNotifications` (boolean): If `true`, the system disables software update notifications. Available in macOS 10.10 and later.
- `restrict-store-disable-app-adoption` (boolean): If `true`, the system disables app adoption by users. Available in macOS 10.10 and later.
- `restrict-store-require-admin-to-install` (boolean): If `true`, the system restricts app installations to admin users only. Deprecated in macOS 10.14. Use the `com.apple.SoftwareUpdate` payload key `restrict-software-update-require-admin-to-install` instead.
- `restrict-store-softwareupdate-only` (boolean): If `true`, the system prevents App Store from launching. Available in macOS 10.14 and later. Restricts installations to software updates only in macOS 10.10 through 10.13.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appstore)*