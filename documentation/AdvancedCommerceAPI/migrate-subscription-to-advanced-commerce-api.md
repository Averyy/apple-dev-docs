# Migrate a Subscription to Advanced Commerce API

**Framework**: Advancedcommerceapi  
**Kind**: httpRequest

Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Advanced Commerce API changelog](changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

> **Note**: You can use the Advanced Commerce API and the StoreKit [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) APIs in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime.

## Request Body

The request body that contains the details for the migration.

## See Also

- [object SubscriptionMigrateRequest](subscriptionmigraterequest.md)
  The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- [object SubscriptionMigrateResponse](subscriptionmigrateresponse.md)
  A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- [object SubscriptionMigrateItem](subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object SubscriptionMigrateRenewalItem](subscriptionmigraterenewalitem.md)
  The item information that replaces a migrated subscription item when the subscription renews.
- [object SubscriptionMigrateDescriptors](subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdvancedCommerceAPI/migrate-subscription-to-advanced-commerce-api)*