# List Bundle Ids

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list bundle IDs that are registered to your team.

## Mentions

- [Generating Tokens for API Requests](./generating-tokens-for-api-requests.md)

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/bundleIds`

## Parameters

### Query Parameters

- `fields[bundleIdCapabilities]` ([string]): **Allowed Values**: `bundleId`, `capabilityType`, `settings`
- `fields[bundleIds]` ([string]): **Allowed Values**: `bundleIdCapabilities`, `identifier`, `name`, `platform`, `profiles`, `seedId`
- `fields[profiles]` ([string]): **Allowed Values**: `bundleId`, `certificates`, `createdDate`, `devices`, `expirationDate`, `name`, `platform`, `profileContent`, `profileState`, `profileType`, `uuid`
- `filter[id]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`
- `filter[seedId]` ([string])
- `include` ([string]): **Allowed Values**: `bundleIdCapabilities`, `profiles`
- `limit` (integer): **Maximum**: `200`
- `limit[bundleIdCapabilities]` (integer): **Maximum**: `50`
- `limit[profiles]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `id`, `-id`, `identifier`, `-identifier`, `name`, `-name`, `platform`, `-platform`, `seedId`, `-seedId`

## Responses

- `200` OK (`BundleIdsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Getting Bundle ID Information
- [Read BundleId Information](./read-bundleid-information.md)
  Get information about a specific bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-bundle-ids)*