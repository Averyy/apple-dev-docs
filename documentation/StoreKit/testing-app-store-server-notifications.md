# Testing App Store server notifications

**Framework**: StoreKit

Confirm that App Store Server Notifications service responds properly in the sandbox environment.

#### Overview

If you enabled notifications from the App Store for your app, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field equals `Sandbox` in the [`data`](https://developer.apple.com/documentation/appstoreservernotifications/data) object of the App Store Server Notifications [`responseBodyV2DecodedPayload`](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2decodedpayload) object.

For more information about the App Store Server Notifications service, see [`App Store Server Notifications`](https://developer.apple.com/documentation/appstoreservernotifications). To ask the App Store to send test notifications, and to get a history of notifications sent to your server, see [`Request a Test Notification`](https://developer.apple.com/documentation/appstoreserverapi/request-a-test-notification) and [`Get Notification History`](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history) in the [`App Store Server API`](https://developer.apple.com/documentation/appstoreserverapi).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-app-store-server-notifications)*