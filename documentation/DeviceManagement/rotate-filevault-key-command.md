# Rotate the FileVault Key

**Framework**: Device Management  
**Kind**: httpRequest

Change the FileVault primary password on a device.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Change the FileVault password periodically to mitigate the security risk of deployed devices.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | DeviceLockAndRemovePasscode |

##### Example Request and Response Personal Recovery Key

##### Example Request and Response Institutional Recovery Key

## Topics

### Command and Response
- [object RotateFileVaultKeyCommand](rotatefilevaultkeycommand.md)
  The command to change the FileVault primary password.
- [object RotateFileVaultKeyResponse](rotatefilevaultkeyresponse.md)
  A response from the device after it processes the command to change the FileVault primary password.

## Request Body

The command to change the FileVault primary password on a device.

## See Also

- [Security Information](security-info-command.md)
  Get security-related information about a device.
- [List the Certificates](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Get the Bypass Code for Activation Lock](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear the Bypass Code for Activation Lock](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotate-filevault-key-command)*