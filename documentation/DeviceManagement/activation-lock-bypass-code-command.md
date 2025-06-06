# Get the Bypass Code for Activation Lock

**Framework**: Device Management  
**Kind**: httpRequest

Get the code to bypass Activation Lock on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- macOS 10.15+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Creating and Using Bypass Codes](creating-and-using-bypass-codes.md)

#### Discussion

iOS 7.1 adds support for bypassing Activation Lock. This allows organizations to remove the Activation Lock from supervised devices prior to device activation without knowing the userʼs personal Apple ID and password. Use this command to retrieve the device’s bypass code.

When an iOS device is a supervised device, it generates a device-specific Activation Lock bypass code. The activation server verifies this code to bypass Activation Lock on the device. For more information, see [`Creating and Using Bypass Codes`](creating-and-using-bypass-codes.md).

A device creates a new bypass code when:

- Setting up the device the first time.
- Erasing and not restoring the device from a backup.
- Erasing and restoring the device from a backup from a different device.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS |
| User Channel | - |
| Requires Supervision | iOS, macOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object ActivationLockBypassCodeCommand](activationlockbypasscodecommand.md)
  The command to get the code to bypass Activation Lock on a device.
- [object ActivationLockBypassCodeResponse](activationlockbypasscoderesponse.md)
  A response from the device after it processes the command to get the Activation Lock bypass code.

## Request Body

The command to get the code to bypass Activation Lock on a device.

## See Also

- [Security Information](security-info-command.md)
  Get security-related information about a device.
- [List the Certificates](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Clear the Bypass Code for Activation Lock](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate the FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activation-lock-bypass-code-command)*