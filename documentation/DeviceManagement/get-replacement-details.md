# Get Replacement Details

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the device that a replacement device replaces.

## Discussion

This endpoint returns the original device serial number and replacement date for a replacement device. Call this endpoint only when the device’s `is_replacement_device` field is `true` in the response from [`Get a List of Devices`](./fetch-devices.md), [`Sync the List of Devices`](./sync-devices.md), or [`Get Device Details`](./device-details.md). Calling it for a device whose `is_replacement_device` value is `false` returns HTTP 404 `DEVICE_NOT_FOUND`.

This request requires `X-Server-Protocol-Version` 10 or later.

## Topics

### Response
- [object GetReplacementDetailsResponse](./getreplacementdetailsresponse.md)
  Information about a replacement device, including the original device it replaces and the date the replacement occurred.

## Endpoint

`GET https://mdmenrollment.apple.com/device/replacementDetails`

## Parameters

### Query Parameters

- `device` (string) *(required)*: The serial number of the replacement device.

## Responses

- `200` OK (`GetReplacementDetailsResponse`, `application/json`)
- `400` Bad Request:

  - `DEVICE_ID_REQUIRED`: No device serial number was provided as a query parameter.
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.
- `404` Not Found:

  - `DEVICE_NOT_FOUND`: No replacement record was found for the specified device. The serial number is invalid, the device isn’t a replacement device, or the device isn’t accessible by this MDM server.

## See Also

### Device management
- [Activation Lock a Device](./activation-lock-devices.md)
  Enable activation lock on a remote device.
- [Get Device Details](./device-details.md)
  Get the details on a set of devices.
- [Get a List of Devices](./fetch-devices.md)
  Get a list of devices that are managed by the server.
- [Sync the List of Devices](./sync-devices.md)
  Get updates about the list of devices the server manages.
- [Disown Devices](./disown-devices.md)
  Notify Apple’s servers that your organization no longer owns the specified devices.
- [Get Beta Enrollment Tokens](./get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-replacement-details)*