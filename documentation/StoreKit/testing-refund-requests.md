# Testing refund requests

**Framework**: StoreKit  
**Role**: Article

Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.

## Overview

The sandbox environment and StoreKit Testing in Xcode both support testing refund requests, which enable your customers to request a refund from within your app. Your app displays the refund request sheet by calling any of these methods: [`beginRefundRequest(for:in:)`](./transaction/beginrefundrequest%28for,in%29-65tph.md) , [`beginRefundRequest(in:)`](./transaction/beginrefundrequest%28in%29-63bvd.md), [`beginRefundRequest(for:in:)`](./transaction/beginrefundrequest%28for,in%29-9mscy.md), [`beginRefundRequest(in:)`](./transaction/beginrefundrequest%28in%29-9k0pj.md), or [`refundRequestSheet(for:isPresented:onDismiss:)`](../SwiftUI/view/refundrequestsheet%28for,ispresented,ondismiss%29.md). While you’re testing your app, you fill out the sheet to submit the request.

Depending on your testing setup, the App Store automatically approves or declines the refund request in the testing environment. Note that the App Store doesn’t send emails for refund requests in testing environments.

### Test approved refunds

To set up a test for approved refunds, select any refund reason on the refund request sheet, and submit the sheet. The App Store automatically approves the refund request in the testing environment.

Your app receives a [`Transaction`](./transaction.md) with refund information in the [`revocationDate`](./transaction/revocationdate.md) and [`revocationReason`](./transaction/revocationreason-swift.property.md) properties. If you’re testing in the sandbox environment and your server receives [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) for the sandbox, it gets a notification with a `REFUND` [`notificationType`](../AppStoreServerNotifications/notificationtype.md).

### Test declined refunds

To set up a test for declined refunds, follow these steps on the refund request sheet with your app running in the sandbox environment:

1. Under Issue, select Other.
2. In the text box, type DECLINE.
3. Tap Request Refund.

The App Store automatically rejects the refund request in the testing environment.

If your server receives [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) for the sandbox environment, it gets a notification with a `REFUND_DECLINED` [`notificationType`](../AppStoreServerNotifications/notificationtype.md).

### Test prorated refunds

To set up a test for prorated refunds, follow these steps on the refund request sheet with your app running in the sandbox environment:

1. Under Issue, select Other.
2. In the text box, type GRANT_PRORATED.
3. Tap Request Refund.

The testing environment determines the prorated percentages as follows:

- For auto-renewable subscriptions, it calculates the proration based on the time that remains on the subscription
- For consumables, non-consumables, and non-renewing subscriptions, it uses a default proration of 50%

In the testing environment, the App Store automatically approves the prorated refund.

Your app receives a [`Transaction`](./transaction.md) with refund information in the [`revocationDate`](./transaction/revocationdate.md) and [`revocationReason`](./transaction/revocationreason-swift.property.md) properties. If you’re testing in the sandbox environment and your server receives [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) for the sandbox, it gets a notification with a `REFUND` [`notificationType`](../AppStoreServerNotifications/notificationtype.md). For prorated refunds, the transaction data includes the `revocationType` field with a value of `REFUND_PRORATED` and the `revocationPercentage` field.

### Test prorated refunds with information from your server

Another way to test prorated refunds is to provide the refund information by calling the [`Send Consumption Information`](../AppStoreServerAPI/send-consumption-information.md), following these steps:

1. In your app, select any refund reason on the refund request sheet, and submit the sheet.
2. The App Store server sends a `CONSUMPTION_REQUEST` notification to your [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) for the sandbox environment.
3. Respond by calling [`Send Consumption Information`](../AppStoreServerAPI/send-consumption-information.md). Note that in the sandbox environment you need to respond to the notification within five minutes for the system to apply your consumption information to the refund request.

The values you provide in the [`ConsumptionRequest`](../AppStoreServerAPI/consumptionrequest.md) determine the outcome of the refund in the testing environment:

- Specify the `GRANT_PRORATED` value as the refund preference to get a prorated refund
- Specify a valid `consumptionPercentage`. The testing environment approves the prorated refund using your consumption percentage.

For more information on receiving server notifications for the sandbox environment, see [Enabling App Store Server Notifications](./enabling-app-store-server-notifications.md). For more information on testing, see [Testing at all stages of development with Xcode and the sandbox](./testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) and [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md).

## See Also

### Apple In-App Purchase Testing
- [Testing at all stages of development with Xcode and the sandbox](./testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of Apple In-App Purchases by testing your code throughout its development.
- [Testing Apple In-App Purchases with sandbox](./testing-in-app-purchases-with-sandbox.md)
  Test your implementation of Apple In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing win-back offers in Xcode](./testing-win-back-offers-in-xcode.md)
  Validate your app’s handling of win-back offers that you configure for the testing environment.
- [Testing Ask to Buy in Xcode](./testing-ask-to-buy-in-xcode.md)
  Validate your app’s handling of Ask To Buy in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-refund-requests)*