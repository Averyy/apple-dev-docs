# Get the app ID for a beta app review detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/{id}/relationships/app`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BetaAppReviewDetailAppLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Beta App Review Details
- [List beta app review details](./get-v1-betaappreviewdetails.md)
  Find and list beta app review details for all apps.
- [Read beta app review detail information](./get-v1-betaappreviewdetails-_id_.md)
  Get beta app review details for a specific app.
- [Read the app information of a beta app review detail](./get-v1-betaappreviewdetails-_id_-app.md)
  Get the app information for a specific beta app review details resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewdetails-_id_-relationships-app)*