# Get Device Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a device in an organization.

**Availability**:
- Apple Business API 2.6+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/orgDevices/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
      "data": {
        "type": "orgDevices",
        "id": "XABC123X0ABC123X0",
        "attributes": {
          "addedToOrgDateTime": "2025-04-30T22:05:14.192Z",
          "updatedDateTime": "2025-05-01T15:33:54.164Z",
          "releasedFromOrgDateTime": "2025-06-01T15:33:54.164Z",
          "deviceModel": "iMac 21.5\"",
          "productFamily": "Mac",
          "productType": "iMac16,2",
          "deviceCapacity": "750GB",
          "partNumber": "FD311LL/A",
          "orderNumber": "1234567890",
          "color": "",
          "status": "UNASSIGNED",
          "orderDateTime": "2011-08-15T07:00:00Z",
          "imei": [
            "123456789012345",
            "123456789012346"
          ],
          "meid": [
            "123456789012347"
          ],
          "eid": "89049037640158663184237812557346",
          "purchaseSourceUid": "-2085650007946880",
          "purchaseSourceType": "APPLE"
        },
        "relationships": {
          "assignedServer": {
            "links": {
              "self": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0/relationships/assignedServer",
              "related": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0/assignedServer"
            }
          },
          "appleCareCoverage": {
            "links": {
              "related": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0/appleCareCoverage"
            }
          },
          "activationLockStatus": {
            "links": {
              "related": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0/activationLockStatus"
            }
          }
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0"
        }
      },
      "links": {
        "self": "https://api-business.apple.com/v1/orgDevices/XABC123X0ABC123X0"
      }
    }
```

## Topics

### Responses
- [object OrgDeviceResponse](./orgdeviceresponse.md)
  A response that contains a single organization device resource.

## Endpoint

`GET https://api-business.apple.com/v1/orgDevices/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[orgDevices]` ([string]): The fields to return for included related types.

  **Allowed Values**: `serialNumber`, `addedToOrgDateTime`, `releasedFromOrgDateTime`, `updatedDateTime`, `deviceModel`, `productFamily`, `productType`, `deviceCapacity`, `partNumber`, `orderNumber`, `color`, `status`, `orderDateTime`, `imei`, `meid`, `eid`, `purchaseSourceId`, `purchaseSourceType`, `wifiMacAddress`, `bluetoothMacAddress`, `ethernetMacAddress`, `assignedServer`, `appleCareCoverage`

## Responses

- `200` OK (`OrgDeviceResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Devices
- [Get Organization Devices](./get-org-devices.md)
  Get a list of devices in an organization that enroll using Automated Device Enrollment.
- [Get AppleCare coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
- [Get Devices Enrolled in Apple Device Management Service](./get-apple-mdm-enrolled-devices.md)
  Get a list of devices enrolled in Apple Device Management service.
- [Get Details for a Device Enrolled in Apple Device Management Service](./get-the-details-for-apple-mdm-enrolled-device.md)
  Get detailed information about a device enrolled in Apple Device Management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-orgdevice-information)*