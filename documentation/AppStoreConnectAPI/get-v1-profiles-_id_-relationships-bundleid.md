# Get the bundle ID for a profile

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles/{id}/relationships/bundleId`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`ProfileBundleIdLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Related Data
- [Read the bundle id in a profile](./get-v1-profiles-_id_-bundleid.md)
  Get the bundle ID information for a specific provisioning profile.
- [List all certificates in a profile](./get-v1-profiles-_id_-certificates.md)
  Get a list of all certificates and their data for a specific provisioning profile.
- [List certificate IDs for a profile](./get-v1-profiles-_id_-relationships-certificates.md)
- [List all devices in a profile](./get-v1-profiles-_id_-devices.md)
  Get a list of all devices for a specific provisioning profile.
- [List device IDs for a profile](./get-v1-profiles-_id_-relationships-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles-_id_-relationships-bundleid)*