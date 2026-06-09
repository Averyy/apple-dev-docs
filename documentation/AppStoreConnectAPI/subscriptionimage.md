# SubscriptionImage

**Framework**: App Store Connect API  
**Kind**: dictionary

An image used to represent a subscription product on the App Store product page.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object SubscriptionImage
```

## Topics

### Objects
- [object SubscriptionImage.Attributes](subscriptionimage/attributes-data.dictionary.md)
  Attributes that describe a subscription image resource.
- [object SubscriptionImage.Relationships](subscriptionimage/relationships-data.dictionary.md)
  The relationships for a subscription image, linking it to its associated subscription.

## Properties

- `attributes` (SubscriptionImage.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (SubscriptionImage.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object SubscriptionImageCreateRequest](subscriptionimagecreaterequest.md)
  The request body you use to create a subscription purchase image reservation.
- [object SubscriptionImageResponse](subscriptionimageresponse.md)
  A response containing a single subscription product image.
- [object SubscriptionImagesResponse](subscriptionimagesresponse.md)
  A response containing a list of images for a subscription product.
- [object SubscriptionImageUpdateRequest](subscriptionimageupdaterequest.md)
  The request body for updating the upload status or content of a subscription product image.
- [object SubscriptionImagesLinkagesResponse](subscriptionimageslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimage)*