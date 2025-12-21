# responseBodyV2DecodedPayload

**Framework**: App Store Server Notifications  
**Kind**: dictionary

A decoded payload that contains the version 2 notification data.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
object responseBodyV2DecodedPayload
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

The `responseBodyV2DecodedPayload` is the Base64URL-decoded notification information from the JWS payload portion of the [`signedPayload`](signedpayload.md). Use the [`notificationType`](notificationtype.md) and [`subtype`](subtype.md) to understand the event that led to this notification.

The payload can contain only one of the following four fields:

- A [`data`](data.md) object, which contains details including the environment, the app metadata, and the signed transaction and subscription renewal information.
- An [`appData`](appdata.md) object, which contains details including the environment, the app metadata, and the signed app transaction information.
- A [`summary`](summary.md) object, which contains information only when the notification is a `RENEWAL_EXTENSION` with a `SUMMARY` subtype. For more information, see [`Extend Subscription Renewal Dates for All Active Subscribers`](https://developer.apple.com/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers).
- An [`externalPurchaseToken`](externalpurchasetoken.md) object, which contains an external purchase token only when the notification is `EXTERNAL_PURCHASE_TOKEN`. For more information about this notification, see [`externalPurchaseToken`](externalpurchasetoken.md).

## Topics

### Response objects for in-app purchases
- [object summary](summary.md)
  The payload data for a subscription-renewal-date extension notification.
- [object data](data.md)
  The payload data that contains app metadata and the signed renewal and transaction information.
- [object appData](appdata.md)
  The object that contains the app metadata and signed app transaction information.
### Response object for an external purchase
- [object externalPurchaseToken](externalpurchasetoken.md)
  The payload data that contains an external purchase token.
### Response types
- [type notificationType](notificationtype.md)
  The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.
- [type version](version.md)
  A string that indicates the notification’s App Store Server Notifications version number.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.
- [type notificationUUID](notificationuuid.md)
  A unique identifier for the notification.
### JWS header and payload data types
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature header containing transaction or renewal information.
- [Transaction data types](transaction-data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.

## See Also

- [App Store Server Notifications V2](app-store-server-notifications-v2.md)
  Specify your secure server’s URL in App Store Connect to receive version 2 notifications.
- [object responseBodyV2](responsebodyv2.md)
  The response body the App Store sends in a version 2 server notification.
- [type notificationType](notificationtype.md)
  The type that describes the In-App Purchase or external purchase event for which the App Store sends the version 2 notification.
- [type subtype](subtype.md)
  A string that provides details about select notification types in version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2decodedpayload)*