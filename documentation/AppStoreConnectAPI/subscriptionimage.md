# SubscriptionImage

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a subscription image resource.

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
  The data structure that represents the relationships of a subscription image resource.

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
  A response that contains a single subscription images resource.
- [object SubscriptionImagesResponse](subscriptionimagesresponse.md)
  A response that contains a list of subscription image resources.
- [object SubscriptionImageUpdateRequest](subscriptionimageupdaterequest.md)
  The data structure that represents a subscription image update request resource.
- [object SubscriptionImagesLinkagesResponse](subscriptionimageslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimage)*