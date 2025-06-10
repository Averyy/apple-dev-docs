# Transaction

**Framework**: StoreKit  
**Kind**: struct

Information that represents the customer’s purchase of a product in your app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Transaction
```

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
- [Testing win-back offers in the sandbox environment](testing-win-back-offers-in-the-sandbox-environment.md)
- [Testing purchases made outside your app](testing-purchases-made-outside-your-app.md)
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md)
- [Testing refund requests](testing-refund-requests.md)
- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md)
- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)

#### Overview

A  represents a successful In-App Purchase. The App Store generates a transaction each time a customer purchases an In-App Purchase product or renews a subscription. For each transaction that represents a current purchase, your app unlocks the purchased content or service and finishes the transaction.

Use the `Transaction` type to perform these transaction-related tasks:

- Get the customer’s transaction history, latest transactions, and current entitlements to unlock content and services.
- Access transaction properties.
- Finish a transaction after your app delivers the purchased content or service.
- Access the raw JSON Web Signature (JWS) string and supporting values to verify the transaction information.
- Listen for new transactions while the app is running.
- Begin a refund request from within your app.

##### Access Transaction History and Current Entitlements

Your app doesn’t create transaction objects. Instead, StoreKit automatically makes up-to-date transactions available to your app, including when someone launches the app for the first time.

> **Note**:  Session 110404: [`Implement proactive in-app purchase restore`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110404/)

You access transactions in several ways:

- Get transaction history anytime by accessing the static [`all`](transaction/all.md) sequence, or get just the most recent transaction for a product with the [`latestTransaction`](product/latesttransaction.md) property of [`Product`](product.md).
- Receive notifications for new transactions while your app is running when customers complete a purchase outside of the app, including on another device, through the transaction listener, [`updates`](transaction/updates.md).
- Access the latest transaction for a subscription group through the subscription status API, using [`transaction`](product/subscriptioninfo/status-swift.struct/transaction.md).
- After a successful In-App Purchase, StoreKit returns the transaction through [`Product.PurchaseResult.success(_:)`](product/purchaseresult/success(_:).md).

The most important use of transaction information is for determining which In-App Purchases the customer has paid access to, so your app can unlock the content or service. The [`currentEntitlements`](transaction/currententitlements.md) API provides the information you need to unlock all of the customer’s paid content in your app. Use `currentEntitlements` to get a list of transactions for all the products the customer is currently entitled to, including non-consumable In-App Purchases and currently active subscriptions.

##### Verify Transactions

The App Store cryptographically signs transaction information in JWS format. StoreKit automatically validates and returns the signed information, wrapped in a [`VerificationResult`](verificationresult.md). When the `VerificationResult` wraps a `Transaction` value, it provides the raw JWS string in the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property. If you get a transaction through [`VerificationResult.verified(_:)`](verificationresult/verified(_:).md), the information passed validation. If you get it through [`VerificationResult.unverified(_:_:)`](verificationresult/unverified(_:_:).md), the information didn’t pass StoreKit’s automatic validation. Your app can immediately access the transaction information in the [`Transaction properties`](transaction-properties.md).

To perform your own validation on the device, use the verification result’s [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) string, and use the provided convenience properties [`headerData`](verificationresult/headerdata-9egfp.md), [`payloadData`](verificationresult/payloaddata-uyle.md), and [`signatureData`](verificationresult/signaturedata-4pyv8.md). For added control and security, send the `jwsRepresentation` to your server to verify. Consider using the App Store Server Library to implement your verification. The library provides the functions `verifyAndDecodeTransaction` and `verifyAndDecodeRenewalInfo` in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

> 💡 **Tip**:  The [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) is the same as the [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) that the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI) returns and to the [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransaction) that you receive in [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2). You can validate them on your server in the same way.

If StoreKit returns a transaction as verified, the transaction is valid for the device. For information about performing your own verification for a device, see [`deviceVerification`](transaction/deviceverification.md).

For more information about JWS, see the [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

##### Access Purchases Made with the Original Api

All In-App Purchases that customers make are equally available to your app in this `Transaction` API, and in receipts using the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md), as follows:

- New purchases that customers make with the original API are available immediately using the `Transaction` API.
- Purchases that customers make with the [`purchase(options:)`](product/purchase(options:).md) method are available in the original API when your app refreshes the receipt. For more information, see [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md).

## Topics

### Transaction properties
- [Transaction properties](transaction-properties.md)
  The properties of a transaction, including identifiers, purchase and revocation dates and details, status, and offer details.
- [var appTransactionID: String](transaction/apptransactionid.md)
  The unique identifier of the app download transaction.
### Monitoring transaction-related changes
- [static var updates: Transaction.Transactions](transaction/updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [Transaction.Transactions](transaction/transactions.md)
  An asynchronous sequence of transactions.
### Getting transaction history
- [static func latest(for: String) async -> VerificationResult<Transaction>?](transaction/latest(for:).md)
  Gets the customer’s most recent transaction for an In-App Purchase.
- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [static var unfinished: Transaction.Transactions](transaction/unfinished.md)
  A sequence that emits unfinished transactions for the customer.
- [SKIncludeConsumableInAppPurchaseHistory](../BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
### Getting current entitlements
- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.
- [static func currentEntitlement(for: String) async -> VerificationResult<Transaction>?](transaction/currententitlement(for:).md)
  Gets the latest transactions that entitle the customer to a specified product.
### Finishing the transaction
- [func finish() async](transaction/finish.md)
  Indicates to the App Store that the app delivered the purchased content or enabled the service to finish the transaction.
- [static var unfinished: Transaction.Transactions](transaction/unfinished.md)
  A sequence that emits unfinished transactions for the customer.
### Verifying transactions
- [let deviceVerification: Data](transaction/deviceverification.md)
  The device verification value you use to verify whether the transaction belongs to the device.
- [let deviceVerificationNonce: UUID](transaction/deviceverificationnonce.md)
  The UUID for computing the device verification value.
- [let signedDate: Date](transaction/signeddate.md)
  The date that the App Store signed the JWS transaction.
### Getting transaction info in JSON format
- [var jsonRepresentation: Data](transaction/jsonrepresentation.md)
  The JSON representation of the transaction information.
### Requesting refunds
- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [func beginRefundRequest(in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-9k0pj.md)
  Presents the refund request sheet for the transaction in a window scene.
- [func beginRefundRequest(in: NSViewController) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-63bvd.md)
  Presents the refund request sheet for the transaction in a view controller.
- [static func beginRefundRequest(for: UInt64, in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(for:in:)-65tph.md)
  Presents the refund request sheet for the specified transaction in a window scene.
- [static func beginRefundRequest(for: UInt64, in: NSViewController) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(for:in:)-9mscy.md)
  Presents the refund request sheet for the specified transaction in a view controller.
- [Transaction.RefundRequestError](transaction/refundrequesterror.md)
  The error codes for refund requests.
- [Transaction.RefundRequestStatus](transaction/refundrequeststatus.md)
  The status codes for refund requests.
### Structures
- [Transaction.AdvancedCommerceInfo](transaction/advancedcommerceinfo-swift.struct.md)
  Metadata for transactions that use the Advanced Commerce API.
- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.
### Instance Properties
- [let advancedCommerceInfo: Transaction.AdvancedCommerceInfo?](transaction/advancedcommerceinfo-swift.property.md)
  Metadata for transactions that use the Advanced Commerce API.
- [var offerPeriodStringRepresentation: String?](transaction/offerperiodstringrepresentation.md)
  The string representation of the offer period applied to the subscription offer for this transaction.
### Type Methods
- [static func all(for: String) -> Transaction.Transactions](transaction/all(for:).md)
  Gets all the transactions associated with this product ID.
- [static func currentEntitlements(for: String) -> Transaction.Transactions](transaction/currententitlements(for:).md)
  Gets the transactions that entitle the user to items purchased under a product ID.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var updates: Transaction.Transactions](transaction/updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction)*