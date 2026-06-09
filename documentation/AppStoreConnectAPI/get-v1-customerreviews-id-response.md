# Get a customer review response

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the response to a specific customer review.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviews/{id}/response`

## Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for included related types.
- `fields[customerReviews]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [Read customer review response information](get-v1-customerreviewresponses-_id_.md)
  Get information about a specific response you wrote to a customer review, including the response content and its state.
- [Get the response ID for a customer review](get-v1-customerreviews-_id_-relationships-response.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviews-_id_-response)*