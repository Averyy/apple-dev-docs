# SubscriptionChangeMetadataItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The metadata to change for an item, specifically its SKU, description, and display name.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object SubscriptionChangeMetadataItem
```

## Properties

- `SKU` (SKU): The new SKU of the item.

  **Maximum Length**: `128`
- `currentSKU` (SKU) *(required)*: The original SKU of the item.

  **Maximum Length**: `128`
- `description` (description): The new description for the item.

  **Maximum Length**: `45`
- `displayName` (displayName): The new display name for the item.

  **Maximum Length**: `30`
- `effective` (effective) *(required)*: The string that determines when the metadata change goes into effect.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataitem)*