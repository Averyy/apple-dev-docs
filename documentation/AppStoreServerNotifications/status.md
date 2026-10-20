# status

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The status of an auto-renewable subscription at the time the App Store signs the notification.

**Availability**:
- App Store Server Notifications 2.8+

## Declaration

```
int32 status
```

## Possible Values

- `1`: The auto-renewable subscription is active.
- `2`: The auto-renewable subscription is expired.
- `3`: The auto-renewable subscription is in a billing retry period.
- `4`: The auto-renewable subscription is in a Billing Grace Period.
- `5`: The auto-renewable subscription is revoked. The App Store refunded the transaction or revoked it from Family Sharing.

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

#### Discussion

This status value is current as of the `signedDate` in the decoded payload, [`responseBodyV2DecodedPayload`](./responsebodyv2decodedpayload.md).

## See Also

### App metadata and environment
- [type appAppleId](./appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](./bundleid.md)
  The bundle identifier of an app.
- [type bundleVersion](./bundleversion.md)
  The version of the build that identifies an iteration of the bundle.
- [type environment](./environment.md)
  The server environment, either sandbox or production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/status)*