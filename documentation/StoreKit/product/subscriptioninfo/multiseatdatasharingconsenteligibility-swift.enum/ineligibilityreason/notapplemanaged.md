# notAppleManaged

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A reason that indicates the subscription doesn’t use Apple-hosted invitations.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
static let notAppleManaged: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason
```

## Mentions

- [Supporting multiseat purchases in your app](../../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

With developer-hosted invitations, your own records describe the group, so there’s no group information to share. For more information, see [`Transaction.MultiSeatInfo.InvitationManagement`](../../../../transaction/multiseatinfo-swift.struct/invitationmanagement-swift.struct.md).

## See Also

### Getting reasons
- [static let alreadyConsented: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./alreadyconsented.md)
  A reason that indicates the group purchaser already shares group information with you.
- [static let noOwnedActiveSubscription: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./noownedactivesubscription.md)
  A reason that indicates the person isn’t the group purchaser of an active multiseat subscription in the subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason/notapplemanaged)*