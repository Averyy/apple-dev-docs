# SubscriptionMigrateResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary

A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object SubscriptionMigrateResponse
```

#### Discussion

This is the response body for the [`Migrate a Subscription to Advanced Commerce API`](migrate-subscription-to-advanced-commerce-api.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format, for the migrated subscription.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format, for the migrated subscription.

## See Also

- [Migrate a Subscription to Advanced Commerce API](migrate-subscription-to-advanced-commerce-api.md)
  Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.
- [object SubscriptionMigrateRequest](subscriptionmigraterequest.md)
  The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- [object SubscriptionMigrateItem](subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object SubscriptionMigrateRenewalItem](subscriptionmigraterenewalitem.md)
  The item information that replaces a migrated subscription item when the subscription renews.
- [object SubscriptionMigrateDescriptors](subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigrateresponse)*