# Modify a BundleIdCapability

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the configuration of a specific capability.

#### Overview

- HTTPBody

## Endpoint

`PATCH https://api.enterprise.developer.apple.com/v1/bundleIdCapabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `BundleIdCapabilityUpdateRequest`

## Responses

- `200` OK (`BundleIdCapabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/modify-a-bundleidcapability)*