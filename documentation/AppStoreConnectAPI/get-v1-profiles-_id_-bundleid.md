# Read the bundle id in a profile

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the bundle ID information for a specific provisioning profile.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles/{id}/bundleId`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[bundleIds]` ([string]): **Allowed Values**: `name`, `platform`, `identifier`, `seedId`, `profiles`, `bundleIdCapabilities`, `app`

## Responses

- `200` OK (`BundleIdWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Related Data
- [Get the bundle ID for a profile](./get-v1-profiles-_id_-relationships-bundleid.md)
- [List all certificates in a profile](./get-v1-profiles-_id_-certificates.md)
  Get a list of all certificates and their data for a specific provisioning profile.
- [List certificate IDs for a profile](./get-v1-profiles-_id_-relationships-certificates.md)
- [List all devices in a profile](./get-v1-profiles-_id_-devices.md)
  Get a list of all devices for a specific provisioning profile.
- [List device IDs for a profile](./get-v1-profiles-_id_-relationships-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles-_id_-bundleid)*