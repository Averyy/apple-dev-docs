# Testing App Store server notifications

**Framework**: StoreKit

Confirm that App Store Server Notifications service responds properly in the sandbox environment.

#### Overview

If you enabled notifications from the App Store for your app, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field equals `Sandbox` in the [`data`](https://developer.apple.com/documentation/AppStoreServerNotifications/data) object of the App Store Server Notifications [`responseBodyV2DecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) object.

For more information about the App Store Server Notifications service, see [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications). To ask the App Store to send test notifications, and to get a history of notifications sent to your server, see [`Request a Test Notification`](https://developer.apple.com/documentation/AppStoreServerAPI/Request-a-Test-Notification) and [`Get Notification History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Notification-History) in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-app-store-server-notifications)*