# Disable a Capability

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Disable a capability for a bundle ID.

## Endpoint

`DELETE https://api.enterprise.developer.apple.com/v1/bundleIdCapabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: [missing]

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.

## See Also

### Enabling and Disabling Capabilities
- [Modify a Capability Configuration](./create-a-bundleidcapability.md)
  Enable a capability for a bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/delete-a-bundleidcapability)*