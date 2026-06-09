# Assign individual testers to a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Enable a beta tester who is not a part of a beta group to test a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/individualTesters`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Add access for beta groups to a build](post-v1-builds-_id_-relationships-betagroups.md)
  Add or create a beta group to a build to enable testing.
- [Remove access for beta groups to a build](delete-v1-builds-_id_-relationships-betagroups.md)
  Remove access to a specific build for all beta testers in one or more beta groups.
- [Remove individual testers from a build](delete-v1-builds-_id_-relationships-individualtesters.md)
  Remove access to test a specific build from one or more individually assigned testers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-builds-_id_-relationships-individualtesters)*