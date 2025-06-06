# FailableStoreKitAPI

**Framework**: StoreKit Test  
**Kind**: protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol FailableStoreKitAPI<Failure> : Sendable
```

## Topics

### Associated Types
- [associatedtype Failure : SKTestFailure](failablestorekitapi/failure.md)
### Type Properties
- [static var appStoreSync: StoreKitAppStoreSyncAPI](failablestorekitapi/appstoresync.md)
- [static var appTransaction: StoreKitAppTransactionAPI](failablestorekitapi/apptransaction.md)
- [static var loadProducts: StoreKitLoadProductsAPI](failablestorekitapi/loadproducts.md)
- [static var manageSubscriptions: StoreKitManageSubscriptionsAPI](failablestorekitapi/managesubscriptions.md)
- [static var offerCodeRedeem: StoreKitOfferCodeRedeemAPI](failablestorekitapi/offercoderedeem.md)
- [static var purchase: StoreKitPurchaseAPI](failablestorekitapi/purchase.md)
- [static var refundRequest: StoreKitRefundRequestAPI](failablestorekitapi/refundrequest.md)
- [static var subscriptionStatus: StoreKitSubscriptionStatusAPI](failablestorekitapi/subscriptionstatus.md)
- [static var verification: StoreKitVerificationAPI](failablestorekitapi/verification.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [StoreKitAppStoreSyncAPI](storekitappstoresyncapi.md)
- [StoreKitAppTransactionAPI](storekitapptransactionapi.md)
- [StoreKitLoadProductsAPI](storekitloadproductsapi.md)
- [StoreKitManageSubscriptionsAPI](storekitmanagesubscriptionsapi.md)
- [StoreKitOfferCodeRedeemAPI](storekitoffercoderedeemapi.md)
- [StoreKitPurchaseAPI](storekitpurchaseapi.md)
- [StoreKitRefundRequestAPI](storekitrefundrequestapi.md)
- [StoreKitSubscriptionStatusAPI](storekitsubscriptionstatusapi.md)
- [StoreKitVerificationAPI](storekitverificationapi.md)

## See Also

- [protocol SKTestFailure](sktestfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/failablestorekitapi)*