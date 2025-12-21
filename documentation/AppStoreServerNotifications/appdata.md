# appData

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The object that contains the app metadata and signed app transaction information.

**Availability**:
- App Store Server Notifications 2.19+

## Declaration

```swift
object appData
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

The `appData` object is part of the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md). This object is present in the payload when the [`notificationType`](notificationtype.md) is `RESCIND_CONSENT`.

## Topics

### JWS app transaction information
- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

## See Also

- [object summary](summary.md)
  The payload data for a subscription-renewal-date extension notification.
- [object data](data.md)
  The payload data that contains app metadata and the signed renewal and transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/appdata)*