# Remove access for beta groups to a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove access to a specific build for all beta testers in one or more beta groups.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/betaGroups`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Add access for beta groups to a build](post-v1-builds-_id_-relationships-betagroups.md)
  Add or create a beta group to a build to enable testing.
- [Assign individual testers to a build](post-v1-builds-_id_-relationships-individualtesters.md)
  Enable a beta tester who is not a part of a beta group to test a build.
- [Remove individual testers from a build](delete-v1-builds-_id_-relationships-individualtesters.md)
  Remove access to test a specific build from one or more individually assigned testers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-builds-_id_-relationships-betagroups)*