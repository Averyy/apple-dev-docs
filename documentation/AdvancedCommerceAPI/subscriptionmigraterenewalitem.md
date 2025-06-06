# SubscriptionMigrateRenewalItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The item information that replaces a migrated subscription item when the subscription renews.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object SubscriptionMigrateRenewalItem
```

#### Discussion

If you migrate a subscription that is to renew to another SKU, provide the item that is to renew in the `SubscriptionMigrateRenewalItem`.
For example, if a customer downgrades a subscription, the subscription continues unchanged until the end of the billing period, and downgrades when it renews. If you migrate a subscription in this state before the end of the billing period, you need to provide the item that renews.

## See Also

- [Migrate a Subscription to Advanced Commerce API](migrate-subscription-to-advanced-commerce-api.md)
  Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.
- [object SubscriptionMigrateRequest](subscriptionmigraterequest.md)
  The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- [object SubscriptionMigrateResponse](subscriptionmigrateresponse.md)
  A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- [object SubscriptionMigrateItem](subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object SubscriptionMigrateDescriptors](subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigraterenewalitem)*