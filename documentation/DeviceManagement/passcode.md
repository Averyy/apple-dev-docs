# Passcode

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a passcode policy.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- visionOS 2.0+
- watchOS 10.0+

## Declaration

```swift
object Passcode
```

#### Discussion

Specify `com.apple.mobiledevice.passwordpolicy` as the payload type.

The presence of this payload type causes the device to present the user with a passcode entry mechanism. The payload controls the complexity of the passcode.

For user enrollments, the system allows this payload type, but ignores most of the keys. Instead, the presence of the payload forces only these settings:

- `allowSimple`: always set to `false`
- `forcePIN`: always set to `true`
- `minLength`: always set to `6`
- `maxInactivity`: if this key is present its value is ignored, but the `never` option is removed in the Settings UI.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | iOS, macOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>allowSimple</key>
            <true/>
            <key>forcePIN</key>
            <true/>
            <key>maxFailedAttempts</key>
            <integer>5</integer>
            <key>maxGracePeriod</key>
            <integer>1</integer>
            <key>maxInactivity</key>
            <integer>2</integer>
            <key>maxPINAgeInDays</key>
            <real>30</real>
            <key>minLength</key>
            <integer>8</integer>
            <key>pinHistory</key>
            <real>2</real>
            <key>requireAlphanumeric</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mypasscodepayload</string>
            <key>PayloadType</key>
            <string>com.apple.mobiledevice.passwordpolicy</string>
            <key>PayloadUUID</key>
            <string>2a8a75e5-d17d-44d5-b062-3cb92161af9f</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Passcode</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>e044f50d-ff67-4bcd-9f3f-d7b678091061</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Passcode.CustomRegex](passcode/customregex-data.dictionary.md)
  The regex defining the passcode policy.

## See Also

- [object SecurityPreferences](securitypreferences.md)
  The payload that configures security preferences.
- [object SmartCard](smartcard.md)
  The payload that configures a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcode)*