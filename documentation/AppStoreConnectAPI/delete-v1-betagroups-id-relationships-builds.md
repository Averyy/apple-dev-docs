# Remove builds from a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove access to test one or more builds from beta testers in a specific beta group.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/relationships/builds`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Add beta testers to a beta group](post-v1-betagroups-_id_-relationships-betatesters.md)
  Add a specific beta tester to one or more beta groups for beta testing.
- [Remove beta testers from a beta group](delete-v1-betagroups-_id_-relationships-betatesters.md)
  Remove a specific beta tester from a one or more beta groups, revoking their access to test builds associated with those groups.
- [Add builds to a beta group](post-v1-betagroups-_id_-relationships-builds.md)
  Associate builds with a beta group to enable the group to test the builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betagroups-_id_-relationships-builds)*