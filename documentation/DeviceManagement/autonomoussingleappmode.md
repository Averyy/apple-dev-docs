# AutonomousSingleAppMode

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Autonomous Single App mode.

**Availability**:
- macOS 10.13.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AutonomousSingleAppMode
```

#### Discussion

Specify `com.apple.asam` as the payload type.

The system only allows installation of one profile of this type, and it requires installation through a user-approved MDM server. Apps listed in this profile have low-level access to the system, including, but not limited to, key logging and user interface manipulation outside the app’s context.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | - |
| Requires Supervision | - |
| Requires User Approved MDM | macOS |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowedApplications</key>
            <array>
                <dict>
                    <key>BundleIdentifier</key>
                    <string>com.apple.safari</string>
                    <key>TeamIdentifier</key>
                    <string>team-id</string>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myasampayload</string>
            <key>PayloadType</key>
            <string>com.apple.asam</string>
            <key>PayloadUUID</key>
            <string>c324fd3e-d98a-4ea8-818a-5991024cddd0</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Autonomous Single App Mode</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>467ab3a0-9423-4c16-a05c-5c99d771088f</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object AutonomousSingleAppMode.AllowedApplicationsItem](autonomoussingleappmode/allowedapplicationsitem.md)
  A dictionary that specifies an app that can be granted access to the Accessibilty APIs.

## See Also

- [object AppLock](applock.md)
  The payload you use to configure a device to run a single app.
- [object AssociatedDomains](associateddomains.md)
  The payload you use to configure associated domains.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload you use to configure the extensions that the system allows or disallows to run on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/autonomoussingleappmode)*