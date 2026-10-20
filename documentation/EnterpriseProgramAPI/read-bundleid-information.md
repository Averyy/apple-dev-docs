# Read BundleId Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific bundle ID.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/bundleIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[bundleIdCapabilities]` ([string]): **Allowed Values**: `bundleId`, `capabilityType`, `settings`
- `fields[bundleIds]` ([string]): **Allowed Values**: `bundleIdCapabilities`, `identifier`, `name`, `platform`, `profiles`, `seedId`
- `fields[profiles]` ([string]): **Allowed Values**: `bundleId`, `certificates`, `createdDate`, `devices`, `expirationDate`, `name`, `platform`, `profileContent`, `profileState`, `profileType`, `uuid`
- `include` ([string]): **Allowed Values**: `bundleIdCapabilities`, `profiles`
- `limit[bundleIdCapabilities]` (integer): **Maximum**: `50`
- `limit[profiles]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`BundleIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Bundle ID Information
- [List Bundle Ids](./list-bundle-ids.md)
  Find and list bundle IDs that are registered to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-bundleid-information)*