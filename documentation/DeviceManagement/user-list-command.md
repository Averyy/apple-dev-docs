# User List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of users with active accounts on a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object UserListCommand](userlistcommand.md)
  The command to get a list of users with active accounts on a device.
- [object UserListResponse](userlistresponse.md)
  A response from the device after it processes the command to get a list of users with active accounts on a device.

## Request Body

The request object the server returns for the User List Command.

## See Also

- [Log Out User](log-out-user-command.md)
  Force the current user to log out of a device.
- [Delete User](delete-user-command.md)
  Delete a user’s account from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-list-command)*