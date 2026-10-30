# Get Details for a Device Enrolled in Apple Device Management Service

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get detailed information about a device enrolled in Apple Device Management service.

**Availability**:
- Apple Business API 2.7+

## Topics

### Responses
- [object MdmDeviceDetailResponse](./mdmdevicedetailresponse.md)
  A response that contains the detailed information for an Apple device enrolled in a device management service.

## Endpoint

`GET https://api-business.apple.com/v1/mdmDevices/{id}/details`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[mdmDeviceDetails]` ([string]): The fields to return for included related types.

  **Allowed Values**: `serialNumber`, `deviceName`, `deviceModel`, `osVersion`, `platform`, `imei`, `meid`, `wifiMacAddress`, `bluetoothMacAddress`, `ethernetMacAddress`, `lastCheckInDateTime`, `isFirewallEnabled`, `isFileVaultEnabled`, `storageFreeCapacity`, `storageTotalCapacity`, `deviceLockStatus`, `deviceEraseStatus`, `lostModeStatus`

## Responses

- `200` OK (`MdmDeviceDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Devices
- [Get Organization Devices](./get-org-devices.md)
  Get a list of devices in an organization that enroll using Automated Device Enrollment.
- [Get Device Information](./get-orgdevice-information.md)
  Get information about a device in an organization.
- [Get AppleCare coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
- [Get Devices Enrolled in Apple Device Management Service](./get-apple-mdm-enrolled-devices.md)
  Get a list of devices enrolled in Apple Device Management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-the-details-for-apple-mdm-enrolled-device)*