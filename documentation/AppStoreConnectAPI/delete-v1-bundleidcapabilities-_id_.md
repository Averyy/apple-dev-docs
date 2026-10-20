# Disable a capability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Disable a capability for a bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/bundleIdCapabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Enabling and Disabling Capabilities
- [Enable a capability](./post-v1-bundleidcapabilities.md)
  Enable a capability for a bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-bundleidcapabilities-_id_)*