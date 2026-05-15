# Read Customer Review Summarizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the customer review summarization for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/customerReviewSummarizations`

## Parameters

- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `filter[territory]` ([string]): A filter of territories to include in the response.
- `fields[customerReviewSummarizations]` ([string])
- `fields[territories]` ([string])
- `filter[platform]` ([string]) *(required)*

## See Also

- [List All Customer Reviews for an App](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [GET /v1/apps/{id}/relationships/customerReviews](get-v1-apps-_id_-relationships-customerreviews.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-customerreviewsummarizations)*