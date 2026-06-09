# CustomerReviewSummarization

**Framework**: App Store Connect API  
**Kind**: dictionary

An AI-generated summary of customer reviews for an app in a specific App Store territory.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object CustomerReviewSummarization
```

## Topics

### Dictionaries
- [object CustomerReviewSummarization.Attributes](customerreviewsummarization/attributes-data.dictionary.md)
  Attributes that describe a customer review summarization resource.
- [object CustomerReviewSummarization.Relationships](customerreviewsummarization/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (CustomerReviewSummarization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (CustomerReviewSummarization.Relationships)
- `type` (string) *(required)*

## See Also

- [object CustomerReviewsResponse](customerreviewsresponse.md)
  The response body for endpoints that list customer reviews for an app.
- [object CustomerReviewResponse](customerreviewresponse.md)
  The response body for endpoints that read a single customer review for an app.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarizationsResponse](customerreviewsummarizationsresponse.md)
  A response containing a list of AI-generated review summaries for an app across territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewsummarization)*