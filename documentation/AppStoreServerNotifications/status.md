# status

**Framework**: App Store Server Notifications  
**Kind**: typealias

The status of an auto-renewable subscription at the time the App Store signs the notification.

**Availability**:
- App Store Server Notifications 2.8+

## Declaration

```swift
int32 status
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

This status value is current as of the `signedDate` in the decoded payload, [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md).

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type bundleVersion](bundleversion.md)
  The version of the build that identifies an iteration of the bundle.
- [type environment](environment.md)
  The server environment, either sandbox or production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/status)*