# Get Organization Devices

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of devices in an organization that enroll using Automated Device Enrollment.

**Availability**:
- Apple Business API 2.7+

### Filter devices

Use `filter` query parameters to return only the devices that match the values you specify. You can filter on the following attributes only. Other attributes, including those you can request with `fields[orgDevices]`, aren’t supported as filters.

| **Attribute** | **Operators** | **Values** |
| --- | --- | --- |
| `serialNumber` | Equals | The serial number of the device. |
| `orderNumber` | Equals | The order number of the device. |
| `productFamily` | Equals | `Mac`, `iPhone`, `iPad`, `iPod`, `AppleTV`, `Watch`, or `Vision`. |
| `purchaseSourceType` | Equals | `APPLE`, `RESELLER`, or `MANUALLY_ADDED`. |
| `status` | Equals | `ASSIGNED` or `UNASSIGNED`. |
| `addedToOrgDateTime` | Equals, `[GT]`, `[GTE]`, `[LT]`, `[LTE]` | A UTC date and time, such as `2025-01-01T00:00:00Z`. |
| `orderDateTime` | Equals, `[GT]`, `[GTE]`, `[LT]`, `[LTE]` | A UTC date and time, such as `2025-01-01T00:00:00Z`. |

When you combine filters on different attributes, the response includes only devices that match all of them. Within one filter, separate multiple values with commas to match devices that have any of those values. Range operators (`[GT]`, `[GTE]`, `[LT]`, and `[LTE]`) accept a single value. Filter values must match exactly, and wildcard characters aren’t supported. If a filter attribute, operator, or value isn’t supported, the request fails with a `400` error.

#### Page through filtered results

Set all the filters you need on the first request, without a `cursor`. For each following page, use the `links.next` URL as is. If you build the request yourself, pass the `cursor` from `meta.paging.nextCursor`, and keep the `filter`, `fields[orgDevices]`, and `limit` parameters identical on every page.

> ❗ **Important**: Don’t add, remove, or change filters while you page through results. To change filters, start over with a new request without a `cursor`.

### Example: Get Organization Devices

**Request**:

```
curl "https://api-business.apple.com/v1/orgDevices" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
    "data": [
      {
        "type": "orgDevices",
        "id": "XABC123X0ABC123X0",
        "attributes": {
          "serialNumber": "XABC123X0ABC123X0",
          "addedToOrgDateTime": "2025-04-30T22:05:14.192Z",
          "releasedFromOrgDateTime": null,
          "updatedDateTime": "2025-05-01T15:33:54.164Z",
          "deviceModel": "iMac 21.5\"",
          "productFamily": "Mac",
          "productType": "iMac16,2",
          "deviceCapacity": "750GB",
          "partNumber": "FD311LL/A",
          "orderNumber": "1234567890",
          "color": "SILVER",
          "status": "UNASSIGNED",
          "orderDateTime": "2011-08-15T07:00:00Z",
          "imei": [
            "123456789012345",
            "123456789012346"
          ],
          "meid": [
            "12345678901237"
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
      }
    ],
    "links": {
      "self": "https://api-business.apple.com/v1/orgDevices",
      "next": "https://api-business.apple.com/v1/orgDevices?cursor=MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA"
    },
    "meta": {
      "paging": {
        "nextCursor": "MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA",
        "limit": 100
      }
    }
  }
```

### Example: Filter Organization Devices

**Request**:

```
curl "https://api-business.apple.com/v1/orgDevices?filter[status]=UNASSIGNED&filter[productFamily]=Mac,iPad&filter[addedToOrgDateTime][GTE]=2025-01-01T00:00:00Z&limit=100" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
    "data": [
      {
        "type": "orgDevices",
        "id": "XABC123X0ABC123X0",
        "attributes": {
          "serialNumber": "XABC123X0ABC123X0",
          "addedToOrgDateTime": "2025-04-30T22:05:14.192Z",
          "releasedFromOrgDateTime": null,
          "updatedDateTime": "2025-05-01T15:33:54.164Z",
          "deviceModel": "iMac 21.5\"",
          "productFamily": "Mac",
          "productType": "iMac16,2",
          "deviceCapacity": "750GB",
          "partNumber": "FD311LL/A",
          "orderNumber": "1234567890",
          "color": "SILVER",
          "status": "UNASSIGNED",
          "orderDateTime": "2011-08-15T07:00:00Z",
          "imei": [
            "123456789012345",
            "123456789012346"
          ],
          "meid": [
            "12345678901237"
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
      }
    ],
    "links": {
      "self": "https://api-business.apple.com/v1/orgDevices?filter[status]=UNASSIGNED&filter[productFamily]=Mac,iPad&filter[addedToOrgDateTime][GTE]=2025-01-01T00:00:00Z&limit=100",
      "next": "https://api-business.apple.com/v1/orgDevices?filter[status]=UNASSIGNED&filter[productFamily]=Mac,iPad&filter[addedToOrgDateTime][GTE]=2025-01-01T00:00:00Z&limit=100&cursor=MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA"
    },
    "meta": {
      "paging": {
        "nextCursor": "MDowOjE3NDYxMTM4OTI1OTA6MTc0NjExMzg5MjU5MDp0cnVlOmZhbHNlOjE3NDYxMTM4OTI1OTA",
        "limit": 100
      }
    }
  }
```

## Topics

### Responses
- [object OrgDevicesResponse](./orgdevicesresponse.md)
  A response that contains a list of organization device resources.

## Endpoint

`GET https://api-business.apple.com/v1/orgDevices`

## Parameters

### Query Parameters

- `fields[orgDevices]` ([string]): The fields to include for each device in the response. This parameter doesn’t filter devices. To filter devices, use the `filter` parameters.

  **Allowed Values**: `serialNumber`, `addedToOrgDateTime`, `releasedFromOrgDateTime`, `updatedDateTime`, `deviceModel`, `productFamily`, `productType`, `deviceCapacity`, `partNumber`, `orderNumber`, `color`, `status`, `orderDateTime`, `imei`, `meid`, `eid`, `purchaseSourceId`, `purchaseSourceType`, `wifiMacAddress`, `bluetoothMacAddress`, `ethernetMacAddress`, `assignedServer`, `appleCareCoverage`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`
- `cursor` (string): A pagination cursor to retrieve the next page of results.
- `filter[serialNumber]` ([string]): Filter by the serial number of the device. Separate multiple values with commas.
- `filter[productFamily]` ([string]): Filter by the product family of the device. Possible values: `Mac`, `iPhone`, `iPad`, `iPod`, `AppleTV`, `Watch`, and `Vision`. Separate multiple values with commas.
- `filter[purchaseSourceType]` ([string]): Filter by the purchase source type of the device. Possible values: `APPLE`, `RESELLER`, and `MANUALLY_ADDED`. Separate multiple values with commas.
- `filter[orderNumber]` ([string]): Filter by the order number of the device. Separate multiple values with commas.
- `filter[status]` ([string]): Filter by the assignment status of the device. Possible values: `ASSIGNED` and `UNASSIGNED`. Separate multiple values with commas.
- `filter[addedToOrgDateTime]` ([string]): Filter by the date and time the device was added to the organization, such as `2025-01-01T00:00:00Z`.
- `filter[addedToOrgDateTime][GT]` (string): Filter for devices added to the organization after this date and time.
- `filter[addedToOrgDateTime][GTE]` (string): Filter for devices added to the organization at or after this date and time.
- `filter[addedToOrgDateTime][LT]` (string): Filter for devices added to the organization before this date and time.
- `filter[addedToOrgDateTime][LTE]` (string): Filter for devices added to the organization at or before this date and time.
- `filter[orderDateTime]` ([string]): Filter by the date and time the device was ordered, such as `2025-01-01T00:00:00Z`.
- `filter[orderDateTime][GT]` (string): Filter for devices ordered after this date and time.
- `filter[orderDateTime][GTE]` (string): Filter for devices ordered at or after this date and time.
- `filter[orderDateTime][LT]` (string): Filter for devices ordered before this date and time.
- `filter[orderDateTime][LTE]` (string): Filter for devices ordered at or before this date and time.

## Responses

- `200` OK (`OrgDevicesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Devices
- [Get Device Information](./get-orgdevice-information.md)
  Get information about a device in an organization.
- [Get AppleCare coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
- [Get Devices Enrolled in Apple Device Management Service](./get-apple-mdm-enrolled-devices.md)
  Get a list of devices enrolled in Apple Device Management service.
- [Get Details for a Device Enrolled in Apple Device Management Service](./get-the-details-for-apple-mdm-enrolled-device.md)
  Get detailed information about a device enrolled in Apple Device Management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-org-devices)*