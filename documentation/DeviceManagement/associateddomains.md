# AssociatedDomains

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure associated domains.

**Availability**:
- macOS 10.15+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AssociatedDomains
```

#### Discussion

Specify `com.apple.associated-domains` as the payload type.

You can use associated domains with features such as Extensible AppSSO, universal links, and Password AutoFill.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | macOS |
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
            <key>Configuration</key>
            <array>
                <dict>
                    <key>ApplicationIdentifier</key>
                    <string>com.apple.mobilesafari</string>
                    <key>AssociatedDomains</key>
                    <array>
                        <string>www.example.com</string>
                    </array>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myassociateddomainpayload</string>
            <key>PayloadType</key>
            <string>com.apple.associated-domains</string>
            <key>PayloadUUID</key>
            <string>7f6e26da-c381-4666-9dc6-50b4cd418652</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Associated Domains</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2c8c95c4-fde5-4e90-9dea-f8e9ab633562</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object AssociatedDomains.ConfigurationItem](associateddomains/configurationitem.md)
  A dictionary that maps apps to their associated domains.

## See Also

- [object AppLock](applock.md)
  The payload you use to configure a device to run a single app.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload you use to configure Autonomous Single App mode.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload you use to configure the extensions that the system allows or disallows to run on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/associateddomains)*