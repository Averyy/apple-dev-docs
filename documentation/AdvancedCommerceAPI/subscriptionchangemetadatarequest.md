# SubscriptionChangeMetadataRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request body you provide to change the metadata of a subscription.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionChangeMetadataRequest
```

## Properties

- `displayName` (displayName): **Maximum Length**: `30`
- `effective` (effective) *(required)*
- `items` ([SubscriptionChangeMetadataItem])
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)

## See Also

### Subscription metadata changes from the server
- [Change Subscription Metadata](./change-subscription-metadata.md)
  Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.
- [object SubscriptionChangeMetadataResponse](./subscriptionchangemetadataresponse.md)
  The response body for a successful subscription metadata change.
- [object SubscriptionChangeMetadataDescriptors](./subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](./subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.
- [object ChangeMetadataBundleItem](./changemetadatabundleitem.md)
- [object SubscriptionChangeMetadataRequestV1](./subscriptionchangemetadatarequestv1.md)
- [object SubscriptionChangeMetadataItemV1](./subscriptionchangemetadataitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatarequest)*