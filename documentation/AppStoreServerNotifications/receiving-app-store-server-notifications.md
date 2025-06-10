# Receiving App Store Server Notifications

**Framework**: App Store Server Notifications

Implement server-side code to receive and parse notification posts.

#### Overview

The App Store delivers JSON objects using an HTTP POST to your server for notable in-app purchase events and unreported external purchase tokens. Your server is responsible for parsing, interpreting, and responding to all server-to-server notification posts. For more information about responding, see [`Responding to App Store Server Notifications`](responding-to-app-store-server-notifications.md).

The body of the POST contains the data elements described in the [`responseBodyV2`](responsebodyv2.md) for version 2 notifications, and [`responseBodyV1`](responsebodyv1.md) for version 1. Parse them using the following information:

- The version 2 response body, [`responseBodyV2`](responsebodyv2.md), contains a [`signedPayload`](signedpayload.md) that’s cryptographically signed by the App Store in JSON Web Signature (JWS) format. The JWS format increases security and enables you to decode and validate the signature on your server.  Some notifications include a [`data`](data.md) object, which has transaction and subscription renewal information that the App Store signs in JWS. The [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI) and the StoreKit [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) API use the same JWS-signed format for transaction and subscription status information. For more information about JWS, see the [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.
- The version 1 response body, [`responseBodyV1`](responsebodyv1.md), is a JSON object. It includes the receipt that contains the most recent in-app purchase transaction for the app. For more information, see the [`unified_receipt`](unified_receipt.md) object.

> ❗ **Important**:  The [`App Store Server Notifications V1`](app-store-server-notifications-v1.md) endpoint and version 1 notifications, [`notification_type`](notification_type.md), are deprecated. Instead, implement the [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) endpoint on your server to receive version 2 notifications.

Use the notification type along with the transaction and subscription renewal information to update a user’s service or present promotional offers according to your business logic. For information on handling notifications that contain an external purchase token, see [`externalPurchaseToken`](externalpurchasetoken.md).

## See Also

- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Responding to App Store Server Notifications](responding-to-app-store-server-notifications.md)
  Send HTTP status codes to indicate the success of a notification post.
- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
  Learn about changes to the App Store Server Notifications service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/receiving-app-store-server-notifications)*