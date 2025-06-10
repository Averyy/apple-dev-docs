# StoreKit Test

**Framework**: StoreKit Test  
**Kind**: module

Create and automate tests in Xcode for your app’s subscription and in-app purchase transactions, and SKAdNetwork implementations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.4+

#### Overview

The StoreKitTest framework makes StoreKit testing in Xcode available for automation. Use this framework to write unit tests and continuous integration tests. Use [`SKTestSession`](sktestsession.md) and [`SKAdTestSession`](skadtestsession.md) to control the test environment.

For testing in-app purchase transactions, use `SKTestSession`. Each instance of `SKTestSession` gives you access to the same settings you manually change for StoreKit testing in Xcode. Use this class to test a variety of in-app purchase scenarios, such as subscription renewals and Ask to Buy transactions, and maintain control over the transactions in the testing environment.

For testing ad impressions and postbacks, use `SKAdTestSession`. Each instance of `SKAdTestSession` holds a set of test postbacks that you create and can use in multiple unit tests. Ad networks that use [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) APIs can use this class to validate the ad impressions that they sign, and test receiving postbacks on their server. Advertised apps can test their conversion value updates.

Testing StoreKit in iOS, watchOS, or tvOS apps requires Xcode 12 or later running on macOS 10.15 or later. Testing StoreKit in a macOS app requires Xcode 12 or later running on macOS 11 or later.

> **Note**:  Session 10659 : [`Introducing StoreKit testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/wwdc20/10659)

## Topics

### StoreKit transaction testing
- [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md)
  Prepare your test environment to test in-app purchases with data you configure locally.
- [class SKTestSession](sktestsession.md)
  The controls and environment configuration you use to test StoreKit transactions in Xcode.
- [class SKTestTransaction](sktesttransaction.md)
  A transaction that occurs in the testing environment.
### StoreKit transaction testing errors
- [let SKTestErrorDomain: String](sktesterrordomain.md)
  A constant that represents the domain for error codes in the testing environment.
- [struct SKTestError](sktesterror.md)
  Information about an error that the testing environment returns.
### Ad impression and postback testing
- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- [class SKAdTestSession](skadtestsession.md)
  The class you use to test ad impressions and postbacks in Xcode.
- [class SKAdTestPostback](skadtestpostback.md)
  A test postback that contains ad conversion information in the testing environment.
- [class SKAdTestPostbackResponse](skadtestpostbackresponse.md)
  The status and error information for a postback that the system sends in the testing environment.
- [struct SKAdTestPostbackVersion](skadtestpostbackversion.md)
  A constant that indicates the postback version.
### Ad impression and postback errors
- [let SKAdTestErrorDomain: String](skadtesterrordomain.md)
  A string that identifies the error domain for SKAdNetwork testing in the testing environment.
- [struct SKAdTestError](skadtesterror.md)
  An error the testing environment returns for SKAdNetwork testing errors.
### Structures
- [struct StoreKitAppStoreSyncAPI](storekitappstoresyncapi.md)
- [struct StoreKitAppTransactionAPI](storekitapptransactionapi.md)
- [struct StoreKitLoadProductsAPI](storekitloadproductsapi.md)
- [struct StoreKitManageSubscriptionsAPI](storekitmanagesubscriptionsapi.md)
- [struct StoreKitOfferCodeRedeemAPI](storekitoffercoderedeemapi.md)
- [struct StoreKitPurchaseAPI](storekitpurchaseapi.md)
- [struct StoreKitRefundRequestAPI](storekitrefundrequestapi.md)
- [struct StoreKitSubscriptionStatusAPI](storekitsubscriptionstatusapi.md)
- [struct StoreKitVerificationAPI](storekitverificationapi.md)
### Enumerations
- [enum SKTestFailures](sktestfailures.md)
### Protocols
- [protocol FailableStoreKitAPI](failablestorekitapi.md)
- [protocol SKTestFailure](sktestfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKitTest)*