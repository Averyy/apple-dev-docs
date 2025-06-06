# Clear the Bypass Code for Activation Lock

**Framework**: Device Management  
**Kind**: httpRequest

Clear the Activation Lock bypass code on a device.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- macOS 10.15+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

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
- [object ClearActivationLockBypassCodeCommand](clearactivationlockbypasscodecommand.md)
  The command to clear the Activation Lock bypass code on a device.
- [object ClearActivationLockBypassCodeResponse](clearactivationlockbypasscoderesponse.md)
  A response from the device after it processes the command to clear the Activation Lock bypass code.

## Request Body

The command to clear the Activation Lock bypass code on a device.

## See Also

- [Security Information](security-info-command.md)
  Get security-related information about a device.
- [List the Certificates](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Get the Bypass Code for Activation Lock](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Rotate the FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-activation-lock-bypass-code-command)*