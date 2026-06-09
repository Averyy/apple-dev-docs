# Modify a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify a beta group’s metadata, including changing its TestFlight public link status.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaGroups/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create a beta group](post-v1-betagroups.md)
  Create a beta group associated with an app, optionally enabling TestFlight public links.
- [Delete a beta group](delete-v1-betagroups-_id_.md)
  Delete a beta group and remove beta tester access to associated builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betagroups-_id_)*