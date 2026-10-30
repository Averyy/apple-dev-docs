# Get Devices Enrolled in Apple Device Management Service

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of devices enrolled in Apple Device Management service.

**Availability**:
- Apple Business API 2.7+

## Topics

### Responses
- [object MdmDevicesResponse](./mdmdevicesresponse.md)
  A response that contains a list of Apple devices enrolled in a device management service.

## Endpoint

`GET https://api-business.apple.com/v1/mdmDevices`

## Parameters

### Query Parameters

- `fields[mdmDevices]` ([string]): The fields to return for included related types.

  **Allowed Values**: `serialNumber`, `deviceName`, `productFamily`, `enrolledUserId`, `details`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`

## Responses

- `200` OK (`MdmDevicesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Devices
- [Get Organization Devices](./get-org-devices.md)
  Get a list of devices in an organization that enroll using Automated Device Enrollment.
- [Get Device Information](./get-orgdevice-information.md)
  Get information about a device in an organization.
- [Get AppleCare coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
- [Get Details for a Device Enrolled in Apple Device Management Service](./get-the-details-for-apple-mdm-enrolled-device.md)
  Get detailed information about a device enrolled in Apple Device Management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-apple-mdm-enrolled-devices)*