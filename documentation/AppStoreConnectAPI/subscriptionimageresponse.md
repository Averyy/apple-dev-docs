# SubscriptionImageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single subscription product image.

**Availability**:
- App Store Connect API 3.6+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`SubscriptionImageV2Response`](./subscriptionimagev2response.md) instead.

## Declaration

```
object SubscriptionImageResponse
```

## Properties

- `data` (SubscriptionImage) *(required)*
- `included` ([Subscription])
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object SubscriptionImage](./subscriptionimage.md)
  An image used to represent a subscription product on the App Store product page.
- [object SubscriptionImageCreateRequest](./subscriptionimagecreaterequest.md)
  The request body you use to create a subscription purchase image reservation.
- [object SubscriptionImagesResponse](./subscriptionimagesresponse.md)
  A response containing a list of images for a subscription product.
- [object SubscriptionImageUpdateRequest](./subscriptionimageupdaterequest.md)
  The request body for updating the upload status or content of a subscription product image.
- [object SubscriptionImagesLinkagesResponse](./subscriptionimageslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimageresponse)*