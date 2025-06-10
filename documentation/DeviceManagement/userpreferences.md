# UserPreferences

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure iCloud password preferences.

**Availability**:
- macOS 10.12+

## Declaration

```swift
object UserPreferences
```

#### Discussion

Specify `com.apple.preference.users` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | macOS |
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
            <key>DisableUsingiCloudPassword</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myuserpayload</string>
            <key>PayloadType</key>
            <string>com.apple.preferences.users</string>
            <key>PayloadUUID</key>
            <string>733ec67c-853c-45b2-9510-198e055e0723</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>User</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>1a5fe077-6146-44ae-82db-5cb938dddad4</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object GlobalPreferences](globalpreferences.md)
  The payload you use to configure global preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userpreferences)*