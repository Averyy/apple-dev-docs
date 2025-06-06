# Managing Price Increases for Auto-Renewable Subscriptions

**Framework**: StoreKit

Identify the price increase status for auto-renewable subscriptions in your app and on your server.

#### Overview

If you increase the price of an auto-renewable subscription in App Store Connect, the [`priceIncreaseStatus`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md) in the [`renewalInfo`](product/subscriptioninfo/status-swift.struct/renewalinfo.md) object indicates if the subscription is subject to the price increase. Auto-renewable subscriptions have two types of price increases: those that require customer consent, and those that don’t require customer consent.

For price increases that require customer consent, look for the following status values in your app:

| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/noincreasepending.md) | Indicates there’s no price increase for this auto-renewable subscription. |
| --- | --- |
| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/pending.md) | Indicates there’s a pending price increase for the auto-renewable subscription that requires customer consent, and the customer hasn’t yet consented.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If the customer doesn’t consent, the auto-renewable subscription expires at the end of the billing cycle. When it expires, your app gets a status update in [`updates`](product/subscriptioninfo/status-swift.struct/updates.md) with an [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) of [`didNotConsentToPriceIncrease`](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease.md). |
| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed.md) | Indicates that the customer consented to a price increase for the auto-renewable subscription. |

For price increases that don’t require customer consent, look for the following status values in your app:

| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/noincreasepending.md) | Doesn’t apply. |
| --- | --- |
| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/pending.md) | Doesn’t apply. |
| [`Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed`](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed.md) | Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the subscription is subject to the price increase. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If the customer cancels the auto-renewable subscription, your app gets a status update in [`updates`](product/subscriptioninfo/status-swift.struct/updates.md) with an [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) of [`autoRenewDisabled`](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/autorenewdisabled.md). |

For more information about managing subscription prices in App Store Connect, see [`Managing Prices`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers).

##### Receive Notifications for Price Increase Status Events

If you’ve enabled [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2), your server receives notifications for events related to auto-renewable subscription price increases.

For auto-renewable subscription price increases that require customer consent, look for the following notifications:

| Notification type | Subtype | Description |
| --- | --- | --- |
| `PRICE_INCREASE` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) | `PENDING` | Indicates that the App Store informed the customer of the price increase for the auto-renewable subscription, and the customer hasn’t yet responded. |
| `PRICE_INCREASE` | `ACCEPTED` | Indicates that the customer consented to the price increase for the auto-renewable subscription. |
| `EXPIRED` | `PRICE_INCREASE` | Indicates that the auto-renewable subscription expired because the customer didn’t consent to the price increase, and allowed the subscription to expire. |
| `EXPIRED` | `VOLUNTARY` | Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn’t specific to price increases.) |

For auto-renewable subscription price increases that don’t require customer consent, look for the following notifications:

| Notification type | Subtype | Description |
| --- | --- | --- |
| `PRICE_INCREASE` | `ACCEPTED` | Indicates that the App Store informed the customer of the auto-renewable subscription price increase, and the subscription is subject to the price increase. |
| `EXPIRED` | `VOLUNTARY` | Indicates that the customer voluntarily canceled the auto-renewable subscription. (Note: This notification type and subtype isn’t specific to price increases.) |

For more information about App Store Server Notifications, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md). For more information about notification types and subtypes, see [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) and [`subtype`](https://developer.apple.com/documentation/AppStoreServerNotifications/subtype).

## See Also

- [let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md)
  The status that indicates whether the auto-renewable subscription is subject to a price increase.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum.md)
  Status values that indicate whether an auto-renewable subscription is subject to a price increase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/managing-price-increases-for-auto-renewable-subscriptions)*