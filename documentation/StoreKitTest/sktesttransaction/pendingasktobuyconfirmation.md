# pendingAskToBuyConfirmation

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.

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
var pendingAskToBuyConfirmation: Bool { get }
```

#### Discussion

To test an Ask to Buy scenario, first set [`askToBuyEnabled`](sktestsession/asktobuyenabled.md) to `true` before making a purchase. If [`pendingAskToBuyConfirmation`](sktesttransaction/pendingasktobuyconfirmation.md) is `true`, approve the transaction by calling [`approveAskToBuyTransaction(identifier:)`](sktestsession/approveasktobuytransaction(identifier:).md) , or decline it by calling [`declineAskToBuyTransaction(identifier:)`](sktestsession/declineasktobuytransaction(identifier:).md).

## See Also

- [var autoRenewingEnabled: Bool](sktesttransaction/autorenewingenabled.md)
  A Boolean value that indicates whether automatic renewal is enabled for the subscription.
- [var hasPurchaseIssue: Bool](sktesttransaction/haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var isPendingPriceIncreaseConsent: Bool](sktesttransaction/ispendingpriceincreaseconsent.md)
  A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/pendingasktobuyconfirmation)*