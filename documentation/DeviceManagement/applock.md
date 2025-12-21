# AppLock

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a device to run a single app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- tvOS 10.2+

## Declaration

```swift
object AppLock
```

#### Discussion

Specify `com.apple.app.lock` as the payload type.

With an app lock profile, the device locks to the specified app until removal of the profile. The device returns to the app automatically upon wake or restart.

Only use an app lock payload after installing the target app.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS |
| User channel | NA |
| Allow manual install | iOS, tvOS |
| Requires supervision | iOS, tvOS |
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

### Objects
- [object AppLock.App](applock/app-data.dictionary.md)
  The only app available for use on the iOS device.

## See Also

- [object AssociatedDomains](associateddomains.md)
  The payload that configures associated domains.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload that configures Autonomous Single App mode.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload that configures the extensions that the system allows or disallows to run on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applock)*