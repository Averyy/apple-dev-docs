# Invite To Program

**Framework**: Device Management  
**Kind**: httpRequest

Invite a user to join the Volume Purchase Program (VPP).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+

#### Discussion

This command allows a server to invite a user to join the Volume Purchase Program (VPP). It issues the invitation, but doesn’t allow the server to monitor whether the user joins the program. This command yields a `NotNow` status if Setup Assistant is running.

The command doesn’t work with Account Driven enrollments.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | macOS, Shared iPad |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object InviteToProgramCommand](invitetoprogramcommand.md)
  The command to invite a user to join the Volume Purchase Program (VPP).
- [object InviteToProgramResponse](invitetoprogramresponse.md)
  A response from the device after it processes the command to invite a user to join the Volume Purchase Program (VPP).

## Request Body

The request object the server returns for the Invite To Program Command.

## See Also

- [Account Configuration](account-configuration-command.md)
  Create and configure a local administrator account on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/invite-to-program-command)*