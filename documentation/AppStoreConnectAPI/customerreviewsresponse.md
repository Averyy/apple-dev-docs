# CustomerReviewsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Customer Reviews resources.

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
- `included` ([CustomerReviewResponseV1]): The requested relationship data.

## See Also

- [object CustomerReviewResponse](customerreviewresponse.md)
  A response that contains a single Customer Review resource.
- [object CustomerReview](customerreview.md)
  The data structure that represents a Customer Reviews resource.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarization](customerreviewsummarization.md)
  The data structure that represents a customer review summarization resource.
- [object CustomerReviewSummarizationsResponse](customerreviewsummarizationsresponse.md)
  The data structure that represents a customer review summarizations response resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewsresponse)*