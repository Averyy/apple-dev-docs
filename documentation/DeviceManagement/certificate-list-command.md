# List the Certificates

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of installed certificates on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command allows the server to retrieve the list of installed certificates on the device. The command requires that the server has the Inspect Profile Manifest privilege. For user enrollment, this request returns only certificates pushed by MDM.

Starting with iOS 15.4, this command returns a Not Now response before the passcode-protected device’s first unlock after a device boots. Between iOS 15.0 and iOS 15.4, devices in that state didn’t respond with Not Now, but the response might not contain all identity certificates.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | AllowInspection |

##### Example Request and Response

## Topics

### Command and Response
- [object CertificateListCommand](certificatelistcommand.md)
  The command to get a list of installed certificates on a device.
- [object CertificateListResponse](certificatelistresponse.md)
  A response from the device after it processes the command to get a list of installed certificates.

## Request Body

The command to get a list of installed certificates on a device.

## See Also

- [Security Information](security-info-command.md)
  Get security-related information about a device.
- [Get the Bypass Code for Activation Lock](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear the Bypass Code for Activation Lock](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate the FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificate-list-command)*