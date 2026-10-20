# Delete a Profile

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a provisioning profile that is used for app development or distribution.

#### Discussion

You can delete provisioning profiles, and may wish to do so if they are expiring or obsolete.

## Endpoint

`DELETE https://api.enterprise.developer.apple.com/v1/profiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.

## See Also

### Creating and Deleting Provisioning Profiles
- [Create a Profile](./create-a-profile.md)
  Create a new provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/delete-a-profile)*