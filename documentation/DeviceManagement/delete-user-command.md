# Delete User

**Framework**: Device Management  
**Kind**: httpRequest

Delete a user’s account from a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Error Codes

An error response uses one of the following error codes:

- `12071`: The user doesn’t exist.
- `12072`: The user is currently logged in.
- `12073`: The user has data to sync and ForceDeletion is false or unspecified.
- `12074`: Unable to delete the user. In macOS, this error code also returns for an attempt to delete the last administrator account.

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
- [object DeleteUserCommand](deleteusercommand.md)
  The command to delete a user’s account from a device.
- [object DeleteUserResponse](deleteuserresponse.md)
  A response from the device after it processes the command to delete a user’s account from a device.

## Request Body

The request object the server returns for the Delete User Command.

## See Also

- [User List](user-list-command.md)
  Get a list of users with active accounts on a device.
- [Log Out User](log-out-user-command.md)
  Force the current user to log out of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/delete-user-command)*