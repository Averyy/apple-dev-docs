# Modify a Capability Configuration

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Enable a capability for a bundle ID.

#### Overview

- HTTPBody

## Endpoint

`POST https://api.enterprise.developer.apple.com/v1/bundleIdCapabilities`

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

## See Also

### Enabling and Disabling Capabilities
- [Disable a Capability](./delete-a-bundleidcapability.md)
  Disable a capability for a bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/create-a-bundleidcapability)*