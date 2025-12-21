# notificationType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string notificationType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)

#### Discussion

The `notificationType appears` in the notification payload, [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). It describes the event that leads to the notification. Some notifications also have a [`subtype`](subtype.md) that further describes the event. See the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) for more information about the notification in the [`data`](data.md), [`summary`](summary.md), or [`externalPurchaseToken`](externalpurchasetoken.md) object.

##### Handle Use Cases for in App Purchase Life Cycle Events

When events occur that affect the customer’s In-App Purchase and subscription life cycle, the App Store server sends you notifications. The following tables list the notifications by life-cycle events.

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer purchases a consumable, non-consumable, or non-renewing subscription. | `ONE_TIME_CHARGE` |  |
| Customer redeems an offer code for a consumable, non-consumable, or non-renewing subscription. | `ONE_TIME_CHARGE` |  |
| Customer receives access to a non-consumable In-App Purchase through Family Sharing. | `ONE_TIME_CHARGE` |  |

Events that enable service for subscriptions, including initial subscriptions, resubscribing, and successful auto-renewals, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer subscribes for the first time to any subscription within a subscription group. | `SUBSCRIBED` | `INITIAL_BUY` |
| Customer resubscribes to any subscription from the same subscription group as their expired subscription. | `SUBSCRIBED` | `RESUBSCRIBE` |
| The subscription successfully auto-renews. | `DID_RENEW` |  |
| A family member gains access to the subscription through Family Sharing after the purchaser subscribes for the first time. | `SUBSCRIBED` | `INITIAL_BUY` |
| A family member gains access to the subscription through Family Sharing after the purchaser resubscribes. | `SUBSCRIBED` | `RESUBSCRIBE` |

Customers changing their subscription options, including upgrading, downgrading, or canceling, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer downgrades a subscription within the same subscription group. | `DID_CHANGE_RENEWAL_PREF` | `DOWNGRADE` |
| Customer reverts to the previous subscription, effectively canceling their downgrade. | `DID_CHANGE_RENEWAL_PREF` |  |
| Customer upgrades a subscription within the same subscription group. | `DID_CHANGE_RENEWAL_PREF` | `UPGRADE` |
| Customer cancels the subscription from the App Store Subscriptions settings page. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_DISABLED` |
| Customer subscribes again after canceling a subscription, which reenables auto-renew. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_ENABLED` |
| The system turned off auto-renew because the customer initiated a refund through your app using the refund request API. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_DISABLED` |

Customers redeeming offers, such as promotional offers, win-back offers, or offer codes result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer redeems a promotional offer or offer code for an active subscription. | `OFFER_REDEEMED` |  |
| Customer redeems an offer code to subscribe for the first time. | `SUBSCRIBED` | `INITIAL_BUY` |
| Customer redeems a promotional offer, offer code, or win-back offer after their subscription expired. | `SUBSCRIBED` | `RESUBSCRIBE` |
| Customer redeems a promotional offer or offer code to upgrade their subscription. | `OFFER_REDEEMED` | `UPGRADE` |
| Customer redeems a promotional offer and downgrades their subscription. | `OFFER_REDEEMED` | `DOWNGRADE` |
| Customer redeems an offer code for a consumable, non-consumable, or non-recurring subscription. | `ONE_TIME_CHARGE` |  |

Billing events, including billing retries, entering and exiting the billing grace period, and expiring subscriptions, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The subscription expires because the customer chose to cancel it. | `EXPIRED` | `VOLUNTARY` |
| The subscription expires because the developer removed the subscription from sale and the renewal fails. | `EXPIRED` | `PRODUCT_NOT_FOR_SALE` |
| The subscription expires because the billing retry period ends without recovering the subscription. | `EXPIRED` | `BILLING_RETRY` |
| The subscription fails to renew and enters the billing retry period. | `DID_FAIL_TO_RENEW` |  |
| The subscription fails to renew and enters the billing retry period with Billing Grace Period enabled. | `DID_FAIL_TO_RENEW` | `GRACE_PERIOD` |
| The billing retry successfully recovers the subscription. | `DID_RENEW` | `BILLING_RECOVERY` |
| The subscription exits the billing grace period (and continues in billing retry). | `GRACE_PERIOD_EXPIRED` |  |

Events or notifications that occur when you increase the price of an auto-renewable subscription include:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The system informs the customer of the auto-renewable subscription price increase that requires customer consent, and the customer doesn’t respond. | `PRICE_INCREASE` | `PENDING` |
| The auto-renewable subscription expires because the customer didn’t consent to the price increase that requires consent. | `EXPIRED` | `PRICE_INCREASE` |
| Customer consents to an auto-renewable subscription price increase that requires consent. | `PRICE_INCREASE` | `ACCEPTED` |
| The system notifies the customer of the auto-renewable subscription price increase that doesn’t require customer consent. | `PRICE_INCREASE` | `ACCEPTED` |
| Customer canceled the subscription after receiving a price increase notice or a request to consent to a price increase. | `DID_CHANGE_RENEWAL_STATUS` |  |

Customers requesting refunds or canceling Family Sharing result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Apple refunds the transaction for a consumable or non-consumable In-App Purchase, a non-renewing subscription, or an auto-renewable subscription. | `REFUND` |  |
| Apple reverses a previously granted refund due to a dispute that the customer raised. | `REFUND_REVERSED` |  |
| Apple declines a refund that the customer initiated in the app, using the request refund API. | `REFUND_DECLINED` |  |
| Apple requests consumption information for a refund request that a customer initiates. | `CONSUMPTION_REQUEST` |  |
| A family member loses access to the subscription through Family Sharing. | `REVOKE` |  |

Developers requesting subscription-renewal-date extensions result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The App Store successfully extends a subscription renewal date for a specific subscription. | `RENEWAL_EXTENDED` |  |
| The App Store successfully completes extending the subscription renewal date for all eligible subscribers. | `RENEWAL_EXTENSION` | `SUMMARY` |
| The App Store failed to extend the subscription renewal date for a specific subscriber. | `RENEWAL_EXTENSION` | `FAILURE` |

## See Also

- [App Store Server Notifications V2](app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2](responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [object responseBodyV2DecodedPayload](responsebodyv2decodedpayload.md)
  A decoded payload that contains the version 2 notification data.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)*