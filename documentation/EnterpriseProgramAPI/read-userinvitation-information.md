# Read user invitation information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a pending invitation to join your team.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/userInvitations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `fields[userInvitations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `email`, `expirationDate`, `firstName`, `lastName`, `roles`

## Responses

- `200` OK (`UserInvitationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Invited Users
- [List Invited Users](./list-invited-users.md)
  Get a list of pending invitations to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-userinvitation-information)*