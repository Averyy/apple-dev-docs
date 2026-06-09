# Delete a beta tester

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a beta tester’s ability to test all apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaTesters/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create a beta tester](post-v1-betatesters.md)
  Create a beta tester assigned to a group, a build, or an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betatesters-_id_)*