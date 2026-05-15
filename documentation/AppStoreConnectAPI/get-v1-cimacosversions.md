# List All Macos Versions Available in Xcode Cloud

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all macOS versions available to Xcode Cloud workflows.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists macOS versions available to Xcode Cloud workflows. Use the information provided in the response to read additional data; for example, Xcode version information.

##### Example Request and Response

**Request**:

```None
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

- `fields[ciMacOsVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.
- `fields[ciXcodeVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of macOS Versions resources to return.
- `limit[xcodeVersions]` (integer): The number of included macOS Versions resources to return if the Xcode versions relationship is included.

## See Also

- [Read Macos Version Information](get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [List Available Xcode Versions for a Macos Version](get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.
- [GET /v1/ciMacOsVersions/{id}/relationships/xcodeVersions](get-v1-cimacosversions-_id_-relationships-xcodeversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cimacosversions)*