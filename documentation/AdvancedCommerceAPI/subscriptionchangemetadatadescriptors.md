# SubscriptionChangeMetadataDescriptors

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The subscription metadata to change, specifically the description and display name.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object SubscriptionChangeMetadataDescriptors
```

## Properties

- `description` (description): The new description for the subscription.

  **Maximum Length**: `45`
- `displayName` (displayName): The new display name for the subscription.

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
- [object SubscriptionChangeMetadataItem](./subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatadescriptors)*