# Delete an Android to iOS Mapping Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a specific Android to iOS mapping detail.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/androidToIosAppMappingDetails/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the android to iOS app mapping detail resource ID from the [`Create an Android to iOS App Mapping Detail`](post-v1-androidtoiosappmappingdetails.md) response.

## See Also

- [Read Android to iOS App Mapping Details](get-v1-androidtoiosappmappingdetails-_id_.md)
  Get information about a specific android to iOS app mapping detail.
- [Modify an Android to iOS App Mapping Detail](patch-v1-androidtoiosappmappingdetails-_id_.md)
  Update an Android to iOS app mapping detail.
- [Create an Android to iOS App Mapping Detail](post-v1-androidtoiosappmappingdetails.md)
  Create a detail that maps an Android app to an iOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-androidtoiosappmappingdetails-_id_)*