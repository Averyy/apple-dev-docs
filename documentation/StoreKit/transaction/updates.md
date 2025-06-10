# updates

**Framework**: StoreKit  
**Kind**: property

The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var updates: Transaction.Transactions { get }
```

## Mentions

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Testing win-back offers in the sandbox environment](testing-win-back-offers-in-the-sandbox-environment.md)
- [Testing purchases made outside your app](testing-purchases-made-outside-your-app.md)
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

#### Discussion

Use [`updates`](transaction/updates.md) to receive new transactions while the app is running. This sequence receives transactions that occur outside of the app, such as Ask to Buy transactions, subscription offer code redemptions, and purchases that customers make in the App Store. It also emits transactions that customers complete in your app on another device.

Note that after a successful in-app purchase on the same device, StoreKit returns the transaction through [`Product.PurchaseResult.success(_:)`](product/purchaseresult/success(_:).md).

> ❗ **Important**:  Create a [`Task`](https://developer.apple.com/documentation/Swift/Task) to iterate through the transactions from the listener as soon as your app launches. If your app has unfinished transactions, the [`updates`](transaction/updates.md) listener receives them once, immediately after the app launches. Without the [`Task`](https://developer.apple.com/documentation/Swift/Task) to listen for these transactions, your app may miss them.

The following example shows a class that creates a [`Task`](https://developer.apple.com/documentation/Swift/Task) when it initializes. The task retrieves and processes any unfinished transactions.

```swift
final class TransactionObserver {
    
    var updates: Task<Void, Never>? = nil
    
    init() {
        updates = newTransactionListenerTask()
    }

    deinit {
        // Cancel the update handling task when you deinitialize the class.
        updates?.cancel()
    }
    
    private func newTransactionListenerTask() -> Task<Void, Never> {
        Task(priority: .background) {
            for await verificationResult in Transaction.updates {
                self.handle(updatedTransaction: verificationResult)
            }
        }
    }
    
    private func handle(updatedTransaction verificationResult: VerificationResult<Transaction>) {
        guard case .verified(let transaction) = verificationResult else {
            // Ignore unverified transactions.
            return
        }

        if let revocationDate = transaction.revocationDate {
            // Remove access to the product identified by transaction.productID.
            // Transaction.revocationReason provides details about
            // the revoked transaction.
            <#...#>
        } else if let expirationDate = transaction.expirationDate,
            expirationDate < Date() {
            // Do nothing, this subscription is expired.
            return
        } else if transaction.isUpgraded {
            // Do nothing, there is an active transaction
            // for a higher level of service.
            return
        } else {
            // Provide access to the product identified by
            // transaction.productID.
            <#...#>
        }
    }
    
}
```

The [`updates`](transaction/updates.md) listener receives unfinished transactions just once at app launch, but you can use the [`unfinished`](transaction/unfinished.md) listener to get your app’s unfinished transactions at any time. For information on finishing transactions, see [`finish()`](transaction/finish().md).

## See Also

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
  Provide subscription service for customers who redeem offer codes through the App Store or within your app.
- [struct Transaction](transaction.md)
  Information that represents the customer’s purchase of a product in your app.
- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/updates)*