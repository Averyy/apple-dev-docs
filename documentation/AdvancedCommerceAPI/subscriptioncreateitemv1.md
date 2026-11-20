# SubscriptionCreateItemV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionCreateItemV1
```

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `offer` (OfferV1)
- `partners` ([Partner])
- `price` (price)

## See Also

### Subscription creation in the app
- [object SubscriptionCreateRequest](./subscriptioncreaterequest.md)
  The request data your app provides when a customer purchases an auto-renewable subscription.
- [object SubscriptionCreateItem](./subscriptioncreateitem.md)
  The data that describes a subscription item.
- [object BundleItem](./bundleitem.md)
- [object SubscriptionCreateRequestV1](./subscriptioncreaterequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreateitemv1)*