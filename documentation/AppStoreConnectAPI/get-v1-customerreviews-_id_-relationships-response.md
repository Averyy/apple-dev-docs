# Get the response ID for a customer review

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviews/{id}/relationships/response`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`CustomerReviewResponseLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Review Responses
- [Get a customer review response](./get-v1-customerreviews-_id_-response.md)
  Get the response to a specific customer review.
- [Read customer review response information](./get-v1-customerreviewresponses-_id_.md)
  Get information about a specific response you wrote to a customer review, including the response content and its state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviews-_id_-relationships-response)*