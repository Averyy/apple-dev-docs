# List devices

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list devices registered to your team.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/devices`

## Parameters

### Query Parameters

- `fields[devices]` ([string]): **Allowed Values**: `name`, `platform`, `udid`, `deviceClass`, `status`, `model`, `addedDate`
- `filter[id]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `UNIVERSAL`
- `filter[status]` ([string]): **Allowed Values**: `ENABLED`, `DISABLED`
- `filter[udid]` ([string])
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `name`, `-name`, `platform`, `-platform`, `udid`, `-udid`, `status`, `-status`, `id`, `-id`

## Responses

- `200` OK (`DevicesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Device Information
- [Read device information](./get-v1-devices-_id_.md)
  Get information for a specific device registered to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-devices)*