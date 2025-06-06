# FDEFileVault

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure FileVault.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object FDEFileVault
```

#### Discussion

Specify `com.apple.MCX.FileVault2` as the payload type.

FileVault 2 performs full XTS-AES 128 encryption on the contents of a volume. Removing the FileVault payload doesn’t disable FileVault.

As of macOS 10.15, FileVault settings require supervision or user approval when installed manually.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | macOS |
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
            <key>Defer</key>
            <true/>
            <key>Enable</key>
            <string>On</string>
            <key>ShowRecoveryKey</key>
            <true/>
            <key>UseKeychain</key>
            <false/>
            <key>UseRecoveryKey</key>
            <true/>
            <key>UserEntersMissingInfo</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myfdefilevaultpayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX.FileVault2</string>
            <key>PayloadUUID</key>
            <string>c2c5f5e9-8ffc-4d8f-9108-fd655b90fdb2</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>FDE File Vault</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>5ba0de0e-ff06-4c0b-8dca-f5b55ed9de86</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object FDEFileVaultOptions](fdefilevaultoptions.md)
  The payload you use to configure FileVault options.
- [object FDERecoveryKeyEscrow](fderecoverykeyescrow.md)
  The payload you use to configure FileVault recovery key escrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fdefilevault)*