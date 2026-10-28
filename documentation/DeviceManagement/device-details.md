# Get Device Details

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the details on a set of devices.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

## Topics

### Request and Response
- [object DeviceListRequest](./devicelistrequest.md)
  The request for a list of devices.
- [object DeviceListResponse](./devicelistresponse.md)
- [object DeviceListResponse.Devices](./devicelistresponse/devices-data.dictionary.md)

## Endpoint

`POST https://mdmenrollment.apple.com/devices`

## Request Body

**Content-Type**: `application/json`  
**Type**: `DeviceListRequest`

The request for a list of devices.

## Responses

- `200` OK (`DeviceListResponse`, `application/json`)
- `400` Bad Request:

  - `DEVICE_ID_REQUIRED`: No device IDs (serial numbers) were provided.
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.

## See Also

### Device management
- [Activation Lock a Device](./activation-lock-devices.md)
  Enable activation lock on a remote device.
- [Get a List of Devices](./fetch-devices.md)
  Get a list of devices that are managed by the server.
- [Sync the List of Devices](./sync-devices.md)
  Get updates about the list of devices the server manages.
- [Disown Devices](./disown-devices.md)
  Notify Apple’s servers that your organization no longer owns the specified devices.
- [Get Replacement Details](./get-replacement-details.md)
  Get information about the device that a replacement device replaces.
- [Get Beta Enrollment Tokens](./get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-details)*