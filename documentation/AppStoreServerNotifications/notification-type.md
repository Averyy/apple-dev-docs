# notification_type

**Framework**: Appstoreservernotifications  
**Kind**: typealias

The type that describes the in-app purchase event for which the App Store sends the version 1 notification.

**Availability**:
- App Store Server Notifications 1.0+

## Declaration

```swift
string notification_type
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

You receive and can react to server notifications in real time for the subscription and refund events that these notification type values describe. The `notification_type` appears in the [`responseBodyV1`](responsebodyv1.md).

> **Note**:  If you’re receiving App Store Server Notifications Version 2, see [`responseBodyV2`](responsebodyv2.md) and [`notificationType`](notificationtype.md) instead.

##### Handle Use Cases for Notification Events

When events occur that affect the customer’s product and subscription life-cycle, your server receives notifications from the App Store. Here are some examples of product events and the server notifications you can expect to receive:

| Subscription or in-app purchase event | Notification types |
| --- | --- |
| Customer completed an initial purchase of a subscription | `INITIAL_BUY` |
| Subscription is active; customer upgraded to another SKU | `DID_CHANGE_RENEWAL_STATUS`, `INTERACTIVE_RENEWAL` |
| Subscription is active; customer downgraded to another SKU | `DID_CHANGE_RENEWAL_PREF` |
| Subscription has expired; customer resubscribed to the same SKU | `DID_CHANGE_RENEWAL_STATUS` |
| Subscription has expired; customer resubscribed to another SKU (upgrade or downgrade) | `INTERACTIVE_RENEWAL`, `DID_CHANGE_RENEWAL_STATUS` |
| Customer canceled the subscription from the App Store Subscriptions settings page. Their subscription will not auto-renew and will expire on the `expires_date` | `DID_CHANGE_RENEWAL_STATUS` |
| Customer previously canceled the subscription, but now resubscribed to same product before the subscription expired. The subscription will auto-renew on the `expires_date` | `DID_CHANGE_RENEWAL_STATUS` |
| AppleCare refunded a subscription | `CANCEL`, `DID_CHANGE_RENEWAL_STATUS` |
| Subscription failed to renew because of a billing issue | `DID_FAIL_TO_RENEW` |
| Expired subscription recovered by App Store through a billing retry | `DID_RECOVER` |
| Subscription churned after failed billing retry attempts | `DID_CHANGE_RENEWAL_STATUS` |
| AppleCare successfully refunded the transaction for a consumable, non-consumable, or a non-renewing subscription | `REFUND` |
| You’ve increased the price of an auto-renewable subscription and the price increase requires customer consent before the subscription auto-renews | `PRICE_INCREASE_CONSENT` |
| Subscription successfully auto-renewed | `DID_RENEW` |
| A purchaser disabled Family Sharing for a product, the purchaser (or family member) left the family group, or the purchaser asked for and received a refund | `REVOKE` |
| The customer initiated a refund request for a consumable in-app purchase | `CONSUMPTION_REQUEST` |

##### Receive Notifications for the Purchaser and Family Members

The following table identifies the notifications you receive for the purchaser and for their family members who share products through Family Sharing. To determine if a notification is for the purchaser or a family member, check the value of the [`in_app_ownership_type`](https://developer.apple.com/documentation/appstorereceipts/in_app_ownership_type) field, which appears in the [`unified_receipt.Latest_receipt_info`](unified_receipt/latest_receipt_info-data.dictionary.md) of the `responseBody` object. For more information about Family Sharing, see [`Supporting Family Sharing in your app`](https://developer.apple.com/documentation/StoreKit/supporting-family-sharing-in-your-app).

| Notification type | Received for Purchaser | Received for Family Members |
| --- | --- | --- |
| `CANCEL` | YES | NO |
| `CONSUMPTION_REQUEST` | YES | N/A |
| `DID_CHANGE_RENEWAL_PREF` | YES | YES |
| `DID_CHANGE_RENEWAL_STATUS` | YES | YES |
| `DID_FAIL_TO_RENEW` | YES | YES |
| `DID_RECOVER` | YES | YES |
| `DID_RENEW` | YES | YES |
| `INITIAL_BUY` | YES | NO |
| `INTERACTIVE_RENEWAL` | YES | YES |
| `PRICE_INCREASE_CONSENT` | YES | NO |
| `REFUND` | YES | NO |
| `REVOKE` | NO | YES |
| `RENEWAL` (Deprecated) | N/A | N/A |

The `CONSUMPTION_REQUEST` notification applies to consumable in-app purchases, which aren’t eligible for Family Sharing.

##### Test Notification Events with Sandbox

Your development-signed apps use the sandbox environment when you sign in to App Store using a Sandbox Apple Account. To create a Sandbox Apple Account or test account in App Store Connect, see [`Create a sandbox tester account`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev8b997bee1).

If you enabled App Store Server Notifications, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field in the JSON [`responseBodyV1`](responsebodyv1.md) object equals `Sandbox`.

The following notification types are available in sandbox: `INITIAL_BUY`, `DID_CHANGE_RENEWAL_PREF`, `DID_CHANGE_RENEWAL_STATUS`, `DID_RENEW`, `INTERACTIVE_RENEWAL`, `CANCEL`, and `REFUND`. Notifications in the sandbox environment are for the purchaser only, and have [`in_app_ownership_type`](https://developer.apple.com/documentation/appstorereceipts/in_app_ownership_type) equal to `PURCHASED`. For more information about testing in-app purchases, see [`Testing In-App Purchases with sandbox`](https://developer.apple.com/documentation/StoreKit/testing-in-app-purchases-with-sandbox).

## See Also

- [App Store Server Notifications V1](app-store-server-notifications-v1.md)
  Specify your secure server’s URL in App Store Connect to receive version 1 notifications.
- [object responseBodyV1](responsebodyv1.md)
  The response body containing JSON data that the App Store sends in a version 1 server notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/notification_type)*