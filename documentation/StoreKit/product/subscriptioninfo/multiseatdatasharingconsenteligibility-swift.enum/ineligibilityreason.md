# Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Reasons that you can’t request consent to share group information.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
struct IneligibilityReason
```

## Overview

The App Store might add reasons in the future, so don’t assume that a reason is one of the values in this structure.

## Topics

### Getting reasons
- [static let alreadyConsented: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./ineligibilityreason/alreadyconsented.md)
  A reason that indicates the group purchaser already shares group information with you.
- [static let noOwnedActiveSubscription: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./ineligibilityreason/noownedactivesubscription.md)
  A reason that indicates the person isn’t the group purchaser of an active multiseat subscription in the subscription group.
- [static let notAppleManaged: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./ineligibilityreason/notapplemanaged.md)
  A reason that indicates the subscription doesn’t use Apple-hosted invitations.
### Initializers
- [init(rawValue: String)](./ineligibilityreason/init%28rawvalue%29.md)
  Creates a reason from a raw value.
### Instance Properties
- [let rawValue: String](./ineligibilityreason/rawvalue.md)
  The raw value of the reason.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason)*