# List All Devices in a Profile

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all devices for a specific provisioning profile.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles/{id}/devices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[devices]` ([string]): **Allowed Values**: `addedDate`, `deviceClass`, `model`, `name`, `platform`, `status`, `udid`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`DevicesWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Related Data
- [Read the Bundle ID in a Profile](./read-the-bundle-id-in-a-profile.md)
  Get the bundle ID information for a specific provisioning profile.
- [List All Certificates in a Profile](./list-all-certificates-in-a-profile.md)
  Get a list of all certificates and their data for a specific provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-all-devices-in-a-profile)*