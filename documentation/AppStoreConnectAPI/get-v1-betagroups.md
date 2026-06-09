# List beta groups

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta groups for all apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaGroups]` ([string]): Fields to return for included related types.
- `fields[betaRecruitmentCriteria]` ([string])
- `fields[betaTesters]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[id]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[isInternalGroup]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[name]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[publicLinkEnabled]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[publicLinkLimitEnabled]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[publicLink]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `limit[betaTesters]` (integer): Number of included related resources to return.
- `limit[builds]` (integer): Number of included related resources to return.
- `sort` ([string]): Attributes by which to sort.

## See Also

- [Read beta group information](get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the app information of a beta group](get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [Get the app ID for a beta group](get-v1-betagroups-_id_-relationships-app.md)
- [Read Metrics for Beta Testers in a Beta Group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [List beta recruitment criterion IDs for a beta group](get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Read build compatibility for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibility information for a specific beta group.
- [Get the compatible build check ID for a beta group recruitment criterion](get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups)*