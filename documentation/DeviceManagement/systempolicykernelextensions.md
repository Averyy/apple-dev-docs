# SystemPolicyKernelExtensions

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the kernel extension policies.

**Availability**:
- macOS 10.13.2+

## Declaration

```swift
object SystemPolicyKernelExtensions
```

#### Discussion

Specify `com.apple.syspolicy.kernel-extension-policy` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | macOS |
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
            <key>AllowUserOverrides</key>
            <false/>
            <key>AllowedTeamIdentifiers</key>
            <array>
                <string>ABCDE12345</string>
            </array>
            <key>AllowedKernelExtensions</key>
            <dict>
                <key></key>
                <array>
                    <string>com.example.mydriver</string>
                </array>
                <key>ABCDE12345</key>
                <array>
                    <string>com.example.kext.mydriver</string>
                </array>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mysystempolicykernalextensionspayload</string>
            <key>PayloadType</key>
            <string>com.apple.syspolicy.kernel-extension-policy</string>
            <key>PayloadUUID</key>
            <string>3202f59b-3583-4e6c-82ae-776f3c815df1</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>System Policy Kernal Extension</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>d9fa7f5b-713d-48f8-a8bd-219cf3061873</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object SystemPolicyKernelExtensions.AllowedKernelExtensions](systempolicykernelextensions/allowedkernelextensions-data.dictionary.md)
  The dictionary that represents a set of kernel extensions.

## See Also

- [object SystemPolicyControl](systempolicycontrol.md)
  The payload that configures the system policy for assessments.
- [object SystemPolicyManaged](systempolicymanaged.md)
  The payload that configures the Finder’s contextual menu to bypass the system policy.
- [object SystemPolicyRule](systempolicyrule.md)
  The payload that configures the system policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systempolicykernelextensions)*