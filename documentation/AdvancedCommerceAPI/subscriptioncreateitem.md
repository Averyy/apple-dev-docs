# SubscriptionCreateItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The data that describes a subscription item.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionCreateItem
```

## Mentions

- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)

## Properties

- `SKU` (SKU) *(required)*: The item’s product identifier, which you define.

  **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `offer` (Offer)
- `price` (price) *(required)*

## See Also

### Subscription creation in the app
- [object SubscriptionCreateRequest](./subscriptioncreaterequest.md)
  The request data your app provides when a customer purchases an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreateitem)*