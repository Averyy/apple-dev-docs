# Invite to the Program

**Framework**: Device Management  
**Kind**: httpRequest

Invite a user to join the Volume Purchase Program (VPP).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | Shared iPad, macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object InviteToProgramCommand](invitetoprogramcommand.md)
  The command to invite a user on a device to join the Volume Purchase Program (VPP).
- [object InviteToProgramResponse](invitetoprogramresponse.md)
  A response from the device after it processes the command to invite a user to join the Volume Purchase Program (VPP).

## Request Body

The command to invite a user on a device to join the Volume Purchase Program (VPP).

## See Also

- [Account Configuration](account-configuration-command.md)
  Create and configure a local administrator account on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/invite-to-program-command)*