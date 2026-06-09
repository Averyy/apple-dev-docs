# CustomerReviewResponseV1Response

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a developer’s response to a customer review.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReviewResponseV1Response
```

## Properties

- `data` (CustomerReviewResponseV1) *(required)*: The data structure that represents a `CustomerReviewResponses` resource.
- `included` ([CustomerReview]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object CustomerReviewResponseV1](customerreviewresponsev1.md)
  A developer’s public reply to a customer review on the App Store.
- [object CustomerReviewResponseV1CreateRequest](customerreviewresponsev1createrequest.md)
  The request body to use to create a response to a customer review.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewResponseLinkageResponse](customerreviewresponselinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewresponsev1response)*