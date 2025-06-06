# latest(for:)

**Framework**: StoreKit  
**Kind**: method

Gets the customer’s most recent transaction for an In-App Purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func latest(for productID: String) async -> VerificationResult<Transaction>?
```

#### Return Value

A [`VerificationResult`](verificationresult.md) with a single [`Transaction`](transaction.md), or `nil` if the customer hasn’t purchased the product.

#### Discussion

Call this method for any type of In-App Purchase. The following code example illustrates requesting the most recent transaction to determine whether the customer purchased the product indicated by the string `productIdentifier`:

```swift
guard let verificationResult = await Transaction.latest(for: productIdentifier) else {    
    // The customer hasn't purchased this product.
    return
}

switch verificationResult {
case .verified(let transaction):
    // Check the transaction and give the customer access to purchased 
    // content as appropriate.
    ...
case .unverified(let transaction, let verificationError):
    // Handle unverified transactions based 
    // on your business model.
    ...
}
```

By default, when the [`SKIncludeConsumableInAppPurchaseHistory`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory) property list key is `false`, this method excludes finished consumable in-app purchases unless they are refunded or revoked.

If you set the [`SKIncludeConsumableInAppPurchaseHistory`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory) property list key to `true`, this method returns all transactions, including consumable In-App Purchases that your app marked as finished ([`finish()`](transaction/finish().md)).

## Parameters

- `productID`: The product identifier that the method uses to look up the most recent transaction.

## See Also

- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [static var unfinished: Transaction.Transactions](transaction/unfinished.md)
  A sequence that emits unfinished transactions for the customer.
- [SKIncludeConsumableInAppPurchaseHistory](../BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/latest(for:))*