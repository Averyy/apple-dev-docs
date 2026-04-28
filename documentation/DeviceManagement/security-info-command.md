# Security Info

**Framework**: Device Management  
**Kind**: httpRequest

Get security-related information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowQuerySecurity |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>RequestType</key>
        <string>SecurityInfo</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_SecurityInfo</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CommandUUID</key>
    <string>0011_SecurityInfo</string>
    <key>SecurityInfo</key>
    <dict>
        <key>HardwareEncryptionCaps</key>
        <integer>3</integer>
        <key>ManagementStatus</key>
        <dict>
            <key>IsUserEnrollment</key>
            <false/>
        </dict>
        <key>PasscodeCompliant</key>
        <true/>
        <key>PasscodeCompliantWithProfiles</key>
        <true/>
        <key>PasscodeLockGracePeriod</key>
        <integer>0</integer>
        <key>PasscodeLockGracePeriodEnforced</key>
        <integer>0</integer>
        <key>PasscodePresent</key>
        <false/>
    </dict>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object SecurityInfoCommand](securityinfocommand.md)
  The command to get security-related information about a device.
- [object SecurityInfoResponse](securityinforesponse.md)
  A response from the device after it processes the command to get security-related information about a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#SecurityInfoCommand`

## Request Body

The request object the server returns for the Security Info Command.

## See Also

- [Certificate List](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Activation Lock Bypass Code](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear Activation Lock Bypass Code](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/security-info-command)*