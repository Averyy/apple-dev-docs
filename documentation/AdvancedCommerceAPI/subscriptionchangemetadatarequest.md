# SubscriptionChangeMetadataRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The request body you provide to change the metadata of a subscription.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object SubscriptionChangeMetadataRequest
```

## Properties

- `descriptors` (SubscriptionChangeMetadataDescriptors)
- `items` ([SubscriptionChangeMetadataItem])
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode)

## See Also

- [Change Subscription Metadata](change-subscription-metadata.md)
  Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.
- [object SubscriptionChangeMetadataResponse](subscriptionchangemetadataresponse.md)
  The response body for a successful subscription metadata change.
- [object SubscriptionChangeMetadataDescriptors](subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatarequest)*