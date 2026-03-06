# SubscriptionMigrateRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object SubscriptionMigrateRequest
```

## Properties

- `descriptors` (SubscriptionMigrateDescriptors) *(required)*
- `items` ([SubscriptionMigrateItem]) *(required)*: An array of one or more SKUs, along with descriptions and display names, that are included in the subscription.
- `renewalItems` ([SubscriptionMigrateRenewalItem]): An optional array of subscription items that represents the items that renew at the next renewal period, if they differ from `items`. Supply this array if the customer has a pending subscription downgrade or cross-grade, which applies at the next renewal period.
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `targetProductId` (targetProductId) *(required)*: Your generic product ID for an auto-renewable subscription. You configure this product ID in App Store Connect during setup. For more information, see [`Creating SKUs for your In-App Purchases`](creating-your-purchases.md).
- `taxCode` (taxCode) *(required)*

## See Also

- [Migrate a Subscription to Advanced Commerce API](migrate-subscription-to-advanced-commerce-api.md)
  Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.
- [object SubscriptionMigrateResponse](subscriptionmigrateresponse.md)
  A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- [object SubscriptionMigrateItem](subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object SubscriptionMigrateRenewalItem](subscriptionmigraterenewalitem.md)
  The item information that replaces a migrated subscription item when the subscription renews.
- [object SubscriptionMigrateDescriptors](subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigraterequest)*