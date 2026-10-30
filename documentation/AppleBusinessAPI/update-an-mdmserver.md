# Update a Device Management Service

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update an existing device management service in an organization.

**Availability**:
- Apple Business API 2.7+

## Overview

> **Note**: Only the fields included in the request are updated. Any omitted fields retain their existing values.

### Example

**Request**:

```
curl -X PATCH "https://api-business.apple.com/v1/mdmServers/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "mdmServers",
        "id": "2A87349736CF4614A94F624E705841BE",
        "attributes": {
          "serverName": "Marketing Team MDM (Renamed)",
          "defaultProductFamilies": ["IPAD", "IPHONE"]
        }
      }
    }'
```

**Response**:

```json
{
  "data": {
    "type": "mdmServers",
    "id": "2A87349736CF4614A94F624E705841BE",
    "attributes": {
      "serverName": "Marketing Team MDM (Renamed)",
      "serverType": "MDM",
      "enableMdmDisownFlag": true,
      "defaultProductFamilies": ["IPAD", "IPHONE"],
      "status": "ACTIVE",
      "deviceCount": 42,
      "lastConnectedDateTime": "2026-06-01T08:14:23Z",
      "lastConnectedIp": "203.0.113.5",
      "createdDateTime": "2026-06-01T10:30:00Z",
      "updatedDateTime": "2026-06-01T14:22:00Z"
    },
    "relationships": {
      "devices": {
        "links": {
          "self": "https://api-business.apple.com/v1/mdmServers/2A87349736CF4614A94F624E705841BE/relationships/devices"
        }
      }
    },
    "links": {
      "self": "https://api-business.apple.com/v1/mdmServers/2A87349736CF4614A94F624E705841BE"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/mdmServers/2A87349736CF4614A94F624E705841BE"
  }
}
```

## Topics

### Responses
- [object MdmServerResponse](./mdmserverresponse.md)
  A response that contains a single device management service resource.

## Endpoint

`PATCH https://api-business.apple.com/v1/mdmServers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `MdmServerUpdateRequest`

## Responses

- `200` OK (`MdmServerResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `422` (`ErrorResponse`, `application/json`): Unprocessable request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Device Management Services
- [Get Device Management Services](./get-mdm-servers.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Create a Device Management Service](./create-an-mdmserver.md)
  Create a new device management service in an organization.
- [Delete a Device Management Service](./delete-an-mdmserver.md)
  Delete a device management service from an organization.
- [Get the Device Serial Numbers for a Device Management Service](./get-all-device-ids-for-an-mdmserver.md)
  Get a list of device serial numbers assigned to a device management service.
- [Get the Assigned Device Management Service ID for a Device](./get-the-assigned-server-id-for-an-orgdevice.md)
  Get the assigned device management service ID information for a device.
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-server-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service or Release Devices](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, manage a device management service migration for devices, or release devices from an organization.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assign or unassign, creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/update-an-mdmserver)*