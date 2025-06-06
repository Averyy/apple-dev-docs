# isPendingPriceIncreaseConsent

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
var isPendingPriceIncreaseConsent: Bool { get }
```

#### Discussion

This value applies only to subscription price increases that require customer consent in the test environment.

## See Also

- [var autoRenewingEnabled: Bool](sktesttransaction/autorenewingenabled.md)
  A Boolean value that indicates whether automatic renewal is enabled for the subscription.
- [var hasPurchaseIssue: Bool](sktesttransaction/haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var pendingAskToBuyConfirmation: Bool](sktesttransaction/pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/ispendingpriceincreaseconsent)*