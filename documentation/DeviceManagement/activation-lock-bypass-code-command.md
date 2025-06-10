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

This command allows organizations to remove the Activation Lock from supervised devices prior to device activation without knowing the user’s personal Apple Account and password. Use this command to retrieve the device’s bypass code.

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

## Topics

### Commands and responses
- [object ActivationLockBypassCodeCommand](activationlockbypasscodecommand.md)
  The command to get the code to bypass Activation Lock on a device.
- [object ActivationLockBypassCodeResponse](activationlockbypasscoderesponse.md)
  A response from the device after it processes the command to get the code to bypass Activation Lock on a device.

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