# CustomerReviewsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list customer reviews for an app.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReviewsResponse
```

## Properties

- `data` ([CustomerReview]) *(required)*: A list of customer review resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([*]): The requested relationship data.

## See Also

- [object CustomerReviewResponse](customerreviewresponse.md)
  The response body for endpoints that read a single customer review for an app.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarization](customerreviewsummarization.md)
  An AI-generated summary of customer reviews for an app in a specific App Store territory.
- [object CustomerReviewSummarizationsResponse](customerreviewsummarizationsresponse.md)
  A response containing a list of AI-generated review summaries for an app across territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewsresponse)*