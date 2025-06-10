# Restrictions

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure restrictions on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object Restrictions
```

#### Discussion

Specify `com.apple.applicationaccess` as the payload type.

> ❗ **Important**:  The system allows multiple Restrictions payloads. However, don’t attempt to manage the same restriction in different payloads. Doing so results in unexpected behavior.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>allowActivityContinuation</key>
            <false/>
            <key>blockedAppBundleIDs</key>
            <array>
                <string>com.apple.mobilesafari</string>
            </array>
            <key>ratingApps</key>
            <integer>500</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.myrestrictionspayload</string>
            <key>PayloadType</key>
            <string>com.apple.applicationaccess</string>
            <key>PayloadUUID</key>
            <string>53bec1be-ffec-4f88-acbd-b02aee8f04a9</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Restrictions</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>6020206c-12c2-4ada-987a-dd4c560ca73a</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictions)*