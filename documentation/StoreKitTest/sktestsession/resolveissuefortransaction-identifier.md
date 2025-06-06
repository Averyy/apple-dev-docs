# resolveIssueForTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method

Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func resolveIssueForTransaction(identifier: Int) throws
```

#### Discussion

Call this method to simulate a user resolving an issue that prevents a purchase, such as an interrupted purchase or a billing issue. You enable the testing environment to simulate the issues by setting the [`interruptedPurchasesEnabled`](sktestsession/interruptedpurchasesenabled.md) and [`billingGracePeriodIsEnabled`](sktestsession/billinggraceperiodisenabled.md) properties, respectively.

In the production environment, users resolve the issues by completing actions outside of your app. For example, users may need to agree to new terms and conditions or update a payment card.

When you call [`resolveIssueForTransaction(identifier:)`](sktestsession/resolveissuefortransaction(identifier:).md), your app receives the new transaction in the [`updates`](https://developer.apple.com/documentation/StoreKit/Transaction/updates) sequence or the [`transactionObservers`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/transactionObservers).

## Parameters

- `identifier`: The transaction   for the transaction that the test environment resolves.

## See Also

- [var interruptedPurchasesEnabled: Bool](sktestsession/interruptedpurchasesenabled.md)
  A Boolean value that determines whether the test environment simulates an interrupted purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/resolveissuefortransaction(identifier:))*