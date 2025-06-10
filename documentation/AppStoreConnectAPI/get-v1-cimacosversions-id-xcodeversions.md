# List Available Xcode Versions for a macOS Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all Xcode versions available for a specific macOS version in Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists Xcode versions available in Xcode Cloud for a specific macOS version. Use the data provided in the response to display available Xcode versions and test destinations on a dashboard.

##### Example Request and Response

## See Also

- [List All macOS Versions Available in Xcode Cloud](get-v1-cimacosversions.md)
  List all macOS versions available to Xcode Cloud workflows.
- [Read macOS Version Information](get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [GET /v1/ciMacOsVersions/{id}/relationships/xcodeVersions](get-v1-cimacosversions-_id_-relationships-xcodeversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cimacosversions-_id_-xcodeversions)*