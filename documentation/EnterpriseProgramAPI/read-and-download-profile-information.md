# Read and Download Profile Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific provisioning profile and download its data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[bundleIds]` ([string]): **Allowed Values**: `bundleIdCapabilities`, `identifier`, `name`, `platform`, `profiles`, `seedId`
- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[devices]` ([string]): **Allowed Values**: `addedDate`, `deviceClass`, `model`, `name`, `platform`, `status`, `udid`
- `fields[profiles]` ([string]): **Allowed Values**: `bundleId`, `certificates`, `createdDate`, `devices`, `expirationDate`, `name`, `platform`, `profileContent`, `profileState`, `profileType`, `uuid`
- `include` ([string]): **Allowed Values**: `bundleId`, `certificates`, `devices`
- `limit[certificates]` (integer): **Maximum**: `50`
- `limit[devices]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`ProfileResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Provisioning Profile Information
- [List and Download Profiles](./list-and-download-profiles.md)
  Find and list provisioning profiles and download their data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-and-download-profile-information)*