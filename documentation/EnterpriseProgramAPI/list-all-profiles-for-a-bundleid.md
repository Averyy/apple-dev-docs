# List All Profiles for a BundleId

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all profiles for a specific bundle ID.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/bundleIds/{id}/profiles`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[profiles]` ([string]): **Allowed Values**: `bundleId`, `certificates`, `createdDate`, `devices`, `expirationDate`, `name`, `platform`, `profileContent`, `profileState`, `profileType`, `uuid`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`ProfilesWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Related Data
- [List All Bundle Id Capabilities for a BundleId](./list-all-bundle-id-capabilities-for-a-bundleid.md)
  Get a list of all capabilities for a specific bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-all-profiles-for-a-bundleid)*