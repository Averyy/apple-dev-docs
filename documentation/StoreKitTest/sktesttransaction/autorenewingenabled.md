# autoRenewingEnabled

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether automatic renewal is enabled for the subscription.

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
var autoRenewingEnabled: Bool { get }
```

#### Discussion

By default, the system creates subscriptions with auto-renew enabled. To disable auto-renew, call [`disableAutoRenewForTransaction(identifier:)`](sktestsession/disableautorenewfortransaction(identifier:).md).

## See Also

- [var hasPurchaseIssue: Bool](sktesttransaction/haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var isPendingPriceIncreaseConsent: Bool](sktesttransaction/ispendingpriceincreaseconsent.md)
  A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.
- [var pendingAskToBuyConfirmation: Bool](sktesttransaction/pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/autorenewingenabled)*