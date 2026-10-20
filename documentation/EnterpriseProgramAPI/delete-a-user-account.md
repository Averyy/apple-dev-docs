# Delete a User Account

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a user from your team.

## Endpoint

`DELETE https://api.enterprise.developer.apple.com/v1/users/{id}`

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

### Modifying and Removing User Accounts
- [Modify a User Account](./modify-a-user-account.md)
  Change a user’s role, app visibility information, or other account details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/delete-a-user-account)*