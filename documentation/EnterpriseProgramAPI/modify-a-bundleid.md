# Modify a PassTypeId

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific bundle ID’s name.

#### Overview

- HTTPBody

## Endpoint

`PATCH https://api.enterprise.developer.apple.com/v1/bundleIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `BundleIdUpdateRequest`

## Responses

- `200` OK (`BundleIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)

## See Also

### Modifying and Removing Bundle IDs
- [Delete a BundleId](./delete-a-bundleid.md)
  Delete a bundle ID that is used for app development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/modify-a-bundleid)*