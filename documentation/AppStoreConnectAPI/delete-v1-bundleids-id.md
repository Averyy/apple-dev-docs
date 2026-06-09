# Delete a bundle id

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 1.1+

#### Discussion

You can only delete bundle IDs that are used for development. You can’t delete bundle IDs that are being used by an app in App Store Connect.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/bundleIds/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Modify a bundle id](patch-v1-bundleids-_id_.md)
  Update a specific bundle ID’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-bundleids-_id_)*