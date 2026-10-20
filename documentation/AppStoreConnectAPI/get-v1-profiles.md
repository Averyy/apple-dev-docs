# List and download profiles

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list provisioning profiles and download their data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles`

## Parameters

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[devices]` ([string]): **Allowed Values**: `name`, `platform`, `udid`, `deviceClass`, `status`, `model`, `addedDate`
- `fields[profiles]` ([string]): **Allowed Values**: `name`, `platform`, `profileType`, `profileState`, `profileContent`, `uuid`, `createdDate`, `expirationDate`, `bundleId`, `devices`, `certificates`
- `filter[id]` ([string])
- `filter[name]` ([string])
- `include` ([string]): **Allowed Values**: `bundleId`, `devices`, `certificates`
- `limit` (integer): **Maximum**: `200`
- `limit[certificates]` (integer): **Maximum**: `50`
- `limit[devices]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `name`, `-name`, `profileType`, `-profileType`, `profileState`, `-profileState`, `id`, `-id`
- `fields[bundleIds]` ([string]): **Allowed Values**: `name`, `platform`, `identifier`, `seedId`, `profiles`, `bundleIdCapabilities`, `app`
- `filter[profileState]` ([string]): **Allowed Values**: `ACTIVE`, `INVALID`
- `filter[profileType]` ([string]): **Allowed Values**: `IOS_APP_DEVELOPMENT`, `IOS_APP_STORE`, `IOS_APP_ADHOC`, `IOS_APP_INHOUSE`, `MAC_APP_DEVELOPMENT`, `MAC_APP_STORE`, `MAC_APP_DIRECT`, `TVOS_APP_DEVELOPMENT`, `TVOS_APP_STORE`, `TVOS_APP_ADHOC`, `TVOS_APP_INHOUSE`, `MAC_CATALYST_APP_DEVELOPMENT`, `MAC_CATALYST_APP_STORE`, `MAC_CATALYST_APP_DIRECT`

## Responses

- `200` OK (`ProfilesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Provisioning Profile Information
- [Read and download profile information](./get-v1-profiles-_id_.md)
  Get information for a specific provisioning profile and download its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles)*