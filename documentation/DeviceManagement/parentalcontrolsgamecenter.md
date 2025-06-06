# ParentalControlsGameCenter

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Game Center parental controls.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ParentalControlsGameCenter
```

#### Discussion

Specify `com.apple.gamed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
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
            <key>GKFeatureAccountModificationAllowed</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mygamecenterpayload</string>
            <key>PayloadType</key>
            <string>com.apple.gamed</string>
            <key>PayloadUUID</key>
            <string>2967fc4d-2ab8-40db-8f3e-f6f4cfe3e408</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Parental Control Game Center</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>73f89c96-6383-4db9-b879-9cc5bb8d9ad3</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ParentalControlsApplicationRestrictions](parentalcontrolsapplicationrestrictions.md)
  The payload you use to configure parental controls for apps.
- [object ParentalControlsContentFilter](parentalcontrolscontentfilter.md)
  The payload you use to configure the parental control web content filters.
- [object ParentalControlsDictionary](parentalcontrolsdictionary.md)
  The payload you use to configure parental control dictionary restrictions.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload you use to configure parental control time limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsgamecenter)*