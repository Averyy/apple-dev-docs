# SystemPolicyControl

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the system policy for assessments.

**Availability**:
- macOS 10.8+

## Declaration

```swift
object SystemPolicyControl
```

#### Discussion

Specify `com.apple.systempolicy.control` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowIdentifiedDevelopers</key>
            <true/>
            <key>EnableAssessment</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempolicycontrolpayload</string>
            <key>PayloadType</key>
            <string>com.apple.systempolicy.control</string>
            <key>PayloadUUID</key>
            <string>f26fc0a5-09f4-4d71-9a5c-6f1a7d30e905</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Policy Control</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>f379ac8d-8b9e-4e36-98e7-a43094d51e38</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object SystemPolicyKernelExtensions](systempolicykernelextensions.md)
  The payload you use to configure the kernel extension policies.
- [object SystemPolicyManaged](systempolicymanaged.md)
  The payload you use to configure the Finder’s contextual menu to bypass the system policy.
- [object SystemPolicyRule](systempolicyrule.md)
  The payload you use to configure the system policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempolicycontrol)*