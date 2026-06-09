# CustomerReviewSummarizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of AI-generated review summaries for an app across territories.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object CustomerReviewSummarizationsResponse
```

## Properties

- `data` ([CustomerReviewSummarization]) *(required)*
- `included` ([Territory])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object CustomerReviewsResponse](customerreviewsresponse.md)
  The response body for endpoints that list customer reviews for an app.
- [object CustomerReviewResponse](customerreviewresponse.md)
  The response body for endpoints that read a single customer review for an app.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarization](customerreviewsummarization.md)
  An AI-generated summary of customer reviews for an app in a specific App Store territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewsummarizationsresponse)*