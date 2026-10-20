# Read Device Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/devices/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[devices]` ([string]): **Allowed Values**: `addedDate`, `deviceClass`, `model`, `name`, `platform`, `status`, `udid`

## Responses

- `200` OK (`DeviceResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)

## See Also

### Getting Device Information
- [List Devices](./list-devices.md)
  Find and list devices registered to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-device-information)*