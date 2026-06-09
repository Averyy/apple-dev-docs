# List beta testers

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta testers for all apps, builds, and beta groups.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaTesters`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaGroups]` ([string]): Fields to return for included related types.
- `fields[betaTesters]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `filter[apps]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[betaGroups]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[email]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[firstName]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[inviteType]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[lastName]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `limit[apps]` (integer): Number of included related resources to return.
- `limit[betaGroups]` (integer): Number of included related resources to return.
- `limit[builds]` (integer): Number of included related resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[id]` ([string])

## See Also

- [Read beta tester information](get-v1-betatesters-_id_.md)
  Get a specific beta tester.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betatesters)*