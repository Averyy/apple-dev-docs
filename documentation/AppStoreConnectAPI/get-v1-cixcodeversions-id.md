# Read Xcode Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Xcode version that’s available to Xcode Cloud workflows.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below accesses detailed information for a specific Xcode version available to Xcode Cloud workflows. Use the data provided in the response to display available Xcode versions and test destinations on a dashboard or to read additional information; for example, macOS version information.

##### Example Request and Response

## See Also

- [List All Xcode Versions Available in Xcode Cloud](get-v1-cixcodeversions.md)
  List all Xcode versions that are available to Xcode Cloud workflows.
- [List Available macOS Versions for an Xcode Version](get-v1-cixcodeversions-_id_-macosversions.md)
  List all macOS versions available in Xcode Cloud that support a specific Xcode version.
- [GET /v1/ciXcodeVersions/{id}/relationships/macOsVersions](get-v1-cixcodeversions-_id_-relationships-macosversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cixcodeversions-_id_)*