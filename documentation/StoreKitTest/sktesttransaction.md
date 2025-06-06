# SKTestTransaction

**Framework**: StoreKit Test  
**Kind**: class

A transaction that occurs in the testing environment.

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
class SKTestTransaction
```

#### Overview

The test transaction represents the test environment’s knowledge of the transaction, including its identifier and the transaction’s state. It represents all the transaction-related configurations you control manually in Xcode for interrupted purchases, Ask to Buy scenarios, and changes to a subscription’s auto-renew state.

The test environment creates an `SKTestTransaction` instance each time your test code calls any method of [`SKTestSession`](sktestsession.md) that affects in-app purchases.

## Topics

### Identifying Transactions and Products
- [var identifier: Int](sktesttransaction/identifier.md)
  The identifier of the transaction in the testing environment.
- [var originalTransactionIdentifier: Int](sktesttransaction/originaltransactionidentifier.md)
  The identifier of the original transaction.
- [var productIdentifier: String](sktesttransaction/productidentifier.md)
  An identifier that uniquely represents a product, which you provide in the StoreKit configuration file.
### Getting Payment Transaction States
- [var state: SKPaymentTransactionState](sktesttransaction/state.md)
  The state of the transaction in the test environment.
### Getting Dates
- [var purchaseDate: Date](sktesttransaction/purchasedate.md)
  The date of purchase for the transaction.
- [var cancelDate: Date?](sktesttransaction/canceldate.md)
  The date when the system refunded the transaction.
- [var expirationDate: Date?](sktesttransaction/expirationdate.md)
  The date a subscription expires.
### Getting Test Environment States
- [var autoRenewingEnabled: Bool](sktesttransaction/autorenewingenabled.md)
  A Boolean value that indicates whether automatic renewal is enabled for the subscription.
- [var hasPurchaseIssue: Bool](sktesttransaction/haspurchaseissue.md)
  A Boolean value that indicates whether you resolve this transaction using the test framework functions.
- [var isPendingPriceIncreaseConsent: Bool](sktesttransaction/ispendingpriceincreaseconsent.md)
  A Boolean value that indicates whether the auto-renewable subscription has a price increase that’s awaiting user consent in the test environment.
- [var pendingAskToBuyConfirmation: Bool](sktesttransaction/pendingasktobuyconfirmation.md)
  A Boolean value that indicates whether the transaction is awaiting an Ask to Buy confirmation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md)
  Prepare your test environment to test in-app purchases with data you configure locally.
- [class SKTestSession](sktestsession.md)
  The controls and environment configuration you use to test StoreKit transactions in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction)*