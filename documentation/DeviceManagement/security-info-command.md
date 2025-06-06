# Security Information

**Framework**: Device Management  
**Kind**: httpRequest

Get security-related information about a device.

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

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | AllowQuerySecurity |

##### Example Request and Response

## Topics

### Command and Response
- [object SecurityInfoCommand](securityinfocommand.md)
  The command to get security-related information about a device.
- [object SecurityInfoResponse](securityinforesponse.md)
  A response from the device after it processes the command to get security-related information.

## Request Body

The command to get security-related information about a device.

## See Also

- [List the Certificates](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Get the Bypass Code for Activation Lock](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear the Bypass Code for Activation Lock](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate the FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/security-info-command)*