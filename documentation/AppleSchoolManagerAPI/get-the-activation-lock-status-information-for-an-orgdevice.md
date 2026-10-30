# Get the Activation Lock Status for a Device

**Framework**: AppleSchoolManagerAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the Activation Lock status of an organization device.

**Availability**:
- Apple School Manager API 1.8+

## Overview

> **Note**: The request can also fail with an unexpected server error if the device reports an internal-only lock state that isn’t valid for a managed device.

### Example

**Request**:

```
curl "https://api-school.apple.com/v1/orgDevices/{id}/activationLockStatus" \
-H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "activationLockStatus",
    "id": "C39J8W1H3VG5",
    "attributes": {
      "isLocked": true,
      "lockType": "MDM"
    }
  },
  "links": {
    "self": "https://api-school.apple.com/v1/orgDevices/C39J8W1H3VG5/activationLockStatus"
  }
}
```

## Topics

### Responses
- [object ActivationLockStatusResponse](./activationlockstatusresponse.md)
  A response that contains the Activation Lock status of an organization device.

## Endpoint

`GET https://api-school.apple.com/v1/orgDevices/{id}/activationLockStatus`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource. For example, the device’s serial number.

### Query Parameters

- `fields[activationLockStatus]` ([string]): The fields to return for included related types.

  **Allowed Values**: `isLocked`, `lockType`

## Responses

- `200` OK (`ActivationLockStatusResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): The org doesn’t manage a device with the requested serial number.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/get-the-activation-lock-status-information-for-an-orgdevice)*