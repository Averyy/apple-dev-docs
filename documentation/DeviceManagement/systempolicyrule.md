# SystemPolicyRule

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the system policy.

**Availability**:
- macOS 10.8+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SystemPolicyRule
```

#### Discussion

Specify `com.apple.systempolicy.rule` as the payload type.

This payload allows control over Gatekeeper’s system policy rules. The keys and functionality are tightly related to the `spctl` command line tool. For more information, see the manual page for `spctl`.

This payload must only exist in a device profile. If the payload is present in a user profile, an error is generated during installation and the profile installation fails.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
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
            <key>Priority</key>
            <real>101</real>
            <key>Requirement</key>
            <string>anchor apple generic and identifier "com.example.myapp" and (certificate leaf[field.9.8.765.432109.876.5.4.3] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.9.8.765.432109.876.5.4.3] /* exists */ and certificate leaf[subject.OU] = "ABCDE12345")</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempolicyrulepayload</string>
            <key>PayloadType</key>
            <string>com.apple.systempolicy.rule</string>
            <key>PayloadUUID</key>
            <string>624b5152-a1cd-4bac-baa3-51fbb1f04973</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Policy Rule</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>7fa54f02-e6e1-4042-bb75-a2a4d962ac6d</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object SystemPolicyControl](systempolicycontrol.md)
  The payload you use to configure the system policy for assessments.
- [object SystemPolicyKernelExtensions](systempolicykernelextensions.md)
  The payload you use to configure the kernel extension policies.
- [object SystemPolicyManaged](systempolicymanaged.md)
  The payload you use to configure the Finder’s contextual menu to bypass the system policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempolicyrule)*