# List all macos versions available in xcode cloud

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all macOS versions available to Xcode Cloud workflows.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists macOS versions available to Xcode Cloud workflows. Use the information provided in the response to read additional data; for example, Xcode version information.

##### Example Request and Response

**Request**:

```
GET https://api.appstoreconnect.apple.com/v1/ciMacOsVersions
```

**Response**:

```json
{
    "data": [
        {
            "type": "ciMacOsVersions",
            "id": "20G95",
            "attributes": {
                "version": "20G95",
                "name": "macOS Big Sur 11.5.2 (20G95)"
            },
            "relationships": {
                "xcodeVersions": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/20G95/relationships/xcodeVersions",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/20G95/xcodeVersions"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/20G95"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciMacOsVersions"
    },
    "meta": {
        "paging": {
            "total": 1,
            "limit": 50
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciMacOsVersions`

## Parameters

### Query Parameters

- `fields[ciMacOsVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.

  **Allowed Values**: `version`, `name`, `xcodeVersions`
- `fields[ciXcodeVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.

  **Allowed Values**: `version`, `name`, `testDestinations`, `macOsVersions`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `xcodeVersions`
- `limit` (integer): The number of macOS Versions resources to return.

  **Maximum**: `200`
- `limit[xcodeVersions]` (integer): The number of included macOS Versions resources to return if the Xcode versions relationship is included.

  **Maximum**: `50`

## Responses

- `200` OK (`CiMacOsVersionsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting macOS Version Information
- [Read macos version information](./get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [List available xcode versions for a macos version](./get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.
- [List Xcode version IDs for a CI macOS version](./get-v1-cimacosversions-_id_-relationships-xcodeversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cimacosversions)*