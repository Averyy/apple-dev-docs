# Get Organization Device Activity Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for an organization device activity that a device management action, such as assign or unassign, creates.

**Availability**:
- Apple Business API 2.6+

#### Overview

> **Note**: This API supports fetching organization device activity information that the system creates for device management actions, such as assigning or unassigning devices to the device management service in the past 30 days.

**Request**:

```
curl "https://api-business.apple.com/v1/orgDeviceActivities/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
        "type": "orgDeviceActivities",
        "id": "84d7f133-b4a4-41be-ad0a-c2e4e53ea624",
        "attributes": {
          "status": "COMPLETED",
          "subStatus": "COMPLETED_WITH_SUCCESS",
          "createdDateTime": "2025-05-01T18:22:27.106Z",
          "completedDateTime": "2025-05-01T18:22:38.894Z",
          "downloadUrl": "https://store.blobstore.apple.com/4a7f73ecd1/1317ef485b3aea95ac80/9b5c028726eacaa1f3e2/ccfa60f6114198d48cc5/88c579b1995efc28cd36?response-content-disposition=attachment%3Bfilename%3D%22ABM-ActivityLog_May-1-2025_14-22-40.csv%22&response-content-type=application%2Foctet-stream&iCloudAccessKeyId=MACOSX_SU_ACCESS_KEY&Expires=1746123820&Signature=wrYW2gn7UZDM9aO3KOMqT8YWCBo%3D"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDeviceActivities/84d7f133-b4a4-41be-ad0a-c2e4e53ea624"
        }
      },
      "links": {
        "self": "https://api-business.apple.com/v1/orgDeviceActivities/84d7f133-b4a4-41be-ad0a-c2e4e53ea624"
      }
    }
```

## Topics

### Responses
- [object OrgDeviceActivityResponse](./orgdeviceactivityresponse.md)
  A response that contains a single organization device activity resource.

## Endpoint

`GET https://api-business.apple.com/v1/orgDeviceActivities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[orgDeviceActivities]` ([string]): The fields to return for included related types.

  **Allowed Values**: `status`, `subStatus`, `createdDateTime`, `completedDateTime`, `downloadUrl`

## Responses

- `200` OK (`OrgDeviceActivityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Device Management Services
- [Get Device Management Services](./get-mdm-servers.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Create a Device Management Service](./create-an-mdmserver.md)
  Create a new device management service in an organization.
- [Update a Device Management Service](./update-an-mdmserver.md)
  Update an existing device management service in an organization.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-orgdeviceactivity-information)*