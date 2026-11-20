# SubscriptionChangeMetadataItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The metadata to change for an item, specifically its SKU, description, and display name.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionChangeMetadataItem
```

## Properties

- `SKU` (SKU): The new SKU of the item.

  **Maximum Length**: `128`
- `bundleItems` ([ChangeMetadataBundleItem])
- `currentSKU` (SKU) *(required)*: The original SKU of the item.

  **Maximum Length**: `128`
- `description` (description): The new description for the item.

  **Maximum Length**: `45`
- `displayName` (displayName): The new display name for the item.

  **Maximum Length**: `30`
- `partners` ([Partner])
- `taxCode` (taxCode)

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
- [object ChangeMetadataBundleItem](./changemetadatabundleitem.md)
- [object SubscriptionChangeMetadataRequestV1](./subscriptionchangemetadatarequestv1.md)
- [object SubscriptionChangeMetadataItemV1](./subscriptionchangemetadataitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataitem)*