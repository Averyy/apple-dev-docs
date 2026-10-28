# resolveIssueForTransaction(identifier:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) resolveIssueForTransactionWithIdentifier:(NSUInteger) identifier error:(NSError **) error;
```

## Discussion

Call this method to simulate a user resolving an issue that prevents a purchase, such as an interrupted purchase or a billing issue. You enable the testing environment to simulate the issues by setting the [`interruptedPurchasesEnabled`](./interruptedpurchasesenabled.md) and [`billingGracePeriodIsEnabled`](./billinggraceperiodisenabled.md) properties, respectively.

In the production environment, users resolve the issues by completing actions outside of your app. For example, users may need to agree to new terms and conditions or update a payment card.

When you call [`resolveIssueForTransaction(identifier:)`](./resolveissuefortransaction%28identifier%29.md), your app receives the new transaction in the [`updates`](../../StoreKit/transaction/updates.md) sequence or the [`transactionObservers`](../../StoreKit/skpaymentqueue/transactionobservers.md).

## Parameters

- `identifier`: The transaction [`identifier`](../sktesttransaction/identifier.md) for the transaction that the test environment resolves.

## See Also

### Testing interrupted purchases
- [var interruptedPurchasesEnabled: Bool](./interruptedpurchasesenabled.md)
  A Boolean value that determines whether the test environment simulates an interrupted purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/resolveissuefortransaction(identifier:))*