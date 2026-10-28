# SKTestSession

**Framework**: StoreKit Test  
**Kind**: class  
**Role**: Class

The controls and environment configuration you use to test StoreKit transactions in Xcode.

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
class SKTestSession
```

```objc
@interface SKTestSession : NSObject
```

## Overview

This class controls the settings that the server uses when it processes transactions. Run tests that reconfigure the environment serially, not concurrently, to avoid overwriting each other’s environment settings.

> **Note**:  There’s a single instance of the test environment. All `SKTestSession` instances control the same test environment.

The test environment creates an [`SKTestTransaction`](./sktesttransaction.md) instance each time your test code calls any method of `SKTestSession` that affects Apple In-App Purchases, including:

- [`buyProduct(productIdentifier:)`](./sktestsession/buyproduct%28productidentifier%29.md)
- [`refundTransaction(identifier:)`](./sktestsession/refundtransaction%28identifier%29.md)
- [`enableAutoRenewForTransaction(identifier:)`](./sktestsession/enableautorenewfortransaction%28identifier%29.md)
- [`disableAutoRenewForTransaction(identifier:)`](./sktestsession/disableautorenewfortransaction%28identifier%29.md)
- [`forceRenewalOfSubscription(productIdentifier:)`](./sktestsession/forcerenewalofsubscription%28productidentifier%29.md)
- [`expireSubscription(productIdentifier:)`](./sktestsession/expiresubscription%28productidentifier%29.md)
- [`approveAskToBuyTransaction(identifier:)`](./sktestsession/approveasktobuytransaction%28identifier%29.md)
- [`declineAskToBuyTransaction(identifier:)`](./sktestsession/declineasktobuytransaction%28identifier%29.md)
- [`resolveIssueForTransaction(identifier:)`](./sktestsession/resolveissuefortransaction%28identifier%29.md)

You can manage the transactions in the test environment. To get a list of all transactions in the test environment, call [`allTransactions()`](./sktestsession/alltransactions%28%29.md). To delete a single transaction, call [`deleteTransaction(identifier:)`](./sktestsession/deletetransaction%28identifier%29.md). To delete all the transactions, call [`clearTransactions()`](./sktestsession/cleartransactions%28%29.md).

Before automating a test session with `SKTestSession`, you must create a StoreKit configuration file. For more information, see [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md) and [`init(configurationFileNamed:)`](./sktestsession/init%28configurationfilenamed%29.md). Set [`disableDialogs`](./sktestsession/disabledialogs.md) to `true` to run tests without showing test environment UI.

## Topics

### Initializing test sessions
- [convenience init(configurationFileNamed: String) throws](./sktestsession/init%28configurationfilenamed%29.md)
  Initializes the test session with the provided configuration file that you include in your application’s bundle.
- [init(contentsOf: URL) throws](./sktestsession/init%28contentsof%29.md)
  Initializes the test session with a configuration file you provide through a URL.
- [func resetToDefaultState()](./sktestsession/resettodefaultstate%28%29.md)
  Removes all property overrides and resets all test session settings to their default state.
### Configuring the test environment
- [var storefront: String](./sktestsession/storefront.md)
  The three-letter code that represents the region associated with the App Store storefront.
- [var locale: Locale](./sktestsession/locale.md)
  The value that determines the localization metadata the test environment uses.
- [var disableDialogs: Bool](./sktestsession/disabledialogs.md)
  A Boolean value that determines whether the testing environment disables dialogs during automated testing.
### Managing transactions in the test environment
- [func allTransactions() -> [SKTestTransaction]](./sktestsession/alltransactions%28%29.md)
  Gets a list of all transactions in the test environment.
- [func deleteTransaction(identifier: Int) throws](./sktestsession/deletetransaction%28identifier%29.md)
  Deletes a specific transaction from the test environment.
- [func clearTransactions()](./sktestsession/cleartransactions%28%29.md)
  Removes all transactions from the test environment.
### Forcing failed transactions
- [var failTransactionsEnabled: Bool](./sktestsession/failtransactionsenabled.md)
  A Boolean value that determines whether transactions fail in the testing environment.
- [var failureError: SKError.Code](./sktestsession/failureerror.md)
  The error code that transactions return when you enable failing transactions.
### Testing interrupted purchases
- [var interruptedPurchasesEnabled: Bool](./sktestsession/interruptedpurchasesenabled.md)
  A Boolean value that determines whether the test environment simulates an interrupted purchase.
- [func resolveIssueForTransaction(identifier: Int) throws](./sktestsession/resolveissuefortransaction%28identifier%29.md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.
### Testing Ask To Buy transactions
- [var askToBuyEnabled: Bool](./sktestsession/asktobuyenabled.md)
  A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.
- [func approveAskToBuyTransaction(identifier: Int) throws](./sktestsession/approveasktobuytransaction%28identifier%29.md)
  Resolves an Ask to Buy test scenario by approving the transaction.
- [func declineAskToBuyTransaction(identifier: Int) throws](./sktestsession/declineasktobuytransaction%28identifier%29.md)
  Resolves an Ask to Buy test scenario by declining the transaction.
### Testing subscription renewals
- [var timeRate: SKTestSession.TimeRate](./sktestsession/timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](./sktestsession/timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](./sktestsession/enableautorenewfortransaction%28identifier%29.md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](./sktestsession/disableautorenewfortransaction%28identifier%29.md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](./sktestsession/forcerenewalofsubscription%28productidentifier%29.md)
  Ends the previous subscription period and begins the next period in the test environment.
- [func expireSubscription(productIdentifier: String) throws](./sktestsession/expiresubscription%28productidentifier%29.md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.
### Testing billing retry and grace period
- [var billingGracePeriodIsEnabled: Bool](./sktestsession/billinggraceperiodisenabled.md)
  A Boolean value that indicates whether the test environment simulates a billing grace period for auto-renewable subscriptions.
- [var shouldEnterBillingRetryOnRenewal: Bool](./sktestsession/shouldenterbillingretryonrenewal.md)
  A Boolean value that indicates whether the testing environment enters a billing retry state when an auto-renewable subscription renews.
- [func resolveIssueForTransaction(identifier: Int) throws](./sktestsession/resolveissuefortransaction%28identifier%29.md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.
### Testing price increase consent
- [func requestPriceIncreaseConsentForTransaction(identifier: Int) throws](./sktestsession/requestpriceincreaseconsentfortransaction%28identifier%29.md)
  Simulates a price increase that requires customer consent for an auto-renewable subscription.
- [func consentToPriceIncreaseForTransaction(identifier: Int) throws](./sktestsession/consenttopriceincreasefortransaction%28identifier%29.md)
  Simulates a user consenting to a price increase for an auto-renewable subscription.
- [func declinePriceIncreaseForTransaction(identifier: Int) throws](./sktestsession/declinepriceincreasefortransaction%28identifier%29.md)
  Simulates a user canceling an auto-renewable subscription by disabling auto-renew.
### Testing externally performed transactions
- [func buyProduct(productIdentifier: String) throws](./sktestsession/buyproduct%28productidentifier%29.md)
  Simulates buying an Apple In-App Purchase or subscription outside the app.
- [func refundTransaction(identifier: Int) throws](./sktestsession/refundtransaction%28identifier%29.md)
  Simulates a refund for an Apple In-App Purchase that completes outside of the app.
### Instance Methods
- [func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption>) async throws -> Transaction](./sktestsession/buyproduct%28identifier,options%29.md)
- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](./sktestsession/setsimulatederror%28_,forapi%29.md)
- [func simulatedError<API>(forAPI: API) async -> API.Failure?](./sktestsession/simulatederror%28forapi%29.md)
### Initializers
- [init(contentsOfURL: URL) throws](./sktestsession/init%28contentsofurl%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### StoreKit transaction testing
- [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md)
  Prepare your test environment to test in-app purchases with data you configure locally.
- [class SKTestTransaction](./sktesttransaction.md)
  A transaction that occurs in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession)*