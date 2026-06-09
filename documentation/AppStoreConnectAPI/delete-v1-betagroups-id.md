# Delete a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a beta group and remove beta tester access to associated builds.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaGroups/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create a beta group](post-v1-betagroups.md)
  Create a beta group associated with an app, optionally enabling TestFlight public links.
- [Modify a beta group](patch-v1-betagroups-_id_.md)
  Modify a beta group’s metadata, including changing its TestFlight public link status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betagroups-_id_)*