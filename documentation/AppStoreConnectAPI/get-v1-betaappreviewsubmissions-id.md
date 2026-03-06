# Read Beta App Review Submission Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific beta app review submission.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewSubmissions/{id}`

## Parameters

- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [List Beta App Review Submissions](get-v1-betaappreviewsubmissions.md)
  Find and list beta app review submissions for all builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewsubmissions-_id_)*