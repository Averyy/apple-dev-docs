# Get All Device IDs for a Device Management Service

**Framework**: AppleSchoolManagerAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Apple School Manager API 1.8+

## Endpoint

`GET https://api-school.apple.com/v1/mdmServers/{id}/relationships/devices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `1000`

## Responses

- `200` OK (`MdmServerDevicesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Device Management Services
- [Get Device Management Services](./get-device-management-services.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Get the Assigned Device Management Service ID for a Device](./get-the-assigned-device-management-service-id-for-an-orgdevice.md)
  Get the assigned device management service ID information for a device.
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-device-management-service-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, or manage a device management service for devices.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assigning or unassigning, creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/get-all-device-ids-for-a-device-management-service)*