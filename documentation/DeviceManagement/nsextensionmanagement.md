# NSExtensionManagement

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the extensions that the system allows or disallows to run on the device.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object NSExtensionManagement
```

#### Discussion

Specify `com.apple.NSExtension` as the payload type.

You can manage extensions by bundle identifiers in allow and deny lists, or by a deny list of extension points.

You can also start with all public extensions disallowed. To do so, include `AllPublicExtensionPoints` in `DeniedExtensionPoints`. This causes the system to expand the list to include all extensions that belong to any public extension points. This expansion occurs at evaluation time. The list of extension points can change from release to release. The expanded list disallows Apple and third-party extensions, but still allows extensions that belong to system-critcial extension points to execute.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | macOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowedExtensions</key>
            <array>
                <string>com.apple.share.AirDrop.send</string>
            </array>
            <key>DeniedExtensions</key>
            <array>
                <string>com.apple.ncplugin.stocks</string>
            </array>
            <key>DeniedExtensionPoints</key>
            <array>
                <string>com.apple.share-services</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mynsempayload</string>
            <key>PayloadType</key>
            <string>com.apple.nsextension</string>
            <key>PayloadUUID</key>
            <string>9726bc46-1e51-466b-99e3-81b23561cf81</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>NS Extension Management</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>4cc87081-feee-46d1-b5d1-2a2fde9a8402</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object AppLock](applock.md)
  The payload you use to configure a device to run a single app.
- [object AssociatedDomains](associateddomains.md)
  The payload you use to configure associated domains.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload you use to configure Autonomous Single App mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextensionmanagement)*