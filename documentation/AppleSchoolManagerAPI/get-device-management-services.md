# Get Device Management Services

**Framework**: AppleSchoolManagerAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of device management services in an organization.

**Availability**:
- Apple School Manager API 1.8+

### Example

**Request**:

```
curl "https://api-school.apple.com/v1/mdmServers?limit=1" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
  {
    "data": [
      {
        "type": "mdmServers",
        "id": "1F97349736CF4614A94F624E705841AD",
        "attributes": {
          "serverName": "Test Device Management Service",
          "serverType": "MDM",
          "createdDateTime": "2025-05-01T03:21:44.685Z",
          "updatedDateTime": "2025-05-01T03:21:46.284Z"
        },
        "relationships": {
          "devices": {
            "links": {
              "self": "https://api-school.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD/relationships/devices"
            }
          }
        }
      }
    ],
    "links": {
      "self": "https://api-school.apple.com/v1/mdmServers"
    },
    "meta": {
      "paging": {
        "limit": 100
      }
    }
  }
```

## Topics

### Responses
- [object MdmServersResponse](./mdmserversresponse.md)
  A response that contains a list of device management service resources.

## Endpoint

`GET https://api-school.apple.com/v1/mdmServers`

## Parameters

### Query Parameters

- `fields[mdmServers]` ([string]): The fields to return for included related types.

  **Allowed Values**: `serverName`, `enableMdmDisownFlag`, `defaultProductFamilies`, `status`, `serverType`, `deviceCount`, `lastConnectedDateTime`, `lastConnectedIp`, `createdDateTime`, `updatedDateTime`, `devices`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`

## Responses

- `200` OK (`MdmServersResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Device Management Services
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/get-device-management-services)*