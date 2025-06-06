# List the User Accounts

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of users with active accounts on a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

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
- [object UserListCommand](userlistcommand.md)
  The command to get a list of users with active accounts on a device.
- [object UserListResponse](userlistresponse.md)
  A response from the device after it processes the command to get a list of users with active accounts.

## Request Body

The command to get a list of users with active accounts on a device.

## See Also

- [Log Out the User](log-out-user-command.md)
  Force the current user to log out of a device.
- [Delete a User](delete-user-command.md)
  Delete a user’s account from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-list-command)*