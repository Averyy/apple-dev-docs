# Get AppleCare coverage Information for a Device

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of AppleCare coverage resources for an organization device.

**Availability**:
- Apple Business API 2.6+

##### Example

**Request**:

```
curl "https://api-business.apple.com/v1/orgDevices/{id}/appleCareCoverage" \
-H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
    "data": [
      {
        "type": "appleCareCoverage",
        "id": "XABC123X0ABC123X0",
        "attributes": {
          "contractCancelDateTime": null,
          "startDateTime": "2025-02-02T00:00:00Z",
          "isRenewable": false,
          "isCanceled": false,
          "description": "Limited Warranty",
          "agreementNumber": null,
          "endDateTime": "2026-02-02T00:00:00Z",
          "status": "ACTIVE",
          "paymentType": "NONE"
        }
      },
      {
        "type": "appleCareCoverage",
        "id": "0000000001",
        "attributes": {
          "contractCancelDateTime": null,
          "startDateTime": "2025-04-17T00:00:00Z",
          "isRenewable": true,
          "isCanceled": false,
          "description": "AppleCare+",
          "agreementNumber": "0000000001",
          "endDateTime": "2026-04-17T00:00:00Z",
          "status": "ACTIVE",
          "paymentType": "SUBSCRIPTION"
        }
      },
      {
        "type": "appleCareCoverage",
        "id": "abe-XABC123X0ABC123X0",
        "attributes": {
          "contractCancelDateTime": null,
          "startDateTime": "2025-04-17T00:00:00Z",
          "isRenewable": true,
          "isCanceled": false,
          "description": "AppleCare+ for Business",
          "agreementNumber": null,
          "endDateTime": null,
          "status": "ACTIVE",
          "paymentType": "ABE_SUBSCRIPTION"
        }
      }
    ],
    "links": {
      "self": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0/appleCareCoverage"
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
- [object AppleCareCoverageResponse](./applecarecoverageresponse.md)
  A response that contains a list of AppleCare coverage resources that belongs to an organization device.

## Endpoint

`GET https://api-business.apple.com/v1/orgDevices/{id}/appleCareCoverage`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource. For example, the device’s serial number.

### Query Parameters

- `fields[appleCareCoverage]` ([string]): The fields to return for included related types.

  **Allowed Values**: `status`, `paymentType`, `description`, `agreementNumber`, `startDateTime`, `endDateTime`, `isRenewable`, `isCanceled`, `contractCancelDateTime`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`

## Responses

- `200` OK (`AppleCareCoverageResponse`, `application/json`)
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
- [Get Devices Enrolled in Apple Device Management Service](./get-apple-mdm-enrolled-devices.md)
  Get a list of devices enrolled in Apple Device Management service.
- [Get Details for a Device Enrolled in Apple Device Management Service](./get-the-details-for-apple-mdm-enrolled-device.md)
  Get detailed information about a device enrolled in Apple Device Management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-all-applecare-coverage-for-an-orgdevice)*