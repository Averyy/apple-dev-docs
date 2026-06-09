# Get the build id for an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the ID of the build that is attached to a specific App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/build`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version resource ID from the [`List all app store versions for an app`](get-v1-apps-_id_-appstoreversions.md) response.

## See Also

- [Read the build information of an app store version](get-v1-appstoreversions-_id_-build.md)
  Get the build that is attached to a specific App Store version.
- [Modify the build for an app store version](patch-v1-appstoreversions-_id_-relationships-build.md)
  Change the build that is attached to a specific App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-relationships-build)*