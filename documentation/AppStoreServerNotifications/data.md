# data

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The payload data that contains app metadata and the signed renewal and transaction information.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
object data
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)
- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

#### Discussion

The `data` object is part of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). It’s present in the payload for [`notificationType`](notificationtype.md) values related to in-app purchases, except for the `RENEWAL_EXTENSION` notification type with a `SUMMARY` [`subtype`](subtype.md), and the `EXTERNAL_PURCHASE_TOKEN` notification type.

Use the notification type along with the transaction and subscription renewal information in the `data` object to update a user’s service or present promotional offers according to your business logic.

## Topics

### App metadata and environment
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type bundleVersion](bundleversion.md)
  The version of the build that identifies an iteration of the bundle.
- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type status](status.md)
  The status of an auto-renewable subscription at the time the App Store signs the notification.
### JWS transaction and renewal info
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
### Consumption request info
- [type consumptionRequestReason](consumptionrequestreason.md)
  The customer-provided reason for a refund request.

## See Also

- [object summary](summary.md)
  The payload data for a subscription-renewal-date extension notification.
- [object appData](appdata.md)
  The object that contains the app metadata and signed app transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/data)*