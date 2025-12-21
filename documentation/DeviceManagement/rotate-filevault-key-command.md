# Rotate FileVault Key

**Framework**: Device Management  
**Kind**: httpRequest

Change the FileVault primary password on a device.

**Availability**:
- macOS 10.9+

#### Discussion

Change the FileVault password periodically to mitigate the security risk of deployed devices.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | DeviceLockAndRemovePasscode |

##### Example Request and Response

## Topics

### Commands and responses
- [object RotateFileVaultKeyCommand](rotatefilevaultkeycommand.md)
  The command to change the FileVault primary password on a device.
- [object RotateFileVaultKeyResponse](rotatefilevaultkeyresponse.md)
  A response from the device after it processes the command to change the FileVault primary password on a device.

## Request Body

The request object the server returns for the Rotate FileVault Key Command.

## See Also

- [Security Info](security-info-command.md)
  Get security-related information about a device.
- [Certificate List](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Activation Lock Bypass Code](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear Activation Lock Bypass Code](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotate-filevault-key-command)*