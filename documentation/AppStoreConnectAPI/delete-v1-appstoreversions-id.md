# Delete an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app store version that is associated with an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version resource ID from the [`List all app store versions for an app`](get-v1-apps-_id_-appstoreversions.md) response.

## See Also

- [Create an app store version](post-v1-appstoreversions.md)
  Add a new App Store version or platform to an app.
- [Modify an app store version](patch-v1-appstoreversions-_id_.md)
  Update the App Store version for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversions-_id_)*