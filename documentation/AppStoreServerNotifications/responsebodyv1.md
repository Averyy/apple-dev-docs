# responseBodyV1

**Framework**: App Store Server Notifications  
**Kind**: dictionary  
**Role**: Object

The response body containing JSON data that the App Store sends in a version 1 server notification.

**Availability**:
- App Store Server Notifications 1.0+ - Deprecated in 2.8

> **Deprecated**: Implement the [`App Store Server Notifications V2`](./app-store-server-notifications-v2.md) endpoint on your server to receive version 2 notifications instead.

## Declaration

```
object responseBodyV1
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](./receiving-app-store-server-notifications.md)

#### Discussion

Use the information in the response body to react quickly to changes in your users’ subscription states. The fields available in a notification sent to your server depend on the [`notification_type`](./responsebodyv1/notification_type.md), which indicates the event that triggered the notification.

## Topics

### Unified receipt object
- [object unified_receipt](./unified_receipt.md)
  An object that contains information about the most recent in-app purchase transactions for the app.

## Properties

- `auto_renew_adam_id` (string) *(deprecated)*: An identifier that App Store Connect generates and the App Store uses to uniquely identify the auto-renewable subscription that the user’s subscription renews. Treat this value as a 64-bit integer.
- `auto_renew_product_id` (string) *(deprecated)*: The product identifier of the auto-renewable subscription that the user’s subscription renews.
- `auto_renew_status` (string) *(deprecated)*: The current renewal status for an auto-renewable subscription product. Note that these values are the strings `“true”` and `“false”`, and not the strings `“0”` or `“1”` that appear in [`auto_renew_status`](../AppStoreReceipts/auto_renew_status.md) in the receipt.

  **Allowed Values**: `true`, `false`
- `auto_renew_status_change_date` (string) *(deprecated)*: The time at which the user turned on or off the renewal status for an auto-renewable subscription, in a date-time format similar to the ISO 8601 standard.
- `auto_renew_status_change_date_ms` (string) *(deprecated)*: The time at which the user turned on or off the renewal status for an auto-renewable subscription, in UNIX time, in milliseconds. Use this time format to process dates.
- `auto_renew_status_change_date_pst` (string) *(deprecated)*: The time at which the user turned on or off the renewal status for an auto-renewable subscription, in Pacific standard time.
- `bid` (string) *(deprecated)*: A string that contains the app bundle ID.
- `bvrs` (string) *(deprecated)*: A string that contains the app bundle version.
- `deprecation` (string) *(deprecated)*: The date that [`App Store Server Notifications V1`](./app-store-server-notifications-v1.md) are deprecated. For more information, see [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md).
- `environment` (string) *(deprecated)*: The environment for which the App Store generated the receipt.

  **Allowed Values**: `Sandbox`, `PROD`
- `expiration_intent` (integer) *(deprecated)*: The reason a subscription expired. This field is only present for an expired auto-renewable subscription. See [`expiration_intent`](../AppStoreReceipts/expiration_intent.md) for more information.
- `notification_type` (notification_type) *(deprecated)*: The subscription event that triggered the notification. See [`notification_type`](./responsebodyv1/notification_type.md) for the complete list of version 1 notification types.
- `original_transaction_id` (long) *(deprecated)*: The original transaction identifier for which App Store Server Notifications sends the notification.
- `password` (string) *(deprecated)*: The same value as the shared secret you submit in the `password` field of the App Store Receipt [`requestBody`](../AppStoreReceipts/requestbody.md) when validating receipts.
- `unified_receipt` (unified_receipt) *(deprecated)*: An object that contains information about the most recent in-app purchase transactions for the app.

## See Also

### Version 1 notifications
- [App Store Server Notifications V1](./app-store-server-notifications-v1.md)
  Specify your secure server’s URL in App Store Connect to receive version 1 notifications.
- [type notification_type](./notification_type.md)
  The type that describes the in-app purchase event for which the App Store sends the version 1 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv1)*