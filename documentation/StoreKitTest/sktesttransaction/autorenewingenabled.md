# autoRenewingEnabled

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL autoRenewingEnabled;
```

## Discussion

By default, the system creates subscriptions with auto-renew enabled. To disable auto-renew, call [`disableAutoRenewForTransaction(identifier:)`](../sktestsession/disableautorenewfortransaction%28identifier%29.md).

## See Also

### Getting Test Environment States
- [var hasPurchaseIssue: Bool](./haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var isPendingPriceIncreaseConsent: Bool](./ispendingpriceincreaseconsent.md)
  A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.
- [var pendingAskToBuyConfirmation: Bool](./pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/autorenewingenabled)*