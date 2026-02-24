# Clear Activation Lock Bypass Code

**Framework**: Device Management  
**Kind**: httpRequest

Clear the Activation Lock bypass code on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- macOS 10.15+
- visionOS 2.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS |
| User channel | NA |
| Requires supervision | iOS, macOS, visionOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

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
        <string>ClearActivationLockBypassCode</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ClearActivationLockBypassCode</string>
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
    <string>0001_ClearActivationLockBypassCode</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ClearActivationLockBypassCodeCommand](clearactivationlockbypasscodecommand.md)
  The command to clear the Activation Lock bypass code on a device.
- [object ClearActivationLockBypassCodeResponse](clearactivationlockbypasscoderesponse.md)
  A response from the device after it processes the command to clear the Activation Lock bypass code on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Clear Activation Lock Bypass Code Command.

## See Also

- [Security Info](security-info-command.md)
  Get security-related information about a device.
- [Certificate List](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Activation Lock Bypass Code](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Rotate FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-activation-lock-bypass-code-command)*