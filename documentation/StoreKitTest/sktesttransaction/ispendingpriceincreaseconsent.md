# isPendingPriceIncreaseConsent

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL pendingPriceIncreaseConsent;
```

#### Discussion

This value applies only to subscription price increases that require customer consent in the test environment.

## See Also

### Getting Test Environment States
- [var autoRenewingEnabled: Bool](./autorenewingenabled.md)
  A Boolean value that indicates whether automatic renewal is enabled for the subscription.
- [var hasPurchaseIssue: Bool](./haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var pendingAskToBuyConfirmation: Bool](./pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/ispendingpriceincreaseconsent)*