# Security Info

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

## Topics

### Commands and responses
- [object SecurityInfoCommand](securityinfocommand.md)
  The command to get security-related information about a device.
- [object SecurityInfoResponse](securityinforesponse.md)
  A response from the device after it processes the command to get security-related information about a device.

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