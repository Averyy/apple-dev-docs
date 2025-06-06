# requestPriceIncreaseConsentForTransaction(identifier:)

**Framework**: Storekittest  
**Kind**: method

Simulates a price increase that requires customer consent for an auto-renewable subscription.

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
func requestPriceIncreaseConsentForTransaction(identifier: Int) throws
```

#### Discussion

Use this method to test how your app handles a price increase consent flow. When you call this method, the testing environment assigns a pending price increase to the subscription indicated by the `identifier`. It also sends the price increase consent message to your app. Note that in the testing environment, changing the price of the subscription is optional.

You may call this method repeatedly to prompt the testing environment to send the price increase consent message.

> **Note**:  The system displays a price increase consent sheet in iOS only. On other supported platforms, use [`requestPriceIncreaseConsentForTransaction(identifier:)`](sktestsession/requestpriceincreaseconsentfortransaction(identifier:).md) to test that your app handles the subscription status update correctly.

By default, if your app doesn’t listen for [`messages`](https://developer.apple.com/documentation/StoreKit/Message/messages-swift.type.property) or implement [`paymentQueueShouldShowPriceConsent(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)), the system displays the price increase consent sheet immediately. Your app may delay displaying the sheet to ensure a good user experience. For more information, see [`Message.Messages`](https://developer.apple.com/documentation/StoreKit/Message/Messages-swift.struct) for apps that run in iOS 16 and later, and [`paymentQueueShouldShowPriceConsent(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)) and [`showPriceConsentIfNeeded()`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/showPriceConsentIfNeeded()) for apps that run in earlier versions.

When the system displays the price increase consent sheet, it awaits a response from the user, which may be one of the following:

- The user consents to the price increase.
- The user does nothing. The subscription expires at the end of the subscription period.
- The user cancels the subscription.

See the sections below for information about simulating these user responses in the testing environment. The system removes the pending price increase status when the user consents to the price increase, the subscription expires, or the user cancels the subscription and auto-renew is disabled.

For more information about increasing prices of auto-renewable subscriptions, see [`Managing prices`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers).

##### Test with Dialogs Enabled

Start with [`disableDialogs`](sktestsession/disabledialogs.md) set to `false`, so the system displays the price increase consent sheet in the testing environment.

To simulate a user consenting to a price increase, the tester consents to the price increase in the sheet. The auto-renewable subscription renews at the next renewal period.

To simulate a user not responding to the price increase, the tester closes the price increase consent sheet without consenting. The auto-renewable subscription expires at the end of the renewal period because the user didn’t consent to the price increase. To speed up the subscription expiration in the testing environment, set a shorter time rate in the [`timeRate`](sktestsession/timerate-swift.property.md) variable.

To simulate a user canceling their subscription, the tester closes the price increase consent sheet without consenting. On the next sheet, select to cancel the subscription. The auto-renewable subscription doesn’t renew at the next renewal period.

##### Test with Dialogs Disabled

Start with [`disableDialogs`](sktestsession/disabledialogs.md) set to `true`, so the system doesn’t displays the price increase consent sheet in the testing environment.

> **Note**:  The system doesn’t display any sheets in the testing environment if [`disableDialogs`](sktestsession/disabledialogs.md) is `true`.

To simulate a user consenting to a price increase, call [`consentToPriceIncreaseForTransaction(identifier:)`](sktestsession/consenttopriceincreasefortransaction(identifier:).md). The auto-renewable subscription renews at the next renewal period.

To simulate a user not responding to the price increase consent, wait until the end of the subscription’s renewal period. The auto-renewable subscription expires because the user didn’t consent to the price increase. To speed up the subscription expiration in the testing environment, set a shorter time rate in the [`timeRate`](sktestsession/timerate-swift.property.md) variable.

To simulate the user canceling their subscription, call [`declinePriceIncreaseForTransaction(identifier:)`](sktestsession/declinepriceincreasefortransaction(identifier:).md). The subscription doesn’t renew at the next renewal period because the auto-renew setting is off.

## Parameters

- `identifier`: The transaction   of the auto-renewable subscription to get a pending price increase.

## See Also

- [func consentToPriceIncreaseForTransaction(identifier: Int) throws](sktestsession/consenttopriceincreasefortransaction(identifier:).md)
  Simulates a user consenting to a price increase for an auto-renewable subscription.
- [func declinePriceIncreaseForTransaction(identifier: Int) throws](sktestsession/declinepriceincreasefortransaction(identifier:).md)
  Simulates a user canceling an auto-renewable subscription by disabling auto-renew.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/requestpriceincreaseconsentfortransaction(identifier:))*