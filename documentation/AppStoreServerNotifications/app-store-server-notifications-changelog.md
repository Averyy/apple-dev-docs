# App Store Server Notifications changelog

**Framework**: App Store Server Notifications

Learn about changes to the App Store Server Notifications service.

#### Overview

App Store Server Notifications has two versions of notifications. Version 1 notifications and the [`App Store Server Notifications V1`](app-store-server-notifications-v1.md) endpoint are deprecated. Instead, implement the [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) endpoint on your server to receive version 2 notifications.

To set up your server to receive notifications, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md). Use this changelog to learn about feature updates, version information, deprecations, and removals for App Store Server Notifications.

##### December 10 2025

- Added the [`revocationType`](revocationtype.md) and [`revocationPercentage`](revocationpercentage.md) fields to the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md).
- Added the [`advancedCommercePriceIncreaseInfo`](advancedcommercepriceincreaseinfo.md) object, and [`advancedCommercePriceIncreaseInfoDependentSKU`](advancedcommercepriceincreaseinfodependentsku.md), [`advancedCommercePriceIncreaseInfoStatus`](advancedcommercepriceincreaseinfostatus.md), [`advancedCommercePriceIncreaseInfoPrice`](advancedcommercepriceincreaseinfoprice.md), fields to the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md).

##### November 4 2025

- Updated the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) to include the new payload object, [`appData`](appdata.md).
- Added the notification type `RESCIND_CONSENT` to [`notificationType`](notificationtype.md).

##### October 29 2025

- Added the `ONE_TIME` value to [`offerDiscountType`](offerdiscounttype.md) to indicate In-App Purchase offer codes.

##### June 26 2025

- Added the `ACTIVE_TOKEN_REMINDER` and `CREATED` values to [`subtype`](subtype.md), which can appear in notifications with an `EXTERNAL_PURCHASE_TOKEN` [`notificationType`](notificationtype.md).
- Updated [`externalPurchaseToken`](externalpurchasetoken.md) to include the new fields [`tokenType`](tokentype.md) and [`tokenExpirationDate`](tokenexpirationdate.md).

##### May 27 2025

- The `ONE_TIME_CHARGE` [`notificationType`](notificationtype.md) is now available in the production environment.

##### March 24 2025

- Added the notification types `METADATA_UPDATE` and `MIGRATE` to [`notificationType`](notificationtype.md).
- Added the [`previousOriginalTransactionId`](previousoriginaltransactionid.md) field to the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md).

##### February 21 2025

- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) and [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) to include the new [`appTransactionId`](apptransactionid.md) and [`offerPeriod`](offerperiod.md) fields.
- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) to include the [`appAccountToken`](appaccounttoken.md) field.

##### January 17 2025

- Added support for the [`Advanced Commerce API`](https://developer.apple.com/documentation/AdvancedCommerceAPI).

##### July 8 2024

- Updated the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) to include the new field [`eligibleWinBackOfferIds`](eligiblewinbackofferids.md).
- Added the win-back offer type to [`offerType`](offertype.md).

##### June 10 2024

- Added the notification type `ONE_TIME_CHARGE` to [`notificationType`](notificationtype.md). This notification type is currently available only in the sandbox environment.
- Added the fields [`renewalPrice`](https://developer.apple.com/documentation/AppStoreServerAPI/renewalPrice), [`currency`](currency.md), and [`offerDiscountType`](offerdiscounttype.md) to the [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md).

##### April 11 2024

- Added the [`consumptionRequestReason`](consumptionrequestreason.md) to the [`data`](data.md) object.
- The `CONSUMPTION_REQUEST` [`notificationType`](notificationtype.md) added notifications for refund requests for auto-renewable subscriptions.

##### March 12 2024

- The type of the [`price`](price.md) field changed from `int32` to `int64`.

##### February 29 2024

- Added a new [`notificationType`](notificationtype.md):  `EXTERNAL_PURCHASE_TOKEN` and a [`subtype`](subtype.md): `UNREPORTED`.
- Updated the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) to include the new payload object, [`externalPurchaseToken`](externalpurchasetoken.md).
- Added the types [`externalPurchaseId`](externalpurchaseid.md) and [`tokenCreationDate`](tokencreationdate.md).

##### January 23 2024

- Changed the notification type the App Store server sends when a customer redeems a subscription offer for an inactive subscription to the `SUBSCRIBED` [`notificationType`](notificationtype.md). The App Store server only sends the `OFFER_REDEEMED` notification type when customers redeem an offer on an active subscription.

##### October 26 2023

- Added new properties in the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object: [`price`](price.md), [`currency`](currency.md), and [`offerDiscountType`](offerdiscounttype.md).

##### June 5 2023

- Added a new version 2 [`notificationType`](notificationtype.md), `REFUND_REVERSED`.
- Added the following new fields in the transaction decoded payload, [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md): [`storefront`](storefront.md), [`storefrontId`](storefrontid.md), and [`transactionReason`](transactionreason.md).
- Added the `renewalDate` field in the renewal info decoded payload, [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md).
- Added a subscription [`status`](status.md) field in the [`data`](data.md) object of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md).
- The [`responseBodyV1`](responsebodyv1.md) now includes a `deprecation` field.

- The [`App Store Server Notifications V1`](app-store-server-notifications-v1.md) endpoint and version 1 notifications are deprecated. Implement the [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) endpoint on your server to receive version 2 notifications instead.

##### January 30 2023

- Added a new notification type for App Store Server Notifications 2 that consists of the [`notificationType`](notificationtype.md) value `RENEWAL_EXTENSION` and [`subtype`](subtype.md) values of `SUMMARY` and `FAILURE`. This notification provides information when you extend the subscription renewal date for all active subscribers, based on a product identifier. For more information, see [`Extend Subscription Renewal Dates for All Active Subscribers`](https://developer.apple.com/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).
- Updated the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) to include the new [`summary`](summary.md) object, which appears in the payload for a `RENEWAL_EXTENSION` notification with a `SUMMARY` [`subtype`](subtype.md).

##### November 7 2022

- Added the `PRODUCT_NOT_FOR_SALE` [`subtype`](subtype.md) for the `EXPIRED` [`notificationType`](notificationtype.md).

##### June 6 2022

- App Store Server Notifications 2 supports sending a `TEST` notification. For more information, see [`notificationType`](notificationtype.md), and the endpoints [`Request a Test Notification`](https://developer.apple.com/documentation/AppStoreServerAPI/Request-a-Test-Notification) and [`Get Test Notification Status`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Test-Notification-Status) in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).

##### May 12 2022

- In App Store Server Notifications 2, the notification subtype `ACCEPTED` is now sent when the App Store notifies the customer of an auto-renewable subscription price increase that doesn’t require customer consent. This notification subtype is available only in version 2 notifications. For more information, see [`subtype`](subtype.md).

##### October 21 2021 Version 2

- [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) is available, and version 1 is still supported. For information about the notifications sent in version 2, see [`notificationType`](notificationtype.md), `substate`, and [`responseBodyV2`](responsebodyv2.md).
- For information about the notifications sent in version 1, see [`notification_type`](notification_type.md) and [`responseBodyV1`](responsebodyv1.md) (previously named `responseBody`).

##### March 10 2021

- In [`App Store Server Notifications Version 1`](app-store-server-notifications-version-1.md), the following notification type and top-level objects are deprecated and removed: `RENEWAL,latest_receipt`, `latest_receipt_info`, `latest_expired_receipt`, and `latest_expired_receipt_info`. For more information, see [`responseBodyV1`](responsebodyv1.md) and [`notification_type`](notification_type.md).

##### November 21 2019 Version 1

- App Store Server Notifications is available.

## See Also

- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md)
  Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)
  Implement server-side code to receive and parse notification posts.
- [Responding to App Store Server Notifications](responding-to-app-store-server-notifications.md)
  Send HTTP status codes to indicate the success of a notification post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-changelog)*