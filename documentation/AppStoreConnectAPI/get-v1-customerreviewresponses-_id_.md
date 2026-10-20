# Read customer review response information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific response you wrote to a customer review, including the response content and its state.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviewResponses/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a `customerReviewResponses` resource that represents your review response.

### Query Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for the included related types.

  **Allowed Values**: `responseBody`, `lastModifiedDate`, `state`, `review`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `review`
- `fields[customerReviews]` ([string]): **Allowed Values**: `rating`, `title`, `body`, `reviewerNickname`, `createdDate`, `territory`, `response`, `reviewTerritory`

## Responses

- `200` OK (`CustomerReviewResponseV1Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Review Responses
- [Get a customer review response](./get-v1-customerreviews-_id_-response.md)
  Get the response to a specific customer review.
- [Get the response ID for a customer review](./get-v1-customerreviews-_id_-relationships-response.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviewresponses-_id_)*