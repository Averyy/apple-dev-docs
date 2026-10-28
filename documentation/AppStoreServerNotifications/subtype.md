# subtype

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

A string that provides details about select notification types in version 2.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
string subtype
```

## Possible Values

- `ACCEPTED`: Applies to the `PRICE_INCREASE` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the customer consented to the subscription price increase if the price increase requires customer consent, or that the system notified them of a price increase if the price increase doesn’t require customer consent.
- `ACTIVE_TOKEN_REMINDER`: Applies to the `EXTERNAL_PURCHASE_TOKEN` [`notificationType`](./notificationtype.md). A notification with this subtype is a reminder that Apple created a custom link external purchase token for your app, and the token is still active. App Store Server sends this notification monthly while the token is active, unless you report the token as a duplicate. For information about reporting tokens, see [`externalPurchaseToken`](./externalpurchasetoken.md).
- `AUTO_RENEW_DISABLED`: Applies to the `DID_CHANGE_RENEWAL_STATUS` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the customer turned off subscription auto-renewal, or the App Store turned off subscription auto-renewal after the customer requested a refund.
- `AUTO_RENEW_ENABLED`: Applies to the `DID_CHANGE_RENEWAL_STATUS` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the customer enabled subscription auto-renewal.
- `BILLING_RECOVERY`: Applies to the `DID_RENEW` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the expired subscription that previously failed to renew has successfully renewed.
- `BILLING_RETRY`: Applies to the EXPIRED notificationType. A notification with this subtype indicates that the subscription expired because the subscription failed to renew before the billing retry period ended.
- `CREATED`: Applies to the `EXTERNAL_PURCHASE_TOKEN` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that Apple created a custom link token for your app. For more information about custom link tokens, see [Receiving and decoding external purchase tokens](../StoreKit/receiving-and-decoding-external-purchase-tokens.md).
- `DOWNGRADE`: Applies to the `DID_CHANGE_RENEWAL_PREF` and `OFFER_REDEEMED` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the customer downgraded their subscription or cross-graded to a subscription with a different duration. Downgrades take effect at the next renewal date.
- `FAILURE`: Applies to the `RENEWAL_EXTENSION` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the subscription-renewal-date extension failed for an individual subscription. For details, see the [`data`](./data.md) object in the [`responseBodyV2DecodedPayload`](./responsebodyv2decodedpayload.md). For information on the request, see [`Extend Subscription Renewal Dates for All Active Subscribers`](../AppStoreServerAPI/extend-subscription-renewal-dates-for-all-active-subscribers.md).
- `GRACE_PERIOD`: Applies to the `DID_FAIL_TO_RENEW` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the subscription failed to renew due to a billing issue. Continue to provide access to the subscription during the grace period.
- `INITIAL_BUY`: Applies to the `SUBSCRIBED` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the customer purchased the subscription for the first time or that the customer received access to the subscription through Family Sharing for the first time.
- `PENDING`: Applies to the `PRICE_INCREASE` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the system informed the customer of the subscription price increase, but the customer hasn’t accepted it.
- `PRICE_INCREASE`: Applies to the `EXPIRED` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the subscription expired because the customer didn’t consent to a price increase.
- `PRODUCT_NOT_FOR_SALE`: Applies to the `EXPIRED` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the subscription expired because the product wasn’t available for purchase at the time the subscription attempted to renew.
- `RESUBSCRIBE`: Applies to the `SUBSCRIBED` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the customer resubscribed or received access through Family Sharing to the same subscription or to another subscription within the same subscription group.
- `SUMMARY`: Applies to the `RENEWAL_EXTENSION` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the App Store server completed your request to extend the subscription renewal date for all eligible subscribers. For the summary details, see the [`summary`](./summary.md) object in the [`responseBodyV2DecodedPayload`](./responsebodyv2decodedpayload.md). For information on the request, see [`Extend Subscription Renewal Dates for All Active Subscribers`](../AppStoreServerAPI/extend-subscription-renewal-dates-for-all-active-subscribers.md).
- `UPGRADE`: Applies to the `DID_CHANGE_RENEWAL_PREF` and `OFFER_REDEEMED` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that the customer upgraded their subscription or cross-graded to a subscription with the same duration. Upgrades take effect immediately.
- `UNREPORTED`: Applies to the `EXTERNAL_PURCHASE_TOKEN` [`notificationType`](./notificationtype.md). A notification with this `subtype` indicates that Apple created a token for your app but didn’t receive a report. For more information about reporting the token, see [`externalPurchaseToken`](./externalpurchasetoken.md).
- `VOLUNTARY`: Applies to the `EXPIRED` [`notificationType`](./notificationtype.md). A notification with this subtype indicates that the subscription expired after the customer turned off subscription auto-renewal.

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

This `subtype` field is part of the [`responseBodyV2DecodedPayload`](./responsebodyv2decodedpayload.md), and further describes an event of type [`notificationType`](./notificationtype.md). It’s present only for specific version 2 notifications.

## See Also

### Server notifications version 2
- [App Store Server Notifications V2](./app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2](./responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [object responseBodyV2DecodedPayload](./responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type notificationType](./notificationtype.md)
  The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/subtype)*