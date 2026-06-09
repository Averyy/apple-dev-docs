# CustomerReviewResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single customer review for an app.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReviewResponse
```

## Properties

- `data` (CustomerReview) *(required)*: The data structure that represents a `CustomerReviews` resource.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([*]): The requested relationship data.

## See Also

- [object CustomerReviewsResponse](customerreviewsresponse.md)
  The response body for endpoints that list customer reviews for an app.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarization](customerreviewsummarization.md)
  An AI-generated summary of customer reviews for an app in a specific App Store territory.
- [object CustomerReviewSummarizationsResponse](customerreviewsummarizationsresponse.md)
  A response containing a list of AI-generated review summaries for an app across territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewresponse)*