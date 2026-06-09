# Read macos version information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific macOS version that’s available to Xcode Cloud workflows.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below accesses information about a macOS version available to Xcode Cloud workflows. Use the data provided in the response to read additional information; for example, Xcode versions.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/20G95
```

**Response**:

```json
{
    "data": {
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
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/20G95"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/{id}`

## Parameters

- `fields[ciMacOsVersions]` ([string]): Additional fields to include for the macOS Versions resource returned by the response.
- `fields[ciXcodeVersions]` ([string]): Additional fields to include for the macOS Versions resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[xcodeVersions]` (integer): The number of included macOS Versions resources to return if the Xcode versions relationship is included.

## See Also

- [List all macos versions available in xcode cloud](get-v1-cimacosversions.md)
  List all macOS versions available to Xcode Cloud workflows.
- [List available xcode versions for a macos version](get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.
- [List Xcode version IDs for a CI macOS version](get-v1-cimacosversions-_id_-relationships-xcodeversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cimacosversions-_id_)*