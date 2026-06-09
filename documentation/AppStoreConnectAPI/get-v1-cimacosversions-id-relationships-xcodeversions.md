# List Xcode version IDs for a CI macOS version

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciMacOsVersions/{id}/relationships/xcodeVersions`

## Parameters

- `limit` (integer)

## See Also

- [List all macos versions available in xcode cloud](get-v1-cimacosversions.md)
  List all macOS versions available to Xcode Cloud workflows.
- [Read macos version information](get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [List available xcode versions for a macos version](get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cimacosversions-_id_-relationships-xcodeversions)*