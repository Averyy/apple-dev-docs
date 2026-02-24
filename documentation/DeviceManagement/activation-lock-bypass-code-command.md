# Activation Lock Bypass Code

**Framework**: Device Management  
**Kind**: httpRequest

Get the code to bypass Activation Lock on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- macOS 10.15+
- visionOS 2.0+

## Mentions

- [Creating and Using Bypass Codes](creating-and-using-bypass-codes.md)

#### Discussion

This command allows organizations to retrieve the device’s bypass code. Organizations can use the bypass code to remove the Activation Lock from supervised devices prior to device activation without knowing the user’s personal Apple Account and password.

Supervised devices generate a device-specific Activation Lock bypass code. The activation server verifies this code to bypass Activation Lock on the device. For more information, see [`Creating and Using Bypass Codes`](creating-and-using-bypass-codes.md).

A device creates a new bypass code when:

- Setting up the device the first time.
- Erasing and not restoring the device from a backup.
- Erasing and restoring the device from a backup from a different device.

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
        <string>ActivationLockBypassCode</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ActivationLockBypassCode</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ActivationLockBypassCode</key>
    <string>A8QK7-GFG21-6RHT-V0U9-756P-L7E3</string>
    <key>CommandUUID</key>
    <string>0001_ActivationLockBypassCode</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ActivationLockBypassCodeCommand](activationlockbypasscodecommand.md)
  The command to get the code to bypass Activation Lock on a device.
- [object ActivationLockBypassCodeResponse](activationlockbypasscoderesponse.md)
  A response from the device after it processes the command to get the code to bypass Activation Lock on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Activation Lock Bypass Code Command.

## See Also

- [Security Info](security-info-command.md)
  Get security-related information about a device.
- [Certificate List](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Clear Activation Lock Bypass Code](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activation-lock-bypass-code-command)*