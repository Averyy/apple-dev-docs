# Cancel a User Invitation

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Cancel a pending invitation for a user to join your team.

## Endpoint

`DELETE https://api.enterprise.developer.apple.com/v1/userInvitations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.

## See Also

### Sending and Canceling Invitations
- [Invite a User](./invite-a-user.md)
  Invite a user with assigned user roles to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/cancel-a-user-invitation)*