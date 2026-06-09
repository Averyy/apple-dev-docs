# List available macos versions for an xcode version

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all macOS versions available in Xcode Cloud that support a specific Xcode version.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists macOS versions available for a specific Xcode version. Use the information provided in the response to update workflows, build dashboards, and more.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/b1e1f7b2-14e7-11ec-82a8-0242ac130003/macOsVersions
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

`GET https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/{id}/macOsVersions`

## Parameters

- `fields[ciMacOsVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.
- `fields[ciXcodeVersions]` ([string]): Additional fields to include for each macOS Versions resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of macOS Versions resources to return.
- `limit[xcodeVersions]` (integer): The number of included macOS Versions resources to return if the Xcode versions relationship is included.

## See Also

- [List all xcode versions available in xcode cloud](get-v1-cixcodeversions.md)
  List all Xcode versions that are available to Xcode Cloud workflows.
- [Read xcode version information](get-v1-cixcodeversions-_id_.md)
  Get information about a specific Xcode version that’s available to Xcode Cloud workflows.
- [List macOS version IDs for a CI Xcode version](get-v1-cixcodeversions-_id_-relationships-macosversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cixcodeversions-_id_-macosversions)*