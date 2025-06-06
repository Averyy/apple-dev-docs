# SystemPolicyManaged

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the Finder’s contextual menu to bypass the system policy.

**Availability**:
- macOS 10.8+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SystemPolicyManaged
```

#### Discussion

Specify `com.apple.systempolicy.managed` as the payload type.

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
            <key>DisableOverride</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempolicymanagedpayload</string>
            <key>PayloadType</key>
            <string>com.apple.systempolicy.managed</string>
            <key>PayloadUUID</key>
            <string>4ceaeaba-dfb9-4eb2-a641-a89c472856f0</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Policy Managed</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>4899fa10-e6e6-4d74-9fa3-64a2feb57c8e</string>
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
- [object SystemPolicyRule](systempolicyrule.md)
  The payload you use to configure the system policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempolicymanaged)*