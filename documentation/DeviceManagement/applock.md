# AppLock

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a device to run a single app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- tvOS 10.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AppLock
```

#### Discussion

Specify `com.apple.app.lock` as the payload type.

With an app lock profile, the device locks to the specified app until removal of the profile. The home button is in a disabled state, and the device returns to the app automatically upon wake or restart.

Only use an app lock payload after installing the target app.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, tvOS |
| User Channel | - |
| Allow Manual Install | - |
| Requires Supervision | iOS, tvOS |
| Requires User Approved MDM | - |
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
            <key>App</key>
            <dict>
                <key>Identifier</key>
                <string>com.apple.mobilenotes</string>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.myapplockpayload</string>
            <key>PayloadType</key>
            <string>com.apple.app.lock</string>
            <key>PayloadUUID</key>
            <string>dc0c6fdd-aae0-4fd0-a19c-861ba28f4c55</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Single App Mode</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>736f867e-3972-4889-aa68-7ce5be12eff6</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object AppLock.App](applock/app-data.dictionary.md)
  The only app available for use on the iOS device.

## See Also

- [object AssociatedDomains](associateddomains.md)
  The payload you use to configure associated domains.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload you use to configure Autonomous Single App mode.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload you use to configure the extensions that the system allows or disallows to run on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applock)*