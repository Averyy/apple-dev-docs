# List Devices

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list devices registered to your team.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/devices`

## Parameters

### Query Parameters

- `fields[devices]` ([string]): **Allowed Values**: `addedDate`, `deviceClass`, `model`, `name`, `platform`, `status`, `udid`
- `filter[id]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`
- `filter[status]` ([string]): **Allowed Values**: `ENABLED`, `DISABLED`
- `filter[udid]` ([string])
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `id`, `-id`, `name`, `-name`, `platform`, `-platform`, `status`, `-status`, `udid`, `-udid`

## Responses

- `200` OK (`DevicesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Getting Device Information
- [Read Device Information](./read-device-information.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-devices)*