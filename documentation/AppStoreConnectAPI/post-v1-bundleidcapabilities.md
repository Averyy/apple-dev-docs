# Enable a capability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Enable a capability for a bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/bundleIdCapabilities`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BundleIdCapabilityCreateRequest`

## Responses

- `201` Created (`BundleIdCapabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Enabling and Disabling Capabilities
- [Disable a capability](./delete-v1-bundleidcapabilities-_id_.md)
  Disable a capability for a bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-bundleidcapabilities)*