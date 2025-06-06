# Testing refund requests

**Framework**: StoreKit

Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.

#### Overview

The sandbox environment and StoreKit Testing in Xcode both support testing refund requests, which enable your customers to request a refund from within your app. Your app displays the refund request sheet by calling any of these methods: [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-65tph.md) , [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-63bvd.md), [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-9mscy.md), [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-9k0pj.md), or [`refundRequestSheet(for:isPresented:onDismiss:)`](https://developer.apple.com/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:)). Customers fill out the sheet to submit the request.

Depending on your testing setup, the App Store automatically approves or declines the refund request in the testing environment. Note that the App Store doesn’t send emails for refund requests in testing environments.

##### Test Approved Refunds

To set up a test for approved refunds, select any refund reason on the refund request sheet, and submit the sheet. The App Store automatically approves the refund request in the testing environment.

Your app receives a [`Transaction`](transaction.md) with refund information in the [`revocationDate`](transaction/revocationdate.md) and [`revocationReason`](transaction/revocationreason-swift.property.md) properties. If you’re testing in the sandbox environment and your server receives [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) for the sandbox, it gets a notification with a `REFUND` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType).

##### Test Declined Refunds

To set up a test for declined refunds, follow these steps on the refund request sheet with your app running in the sandbox environment:

1. Under Issue, select Other.
2. In the text box, type REJECT.
3. Tap Request Refund.

The App Store automatically rejects the refund request in the testing environment.

If your server receives [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) for the sandbox environment, it gets a notification with a `REFUND_DECLINED` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType).

For more information on receiving server notifications for the sandbox environment, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md). For more information on testing, see [`Testing at all stages of development with Xcode and the sandbox`](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) and [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

## See Also

- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
  Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)
  Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md)
  Validate your app’s handling of win-back offers that you configure for the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-refund-requests)*