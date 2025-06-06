# SKTestSession

**Framework**: StoreKit Test  
**Kind**: class

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

#### Overview

This class controls the settings that the server uses when it processes transactions. Run tests that reconfigure the environment serially, not concurrently, to avoid overwriting each other’s environment settings.

> **Note**:  There’s a single instance of the test environment. All `SKTestSession` instances control the same test environment.

 There’s a single instance of the test environment. All `SKTestSession` instances control the same test environment.

The test environment creates an [`SKTestTransaction`](sktesttransaction.md) instance each time your test code calls any method of `SKTestSession` that affects in-app purchases, including:

- [`buyProduct(productIdentifier:)`](sktestsession/buyproduct(productidentifier:).md)
- [`refundTransaction(identifier:)`](sktestsession/refundtransaction(identifier:).md)
- [`enableAutoRenewForTransaction(identifier:)`](sktestsession/enableautorenewfortransaction(identifier:).md)
- [`disableAutoRenewForTransaction(identifier:)`](sktestsession/disableautorenewfortransaction(identifier:).md)
- [`forceRenewalOfSubscription(productIdentifier:)`](sktestsession/forcerenewalofsubscription(productidentifier:).md)
- [`expireSubscription(productIdentifier:)`](sktestsession/expiresubscription(productidentifier:).md)
- [`approveAskToBuyTransaction(identifier:)`](sktestsession/approveasktobuytransaction(identifier:).md)
- [`declineAskToBuyTransaction(identifier:)`](sktestsession/declineasktobuytransaction(identifier:).md)
- [`resolveIssueForTransaction(identifier:)`](sktestsession/resolveissuefortransaction(identifier:).md)

You can manage the transactions in the test environment. To get a list of all transactions in the test environment, call [`allTransactions()`](sktestsession/alltransactions().md). To delete a single transaction, call [`deleteTransaction(identifier:)`](sktestsession/deletetransaction(identifier:).md). To delete all the transactions, call [`clearTransactions()`](sktestsession/cleartransactions().md).

Before automating a test session with `SKTestSession`, you must create a StoreKit configuration file. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) and [`init(configurationFileNamed:)`](sktestsession/init(configurationfilenamed:).md). Set [`disableDialogs`](sktestsession/disabledialogs.md) to `true` to run tests without showing test environment UI.

## Topics

### Initializing test sessions
- [convenience init(configurationFileNamed: String) throws](sktestsession/init(configurationfilenamed:).md)
  Initializes the test session with the provided configuration file that you include in your application’s bundle.
- [init(contentsOf: URL) throws](sktestsession/init(contentsof:).md)
  Initializes the test session with a configuration file you provide through a URL.
- [func resetToDefaultState()](sktestsession/resettodefaultstate.md)
  Removes all property overrides and resets all test session settings to their default state.
### Configuring the test environment
- [var storefront: String](sktestsession/storefront.md)
  The three-letter code that represents the region associated with the App Store storefront.
- [var locale: Locale](sktestsession/locale.md)
  The value that determines the localization metadata the test environment uses.
- [var disableDialogs: Bool](sktestsession/disabledialogs.md)
  A Boolean value that determines whether the testing environment disables dialogs during automated testing.
### Managing transactions in the test environment
- [func allTransactions() -> [SKTestTransaction]](sktestsession/alltransactions.md)
  Gets a list of all transactions in the test environment.
- [func deleteTransaction(identifier: Int) throws](sktestsession/deletetransaction(identifier:).md)
  Deletes a specific transaction from the test environment.
- [func clearTransactions()](sktestsession/cleartransactions.md)
  Removes all transactions from the test environment.
### Forcing failed transactions
- [var failTransactionsEnabled: Bool](sktestsession/failtransactionsenabled.md)
  A Boolean value that determines whether transactions fail in the testing environment.
- [var failureError: SKError.Code](sktestsession/failureerror.md)
  The error code that transactions return when you enable failing transactions.
### Testing interrupted purchases
- [var interruptedPurchasesEnabled: Bool](sktestsession/interruptedpurchasesenabled.md)
  A Boolean value that determines whether the test environment simulates an interrupted purchase.
- [func resolveIssueForTransaction(identifier: Int) throws](sktestsession/resolveissuefortransaction(identifier:).md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.
### Testing Ask To Buy transactions
- [var askToBuyEnabled: Bool](sktestsession/asktobuyenabled.md)
  A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.
- [func approveAskToBuyTransaction(identifier: Int) throws](sktestsession/approveasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by approving the transaction.
- [func declineAskToBuyTransaction(identifier: Int) throws](sktestsession/declineasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by declining the transaction.
### Testing subscription renewals
- [var timeRate: SKTestSession.TimeRate](sktestsession/timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [SKTestSession.TimeRate](sktestsession/timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](sktestsession/enableautorenewfortransaction(identifier:).md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](sktestsession/disableautorenewfortransaction(identifier:).md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](sktestsession/forcerenewalofsubscription(productidentifier:).md)
  Ends the previous subscription period and begins the next period in the test environment.
- [func expireSubscription(productIdentifier: String) throws](sktestsession/expiresubscription(productidentifier:).md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.
### Testing billing retry and grace period
- [var billingGracePeriodIsEnabled: Bool](sktestsession/billinggraceperiodisenabled.md)
  A Boolean value that indicates whether the test environment simulates a billing grace period for auto-renewable subscriptions.
- [var shouldEnterBillingRetryOnRenewal: Bool](sktestsession/shouldenterbillingretryonrenewal.md)
  A Boolean value that indicates whether the testing environment enters a billing retry state when an auto-renewable subscription renews.
- [func resolveIssueForTransaction(identifier: Int) throws](sktestsession/resolveissuefortransaction(identifier:).md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.
### Testing price increase consent
- [func requestPriceIncreaseConsentForTransaction(identifier: Int) throws](sktestsession/requestpriceincreaseconsentfortransaction(identifier:).md)
  Simulates a price increase that requires customer consent for an auto-renewable subscription.
- [func consentToPriceIncreaseForTransaction(identifier: Int) throws](sktestsession/consenttopriceincreasefortransaction(identifier:).md)
  Simulates a user consenting to a price increase for an auto-renewable subscription.
- [func declinePriceIncreaseForTransaction(identifier: Int) throws](sktestsession/declinepriceincreasefortransaction(identifier:).md)
  Simulates a user canceling an auto-renewable subscription by disabling auto-renew.
### Testing externally performed transactions
- [func buyProduct(productIdentifier: String) throws](sktestsession/buyproduct(productidentifier:).md)
  Simulates buying an in-app purchase or subscription outside the app.
- [func refundTransaction(identifier: Int) throws](sktestsession/refundtransaction(identifier:).md)
  Simulates a refund for an in-app purchase that completes outside of the app.
### Instance Methods
- [func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption>) async throws -> Transaction](sktestsession/buyproduct(identifier:options:).md)
- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](sktestsession/setsimulatederror(_:forapi:).md)
- [func simulatedError<API>(forAPI: API) async -> API.Failure?](sktestsession/simulatederror(forapi:).md)

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
- [class SKTestTransaction](sktesttransaction.md)
  A transaction that occurs in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession)*