# List and Download Profiles

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list provisioning profiles and download their data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles`

## Parameters

### Query Parameters

- `fields[bundleIds]` ([string]): **Allowed Values**: `bundleIdCapabilities`, `identifier`, `name`, `platform`, `profiles`, `seedId`
- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[devices]` ([string]): **Allowed Values**: `addedDate`, `deviceClass`, `model`, `name`, `platform`, `status`, `udid`
- `fields[profiles]` ([string]): **Allowed Values**: `bundleId`, `certificates`, `createdDate`, `devices`, `expirationDate`, `name`, `platform`, `profileContent`, `profileState`, `profileType`, `uuid`
- `filter[id]` ([string])
- `filter[name]` ([string])
- `filter[profileState]` ([string]): **Allowed Values**: `ACTIVE`, `INVALID`
- `filter[profileType]` ([string]): **Allowed Values**: `IOS_APP_DEVELOPMENT`, `IOS_APP_STORE`, `IOS_APP_ADHOC`, `IOS_APP_INHOUSE`, `MAC_APP_DEVELOPMENT`, `MAC_APP_STORE`, `MAC_APP_DIRECT`, `TVOS_APP_DEVELOPMENT`, `TVOS_APP_STORE`, `TVOS_APP_ADHOC`, `TVOS_APP_INHOUSE`, `MAC_CATALYST_APP_DEVELOPMENT`, `MAC_CATALYST_APP_STORE`, `MAC_CATALYST_APP_DIRECT`
- `include` ([string]): **Allowed Values**: `bundleId`, `certificates`, `devices`
- `limit` (integer): **Maximum**: `200`
- `limit[certificates]` (integer): **Maximum**: `50`
- `limit[devices]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `id`, `-id`, `name`, `-name`, `profileState`, `-profileState`, `profileType`, `-profileType`

## Responses

- `200` OK (`ProfilesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Getting Provisioning Profile Information
- [Read and Download Profile Information](./read-and-download-profile-information.md)
  Get information for a specific provisioning profile and download its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-and-download-profiles)*