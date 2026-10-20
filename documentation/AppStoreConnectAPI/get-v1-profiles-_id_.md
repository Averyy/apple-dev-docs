# Read and download profile information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific provisioning profile and download its data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[devices]` ([string]): **Allowed Values**: `name`, `platform`, `udid`, `deviceClass`, `status`, `model`, `addedDate`
- `fields[profiles]` ([string]): **Allowed Values**: `name`, `platform`, `profileType`, `profileState`, `profileContent`, `uuid`, `createdDate`, `expirationDate`, `bundleId`, `devices`, `certificates`
- `include` ([string]): **Allowed Values**: `bundleId`, `devices`, `certificates`
- `fields[bundleIds]` ([string]): **Allowed Values**: `name`, `platform`, `identifier`, `seedId`, `profiles`, `bundleIdCapabilities`, `app`
- `limit[devices]` (integer): **Maximum**: `50`
- `limit[certificates]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`ProfileResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Provisioning Profile Information
- [List and download profiles](./get-v1-profiles.md)
  Find and list provisioning profiles and download their data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles-_id_)*