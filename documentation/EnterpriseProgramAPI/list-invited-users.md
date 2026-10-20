# List Invited Users

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of pending invitations to join your team.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/userInvitations`

## Parameters

### Query Parameters

- `fields[userInvitations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `email`, `expirationDate`, `firstName`, `lastName`, `roles`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `email`, `-email`, `lastName`, `-lastName`
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `ADMIN`, `ACCOUNT_HOLDER`, `DEVELOPER`
- `filter[email]` ([string]): Attributes, relationships, and IDs by which to filter.

## Responses

- `200` OK (`UserInvitationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Getting Invited Users
- [Read user invitation information](./read-userinvitation-information.md)
  Get information about a pending invitation to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-invited-users)*