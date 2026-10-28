# hasPurchaseIssue

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you resolve this transaction using the test framework functions.

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
var hasPurchaseIssue: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasPurchaseIssue;
```

## Discussion

To test interrupted purchases, first set [`interruptedPurchasesEnabled`](../sktestsession/interruptedpurchasesenabled.md) to `true` before making a purchase. If [`hasPurchaseIssue`](./haspurchaseissue.md) value is `true`, then resolve the identified transaction by calling [`resolveIssueForTransaction(identifier:)`](../sktestsession/resolveissuefortransaction%28identifier%29.md).

## See Also

### Getting Test Environment States
- [var autoRenewingEnabled: Bool](./autorenewingenabled.md)
  A Boolean value that indicates whether automatic renewal is enabled for the subscription.
- [var isPendingPriceIncreaseConsent: Bool](./ispendingpriceincreaseconsent.md)
  A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.
- [var pendingAskToBuyConfirmation: Bool](./pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/haspurchaseissue)*