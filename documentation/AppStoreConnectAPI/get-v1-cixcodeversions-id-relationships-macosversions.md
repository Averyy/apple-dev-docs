# List macOS version IDs for a CI Xcode version

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciXcodeVersions/{id}/relationships/macOsVersions`

## Parameters

- `limit` (integer)

## See Also

- [List all xcode versions available in xcode cloud](get-v1-cixcodeversions.md)
  List all Xcode versions that are available to Xcode Cloud workflows.
- [Read xcode version information](get-v1-cixcodeversions-_id_.md)
  Get information about a specific Xcode version that’s available to Xcode Cloud workflows.
- [List available macos versions for an xcode version](get-v1-cixcodeversions-_id_-macosversions.md)
  List all macOS versions available in Xcode Cloud that support a specific Xcode version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cixcodeversions-_id_-relationships-macosversions)*