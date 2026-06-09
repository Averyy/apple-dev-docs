# CustomerReviewResponseV1

**Framework**: App Store Connect API  
**Kind**: dictionary

A developer’s public reply to a customer review on the App Store.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReviewResponseV1
```

## Topics

### Objects
- [object CustomerReviewResponseV1.Attributes](customerreviewresponsev1/attributes-data.dictionary.md)
  The attributes of the response to a customer’s review including its content.
- [object CustomerReviewResponseV1.Relationships](customerreviewresponsev1/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (CustomerReviewResponseV1.Attributes): The attributes of the response to the customer’s review, including its content.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the `CustomerReviewResponses` resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (CustomerReviewResponseV1.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CustomerReviewResponseV1Response](customerreviewresponsev1response.md)
  The response body for endpoints that create, read, or modify a developer’s response to a customer review.
- [object CustomerReviewResponseV1CreateRequest](customerreviewresponsev1createrequest.md)
  The request body to use to create a response to a customer review.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewResponseLinkageResponse](customerreviewresponselinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreviewresponsev1)*