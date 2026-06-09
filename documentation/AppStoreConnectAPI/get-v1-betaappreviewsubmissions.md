# List beta app review submissions

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta app review submissions for all builds.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewSubmissions`

## Parameters

- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `filter[betaReviewState]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[build]` ([string]) *(required)*: Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read beta app review submission information](get-v1-betaappreviewsubmissions-_id_.md)
  Get a specific beta app review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewsubmissions)*