# FDEFileVaultOptions

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure FileVault options.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object FDEFileVaultOptions
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
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
            <key>dontAllowFDEDisable</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myfdefvoptionspayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>0a8f4102-0fbf-4d8c-b1e1-3d916f89d927</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>FileVault 2 Options</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>92821df0-7c04-4366-b805-eb51ed87541b</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object FDEFileVault](fdefilevault.md)
  The payload you use to configure FileVault.
- [object FDERecoveryKeyEscrow](fderecoverykeyescrow.md)
  The payload you use to configure FileVault recovery key escrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fdefilevaultoptions)*