# Get a customer review response

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the response to a specific customer review.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviews/{id}/response`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a `customerReviews` resource that represents a customer review. For more information, see [Customer Reviews](./customer-reviews.md).

### Query Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for included related types.

  **Allowed Values**: `responseBody`, `lastModifiedDate`, `state`, `review`
- `fields[customerReviews]` ([string]): Fields to return for included related types.

  **Allowed Values**: `rating`, `title`, `body`, `reviewerNickname`, `createdDate`, `territory`, `response`, `reviewTerritory`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `review`

## Responses

- `200` OK (`CustomerReviewResponseV1Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Review Responses
- [Read customer review response information](./get-v1-customerreviewresponses-_id_.md)
  Get information about a specific response you wrote to a customer review, including the response content and its state.
- [Get the response ID for a customer review](./get-v1-customerreviews-_id_-relationships-response.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviews-_id_-response)*