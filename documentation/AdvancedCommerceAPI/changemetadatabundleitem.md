# ChangeMetadataBundleItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object ChangeMetadataBundleItem
```

## Properties

- `SKU` (SKU): **Maximum Length**: `128`
- `currentSKU` (SKU) *(required)*: **Maximum Length**: `128`
- `description` (description): **Maximum Length**: `45`
- `displayName` (displayName): **Maximum Length**: `30`

## See Also

### Subscription metadata changes from the server
- [Change Subscription Metadata](./change-subscription-metadata.md)
  Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.
- [object SubscriptionChangeMetadataRequest](./subscriptionchangemetadatarequest.md)
  The request body you provide to change the metadata of a subscription.
- [object SubscriptionChangeMetadataResponse](./subscriptionchangemetadataresponse.md)
  The response body for a successful subscription metadata change.
- [object SubscriptionChangeMetadataDescriptors](./subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](./subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.
- [object SubscriptionChangeMetadataRequestV1](./subscriptionchangemetadatarequestv1.md)
- [object SubscriptionChangeMetadataItemV1](./subscriptionchangemetadataitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/changemetadatabundleitem)*