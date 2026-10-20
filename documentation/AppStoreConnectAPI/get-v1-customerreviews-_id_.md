# Read customer review information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific customer review, including the review content.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviews/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The resource ID representing a unique customer review.

### Query Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for included related `customerReviewResponses` resources.

  **Allowed Values**: `responseBody`, `lastModifiedDate`, `state`, `review`
- `fields[customerReviews]` ([string]): Fields to return for included related `customerReviews` resources.

  **Allowed Values**: `rating`, `title`, `body`, `reviewerNickname`, `createdDate`, `territory`, `response`, `reviewTerritory`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `response`, `reviewTerritory`
- `fields[territories]` ([string]): **Allowed Values**: `currency`

## Responses

- `200` OK (`CustomerReviewResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviews-_id_)*