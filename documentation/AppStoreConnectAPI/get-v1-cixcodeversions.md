# List All Xcode Versions Available in Xcode Cloud

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all Xcode versions that are available to Xcode Cloud workflows.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists Xcode versions available to Xcode Cloud workflows and supported test destinations, including information about available simulated devices. Use the data provided in the response to display available Xcode versions and test destinations on a dashboard or to read additional information; for example, macOS version information.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciXcodeVersions
```

**Response**:

```json
{
    "data": [
        {
            "type": "ciXcodeVersions",
            "id": "Xcode12E507:stable",
            "attributes": {
                "version": "Xcode12E507:stable",
                "name": "Xcode 12.5.1 (12E507)",
                "testDestinations": [
                    {
                        "deviceTypeName": "iPhone 8",
                        "deviceTypeIdentifier": "com.apple.CoreSimulator.SimDeviceType.iPhone-8",
                        "availableRuntimes": [
                            {
                                "runtimeName": "iOS 13.0",
                                "runtimeIdentifier": "com.apple.CoreSimulator.SimRuntime.iOS-13-0"
                            }
                        ],
                        "kind": "SIMULATOR"
                    },
                    {
                        "deviceTypeName": "Mac",
                        "deviceTypeIdentifier": "mac",
                        "availableRuntimes": [
                            {
                                "runtimeName": "Same as Selected macOS Version",
                                "runtimeIdentifier": "builder"
                            },
                            {
                                "runtimeName": "Latest Beta or Release (Currently macOS Big Sur 11.5.2 (20G95))",
                                "runtimeIdentifier": "latest:all"
                            },
                            {
                                "runtimeName": "macOS Big Sur 11.5.2 (20G95)",
                                "runtimeIdentifier": "20G95"
                            }
                        ],
                        "kind": "MAC"
                    },
                    {
                        "deviceTypeName": "Mac (Mac Catalyst)",
                        "deviceTypeIdentifier": "mac_catalyst",
                        "availableRuntimes": [
                            {
                                "runtimeName": "Same as Selected macOS Version",
                                "runtimeIdentifier": "builder"
                            },
                            {
                                "runtimeName": "Latest Beta or Release (Currently macOS Big Sur 11.5.2 (20G95))",
                                "runtimeIdentifier": "latest:all"
                            },
                            {
                                "runtimeName": "macOS Big Sur 11.5.2 (20G95)",
                                "runtimeIdentifier": "20G95"
                            }
                        ],
                        "kind": "MAC"
                    }
                ]
            },
            "relationships": {
                "macOsVersions": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/Xcode12E507:stable/relationships/macOsVersions",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/Xcode12E507:stable/macOsVersions"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/Xcode20G95:stable"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciXcodeVersions"
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

`GET https://api.appstoreconnect.apple.com/v1/ciXcodeVersions`

## Parameters

- `fields[ciXcodeVersions]` ([string]): Additional fields to include for each Xcode Versions resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Xcode Versions resources to return.
- `limit[macOsVersions]` (integer): The number of included Xcode Versions resources to return if the macOS versions relationship is included.
- `fields[ciMacOsVersions]` ([string]): Additional fields to include for each Xcode Versions resource returned by the response.

## See Also

- [Read Xcode Version Information](get-v1-cixcodeversions-_id_.md)
  Get information about a specific Xcode version that’s available to Xcode Cloud workflows.
- [List Available Macos Versions for an Xcode Version](get-v1-cixcodeversions-_id_-macosversions.md)
  List all macOS versions available in Xcode Cloud that support a specific Xcode version.
- [GET /v1/ciXcodeVersions/{id}/relationships/macOsVersions](get-v1-cixcodeversions-_id_-relationships-macosversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cixcodeversions)*