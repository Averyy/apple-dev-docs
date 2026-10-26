# Get the Assigned Device Management Service ID for a Device

**Framework**: AppleSchoolManagerAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the assigned device management service ID information for a device.

**Availability**:
- Apple School Manager API 1.7+

##### Example

**Request**:

```
curl "https://api-school.apple.com/v1/orgDevices/{id}/relationships/assignedServer" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
        "type": "mdmServers",
        "id": "1F97349736CF4614A94F624E705841AD"
      },
      "links": {
        "self": "https://api-school.apple.com/v1/orgDevices/XABC123X0ABC123X0/relationships/assignedServer",
        "related": "https://api-school.apple.com/v1/orgDevices/XABC123X0ABC123X0/assignedServer"
      }
    }
```

## Topics

### Responses
- [object OrgDeviceAssignedServerLinkageResponse](./orgdeviceassignedserverlinkageresponse.md)
  The data and links that describe the relationship between the resources.

## Endpoint

`GET https://api-school.apple.com/v1/orgDevices/{id}/relationships/assignedServer`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Responses

- `200` OK (`OrgDeviceAssignedServerLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Device Management Services
- [Get Device Management Services](./get-device-management-services.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Get All Device IDs for a Device Management Service](./get-all-device-ids-for-a-device-management-service.md)
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-device-management-service-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, or manage a device management service for devices.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assigning or unassigning, creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/get-the-assigned-device-management-service-id-for-an-orgdevice)*