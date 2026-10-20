# Testing App Store server notifications

**Framework**: StoreKit  
**Role**: Article

Confirm that App Store Server Notifications service responds properly in the sandbox environment.

#### Overview

If you enabled notifications from the App Store for your app, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field equals `Sandbox` in the [`data`](../AppStoreServerNotifications/data.md) object of the App Store Server Notifications [`responseBodyV2DecodedPayload`](../AppStoreServerNotifications/responsebodyv2decodedpayload.md) object.

For more information about the App Store Server Notifications service, see [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md). To ask the App Store to send test notifications, and to get a history of notifications sent to your server, see [`Request a Test Notification`](../AppStoreServerAPI/request-a-test-notification.md) and [`Get Notification History`](../AppStoreServerAPI/get-notification-history.md) in the [App Store Server API](../AppStoreServerAPI/AppStoreServerAPI.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-app-store-server-notifications)*