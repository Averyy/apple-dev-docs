# Delete a BundleId

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a bundle ID that is used for app development.

## Endpoint

`DELETE https://api.enterprise.developer.apple.com/v1/bundleIds/{id}`

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

### Modifying and Removing Bundle IDs
- [Modify a PassTypeId](./modify-a-bundleid.md)
  Update a specific bundle ID’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/delete-a-bundleid)*