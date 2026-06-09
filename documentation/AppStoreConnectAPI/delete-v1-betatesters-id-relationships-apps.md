# Remove a beta tester’s access to apps

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a specific beta tester’s access to test any builds of one or more apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaTesters/{id}/relationships/apps`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Add a beta tester to beta groups](post-v1-betatesters-_id_-relationships-betagroups.md)
  Add one or more beta testers to a specific beta group.
- [Remove a beta tester from beta groups](delete-v1-betatesters-_id_-relationships-betagroups.md)
  Remove a specific beta tester from one or more beta groups, revoking their access to test builds associated with those groups.
- [Individually assign a beta tester to builds](post-v1-betatesters-_id_-relationships-builds.md)
  Individually assign a beta tester to a build.
- [Individually unassign a beta tester from builds](delete-v1-betatesters-_id_-relationships-builds.md)
  Remove an individually assigned beta tester’s ability to test a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betatesters-_id_-relationships-apps)*