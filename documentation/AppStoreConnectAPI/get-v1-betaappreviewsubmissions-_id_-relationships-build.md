# Get the build ID for a beta app review submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewSubmissions/{id}/relationships/build`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BetaAppReviewSubmissionBuildLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [Read the build information of a beta app review submission](./get-v1-betaappreviewsubmissions-_id_-build.md)
  Get the build information for a specific beta app review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewsubmissions-_id_-relationships-build)*