# Read Customer Review Response Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific response you wrote to a customer review, including the response content and its state.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviewResponses/{id}`

## Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for the included related types.
- `include` ([string]): Relationship data to include in the response.
- `fields[customerReviews]` ([string])

## See Also

- [Get a Customer Review Response](get-v1-customerreviews-_id_-response.md)
  Get the response to a specific customer review.
- [GET /v1/customerReviews/{id}/relationships/response](get-v1-customerreviews-_id_-relationships-response.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviewresponses-_id_)*