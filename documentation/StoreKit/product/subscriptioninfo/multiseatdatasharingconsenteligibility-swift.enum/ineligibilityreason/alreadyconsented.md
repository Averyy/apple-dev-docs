# alreadyConsented

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A reason that indicates the group purchaser already shares group information with you.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
static let alreadyConsented: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason
```

## Mentions

- [Supporting multiseat purchases in your app](../../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

If the group purchaser declines, or later stops sharing group information in Manage Subscriptions, they’re eligible again, so you can ask again.

## See Also

### Getting reasons
- [static let noOwnedActiveSubscription: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./noownedactivesubscription.md)
  A reason that indicates the person isn’t the group purchaser of an active multiseat subscription in the subscription group.
- [static let notAppleManaged: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./notapplemanaged.md)
  A reason that indicates the subscription doesn’t use Apple-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason/alreadyconsented)*