# Log Out the User

**Framework**: Device Management  
**Kind**: httpRequest

Force the current user to log out of a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

After logging out the user, MDM commands aren’t available on the device for up to 2 minutes.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | Shared iPad |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object LogOutUserCommand](logoutusercommand.md)
  The command to force the current user to log out of a device.
- [object LogOutUserResponse](logoutuserresponse.md)
  A response from the device after it processes the command to force the current user to log out.

## Request Body

The command to force the current user to log out of a device.

## See Also

- [List the User Accounts](user-list-command.md)
  Get a list of users with active accounts on a device.
- [Delete a User](delete-user-command.md)
  Delete a user’s account from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/log-out-user-command)*