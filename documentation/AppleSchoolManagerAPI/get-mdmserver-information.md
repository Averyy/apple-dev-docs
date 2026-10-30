# Get Device Management Service Information

**Framework**: AppleSchoolManagerAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the information for a specific device management service.

**Availability**:
- Apple School Manager API 1.8+

### Example

**Request**:

```
curl "https://api-school.apple.com/v1/mdmServers/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "mdmServers",
    "id": "1F97349736CF4614A94F624E705841AD",
    "attributes": {
      "serverName": "Classroom MDM",
      "serverType": "MDM",
      "enableMdmDisownFlag": false,
      "defaultProductFamilies": ["IPAD"],
      "status": "ACTIVE",
      "deviceCount": 250,
      "lastConnectedDateTime": "2026-06-01T08:14:23Z",
      "lastConnectedIp": "203.0.113.5",
      "createdDateTime": "2025-05-01T03:21:44Z",
      "updatedDateTime": "2026-05-12T11:02:18Z"
    },
    "relationships": {
      "devices": {
        "links": {
          "self": "https://api-school.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD/relationships/devices"
        }
      }
    },
    "links": {
      "self": "https://api-school.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD"
    }
  },
  "links": {
    "self": "https://api-school.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD"
  }
}
```

## Topics

### Responses
- [object MdmServerResponse](./mdmserverresponse.md)
  A response that contains a single device management service resource.

## Endpoint

`GET https://api-school.apple.com/v1/mdmServers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[mdmServers]` ([string]): The fields to return for the resource.

  **Allowed Values**: `serverName`, `enableMdmDisownFlag`, `defaultProductFamilies`, `status`, `serverType`, `deviceCount`, `lastConnectedDateTime`, `lastConnectedIp`, `createdDateTime`, `updatedDateTime`, `devices`

## Responses

- `200` OK (`MdmServerResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Device Management Services
- [Get Device Management Services](./get-device-management-services.md)
  Get a list of device management services in an organization.
- [Get All Device IDs for a Device Management Service](./get-all-device-ids-for-a-device-management-service.md)
- [Get the Assigned Device Management Service ID for a Device](./get-the-assigned-device-management-service-id-for-an-orgdevice.md)
  Get the assigned device management service ID information for a device.
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-device-management-service-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, or manage a device management service for devices.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assigning or unassigning, creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/get-mdmserver-information)*