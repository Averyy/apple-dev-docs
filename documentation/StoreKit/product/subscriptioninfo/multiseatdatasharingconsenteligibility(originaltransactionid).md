# multiSeatDataSharingConsentEligibility(originalTransactionID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

The user’s eligibility to receive the data sharing consent sheet for the specified original transaction’s multi-seat subscription.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
static func multiSeatDataSharingConsentEligibility(originalTransactionID: UInt64) async throws -> Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility
```

## Discussion

> **Throws**: [`StoreKitError.unsupported`](../../storekiterror/unsupported.md) if the user isn’t signed in to the App Store, or another error if StoreKit can’t determine eligibility.

## Parameters

- `originalTransactionID`: The original transaction identifier of the multi-seat subscription to check eligibility for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility(originaltransactionid:))*