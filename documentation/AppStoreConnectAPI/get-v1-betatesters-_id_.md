# Read beta tester information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific beta tester.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaTesters/{id}`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaGroups]` ([string]): Fields to return for included related types.
- `fields[betaTesters]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit[builds]` (integer): Number of included related resources to return.
- `limit[betaGroups]` (integer): Number of included related resources to return.
- `limit[apps]` (integer): Number of included related resources to return.

## See Also

- [List beta testers](get-v1-betatesters.md)
  Find and list beta testers for all apps, builds, and beta groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betatesters-_id_)*