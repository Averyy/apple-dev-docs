# Read the Bundle ID in a Profile

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the bundle ID information for a specific provisioning profile.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles/{id}/bundleId`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[bundleIds]` ([string]): **Allowed Values**: `bundleIdCapabilities`, `identifier`, `name`, `platform`, `profiles`, `seedId`

## Responses

- `200` OK (`BundleIdWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Related Data
- [List All Certificates in a Profile](./list-all-certificates-in-a-profile.md)
  Get a list of all certificates and their data for a specific provisioning profile.
- [List All Devices in a Profile](./list-all-devices-in-a-profile.md)
  Get a list of all devices for a specific provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-the-bundle-id-in-a-profile)*