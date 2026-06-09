# Get all app resource ids for a beta tester

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of app resource IDs associated with a beta tester.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaTesters/{id}/relationships/apps`

## Parameters

- `limit` (integer)

## See Also

- [List all apps for a beta tester](get-v1-betatesters-_id_-apps.md)
  Get a list of apps that a beta tester can test.
- [List all builds individually assigned to a beta tester](get-v1-betatesters-_id_-builds.md)
  Get a list of builds individually assigned to a specific beta tester.
- [Get all ids of builds individually assigned to a beta tester](get-v1-betatesters-_id_-relationships-builds.md)
  Get a list of build resource IDs individually assigned to a specific beta tester.
- [List all beta groups to which a beta tester belongs](get-v1-betatesters-_id_-betagroups.md)
  Get a list of beta groups that contain a specific beta tester.
- [Get all beta group ids of a beta tester's groups](get-v1-betatesters-_id_-relationships-betagroups.md)
  Get a list of group resource IDs associated with a beta tester.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betatesters-_id_-relationships-apps)*