# Assign or Unassign Devices to a Device Management Service or Release Devices

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Assign or unassign devices to a device management service, manage a device management service migration for devices, or release devices from an organization.

**Availability**:
- Apple Business API 2.6+

### Example: Assign or Unassign Devices to a Device Management Service

**Request**:

```
curl -X POST https://api-business.apple.com/v1/orgDeviceActivities \
 -H "Authorization: Bearer ${ACCESS_TOKEN} \
 -d '{
   "data": {
     "type": "orgDeviceActivities",
     "attributes": {
       "activityType": "ASSIGN_DEVICES"
     },
     "relationships": {
       "mdmServer": {
         "data": {
           "type": "mdmServers",
           "id": "1F97349736CF4614A94F624E705841AD"
         }
       },
       "devices": {
         "data": [
           {
             "type": "orgDevices",
             "id": "XABC123X0ABC123X0"
           }
         ]
       }
     }
   }
 }'

```

**Response**:

```json
      {
  "data": {
    "type": "orgDeviceActivities",
    "id": "b1481656-b267-480d-b284-a809eed8b041",
    "attributes": {
      "status": "IN_PROGRESS",
      "subStatus": "SUBMITTED",
      "createdDateTime": "2025-05-05T04:15:43.282Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/orgDeviceActivities/b1481656-b267-480d-b284-a809eed8b041"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/orgDeviceActivities"
  }
}
```

### Example: Assign Devices to a Device Management Service With a Device Management Service Migration Deadline

To assign devices to a device management service and schedule a device management service migration, use the `ASSIGN_DEVICES_WITH_MDM_MIGRATION_DEADLINE` activity type and include `activityTypeMetadata.mdmMigrationDeadlineDateTime`, an ISO 8601 date and time by which the migration needs to complete. The deadline can’t be more than 90 days in the future.

**Request**:

```
curl -X POST https://api-business.apple.com/v1/orgDeviceActivities \
 -H "Authorization: Bearer ${ACCESS_TOKEN} \
 -d '{
   "data": {
     "type": "orgDeviceActivities",
     "attributes": {
       "activityType": "ASSIGN_DEVICES_WITH_MDM_MIGRATION_DEADLINE",
       "activityTypeMetadata": {
         "mdmMigrationDeadlineDateTime": "2026-03-15T17:00:00.000Z"
       }
     },
     "relationships": {
       "mdmServer": {
         "data": {
           "type": "mdmServers",
           "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
         }
       },
       "devices": {
         "data": [
           {
             "type": "orgDevices",
             "id": "C39J8W1H3VG5"
           },
           {
             "type": "orgDevices",
             "id": "F2KZ3N4G5HD3"
           }
         ]
       }
     }
   }
 }'

```

**Response**:

```json
{
  "data": {
    "type": "orgDeviceActivities",
    "id": "f7e6d5c4-b3a2-1098-fedc-ba9876543210",
    "attributes": {
      "status": "IN_PROGRESS",
      "subStatus": "SUBMITTED",
      "createdDateTime": "2026-02-27T18:00:00.000Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/orgDeviceActivities/f7e6d5c4-b3a2-1098-fedc-ba9876543210"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/orgDeviceActivities"
  }
}
```

### Example: Update a Device Management Service Migration Deadline

To update the deadline for an in-progress device management service migration, use the `UPDATE_MDM_MIGRATION_DEADLINE` activity type. This doesn’t require a `mdmServer` relationship. If the new deadline is earlier than the existing one, or in the past, the device honors it without giving the user an option to delay the migration.

**Request**:

```
curl -X POST https://api-business.apple.com/v1/orgDeviceActivities \
 -H "Authorization: Bearer ${ACCESS_TOKEN} \
 -d '{
   "data": {
     "type": "orgDeviceActivities",
     "attributes": {
       "activityType": "UPDATE_MDM_MIGRATION_DEADLINE",
       "activityTypeMetadata": {
         "mdmMigrationDeadlineDateTime": "2026-03-15T17:00:00.000Z"
       }
     },
     "relationships": {
       "devices": {
         "data": [
           {
             "type": "orgDevices",
             "id": "C39J8W1H3VG5"
           },
           {
             "type": "orgDevices",
             "id": "F2KZ3N4G5HD3"
           }
         ]
       }
     }
   }
 }'

```

**Response**:

```json
{
  "data": {
    "type": "orgDeviceActivities",
    "id": "f7e6d5c4-b3a2-1098-fedc-ba9876543210",
    "attributes": {
      "status": "IN_PROGRESS",
      "subStatus": "SUBMITTED",
      "createdDateTime": "2026-02-27T18:00:00.000Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/orgDeviceActivities/f7e6d5c4-b3a2-1098-fedc-ba9876543210"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/orgDeviceActivities"
  }
}
```

If the request tries to update the deadline for a serial number that isn’t undergoing a device management service migration, the activity log result indicates a failure for that serial number.

### Example: Cancel an MDM Migration

To cancel an in-progress device management service migration, use the `CANCEL_MDM_MIGRATION` activity type. This doesn’t require a `mdmServer` relationship or `activityTypeMetadata`.

**Request**:

```
curl -X POST https://api-business.apple.com/v1/orgDeviceActivities \
 -H "Authorization: Bearer ${ACCESS_TOKEN} \
 -d '{
   "data": {
     "type": "orgDeviceActivities",
     "attributes": {
       "activityType": "CANCEL_MDM_MIGRATION"
     },
     "relationships": {
       "devices": {
         "data": [
           {
             "type": "orgDevices",
             "id": "C39J8W1H3VG5"
           },
           {
             "type": "orgDevices",
             "id": "F2KZ3N4G5HD3"
           }
         ]
       }
     }
   }
 }'

```

**Response**:

```json
{
  "data": {
    "type": "orgDeviceActivities",
    "id": "f7e6d5c4-b3a2-1098-fedc-ba9876543210",
    "attributes": {
      "status": "IN_PROGRESS",
      "subStatus": "SUBMITTED",
      "createdDateTime": "2026-02-27T18:00:00.000Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/orgDeviceActivities/f7e6d5c4-b3a2-1098-fedc-ba9876543210"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/orgDeviceActivities"
  }
}
```

If the request tries to cancel a device management service migration for a serial number that isn’t undergoing one, the activity log result indicates a failure for that serial number.

### Example: Release Devices from an Organization

To release devices from an organization, use `RELEASE_DEVICES` activity type.

> ❗ **Important**: Released devices will no longer be registered to the organization and device enrollment assignments are removed. Devices will be unenrolled from the built-in device management service and removed from Blueprints.

**Request**:

```
curl -X POST https://api-business.apple.com/v1/orgDeviceActivities \
 -H "Authorization: Bearer ${ACCESS_TOKEN} \
 -d '{
   "data": {
     "type": "orgDeviceActivities",
     "attributes": {
       "activityType": "RELEASE_DEVICES"
     },
     "relationships": {
       "devices": {
         "data": [
           {
             "type": "orgDevices",
             "id": "XABC123X0ABC123X0"
           }
         ]
       }
     }
   }
 }'

```

**Response**:

```json
{
  "data": {
    "type": "orgDeviceActivities",
    "id": "b1481656-b267-480d-b284-a809eed8b041",
    "attributes": {
      "status": "IN_PROGRESS",
      "subStatus": "SUBMITTED",
      "createdDateTime": "2025-05-05T04:15:43.282Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/orgDeviceActivities/b1481656-b267-480d-b284-a809eed8b041"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/orgDeviceActivities"
  }
}
```

## Topics

### Responses
- [object OrgDeviceActivityResponse](./orgdeviceactivityresponse.md)
  A response that contains a single organization device activity resource.

## Endpoint

`POST https://api-business.apple.com/v1/orgDeviceActivities`

## Request Body

**Content-Type**: `application/json`  
**Type**: `OrgDeviceActivityCreateRequest`

## Responses

- `201` Created (`OrgDeviceActivityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The request conflicts with the current state of one or more of the given resources — for example, an invalid device management service ID, an invalid device serial number, or a migration deadline outside the allowed range.
- `422` (`ErrorResponse`, `application/json`)
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
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assign or unassign, creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/create-an-orgdeviceactivity)*