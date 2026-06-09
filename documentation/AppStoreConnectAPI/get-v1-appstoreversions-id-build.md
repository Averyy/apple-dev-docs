# Read the build information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the build that is attached to a specific App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/build`

## Parameters

- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.

## See Also

- [Get the build id for an app store version](get-v1-appstoreversions-_id_-relationships-build.md)
  Get the ID of the build that is attached to a specific App Store version.
- [Modify the build for an app store version](patch-v1-appstoreversions-_id_-relationships-build.md)
  Change the build that is attached to a specific App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-build)*