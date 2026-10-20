# Read the beta app review submission of a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the beta app review submission status for a specific build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/betaAppReviewSubmission`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `betaReviewState`, `submittedDate`, `build`

## Responses

- `200` OK (`BetaAppReviewSubmissionWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Checking Beta Review Submission Status
- [Get the beta app review submission ID for a build](./get-v1-builds-_id_-relationships-betaappreviewsubmission.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-betaappreviewsubmission)*