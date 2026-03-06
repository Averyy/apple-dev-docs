# Read Customer Review Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific customer review, including the review content.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/customerReviews/{id}`

## Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for included related `customerReviewResponses` resources.
- `fields[customerReviews]` ([string]): Fields to return for included related `customerReviews` resources.
- `include` ([string]): Relationship data to include in the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-customerreviews-_id_)*