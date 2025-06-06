# Delete a User

**Framework**: Device Management  
**Kind**: httpRequest

Delete a user’s account from a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS, Shared iPad |
| User Channel | - |
| Requires Supervision | macOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object DeleteUserCommand](deleteusercommand.md)
  The command to delete a user’s account from a device.
- [object DeleteUserResponse](deleteuserresponse.md)
  A response from the device after it processes the command to delete a user’s account.

## Request Body

The command to delete a user’s account from a device.

## See Also

- [List the User Accounts](user-list-command.md)
  Get a list of users with active accounts on a device.
- [Log Out the User](log-out-user-command.md)
  Force the current user to log out of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/delete-user-command)*