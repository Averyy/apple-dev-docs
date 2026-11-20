# MigrateBundleItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object MigrateBundleItem
```

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `appAppleId` (int64)
- `appleProductId` (string)
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `price` (price) *(required)*
- `taxCode` (taxCode)

## See Also

### Migration from the server
- [Migrate a Subscription to Advanced Commerce API](./migrate-subscription-to-advanced-commerce-api.md)
  Migrate a subscription that a customer purchased through Apple In-App Purchase to a subscription you manage using the Advanced Commerce API.
- [object SubscriptionMigrateRequest](./subscriptionmigraterequest.md)
  The subscription details you provide to migrate a subscription from Apple In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- [object SubscriptionMigrateResponse](./subscriptionmigrateresponse.md)
  A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- [object SubscriptionMigrateItem](./subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object SubscriptionMigrateRenewalItem](./subscriptionmigraterenewalitem.md)
  The item information that replaces a migrated subscription item when the subscription renews.
- [object SubscriptionMigrateDescriptors](./subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.
- [object SubscriptionMigrateRequestV1](./subscriptionmigraterequestv1.md)
- [object SubscriptionMigrateItemV1](./subscriptionmigrateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/migratebundleitem)*