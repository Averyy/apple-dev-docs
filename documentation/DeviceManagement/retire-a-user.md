# Retire a User

**Framework**: Device Management  
**Kind**: httpRequest

Retire a user account.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This service disassociates a VPP user from its iTunes account and releases the revocable licenses associated with the VPP user. The revoked licenses can then be assigned to other users in the organization.

Currently, ebook licenses are irrevocable.

A retired VPP user can be reregistered, in the same organization, using the [`Register a User`](register-a-user.md) endpoint.

##### Example Request and Response

## Topics

### Request and Response
- [object RetireVppUserRequest](retirevppuserrequest.md)
  The request to retire a user.
- [object RetireVppUserResponse](retirevppuserresponse.md)
  The response from retiring a user.

## Request Body

missing

## See Also

- [Get a User](get-a-user.md)
  Get information about a particular user.
- [Get Users](get-users-5boi1.md)
  Get information about a set of users.
- [Register a User](register-a-user.md)
  Register a user with the volume-purchase program.
- [Edit a User](edit-a-user.md)
  Modify details about a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retire-a-user)*