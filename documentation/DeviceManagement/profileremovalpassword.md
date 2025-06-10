# ProfileRemovalPassword

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure profile removal.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
object ProfileRemovalPassword
```

#### Discussion

Specify `com.apple.profileRemovalPassword` as the payload type.

This payload provides a password to allow users to remove a locked configuration profile from the device. If this payload is present and has a password value set, the device asks for the password when the user taps a profile’s Remove button. This system encrypts the payload with the rest of the profile.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, tvOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS |
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
            <key>RemovalPassword</key>
            <string>Password123</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myprofileremovalpasswordprofile</string>
            <key>PayloadType</key>
            <string>com.apple.profileRemovalPassword</string>
            <key>PayloadUUID</key>
            <string>55f87465-a869-4ab0-9031-11ca1073641b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Password Removal</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>a42bfe59-7f3a-46a0-9908-4a5095fd2c6d</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>HasRemovalPasscode</key>
    <true/>
</dict>
</plist>
```

## See Also

- [object EducationConfiguration](educationconfiguration.md)
  The payload you use to configure the users, groups, and departments within an educational organization.
- [object LightsOutManagementLOM](lightsoutmanagementlom.md)
  The payload you use to configure lights-out management (LOM) settings.
- [object ManagedPreferences](managedpreferences.md)
  The payload you use to configure managed preferences.
- [object MDM](mdm.md)
  The payload you use to configure mobile device management (MDM) settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profileremovalpassword)*