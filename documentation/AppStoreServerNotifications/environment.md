# environment

**Framework**: App Store Server Notifications  
**Kind**: typealias

The server environment, either sandbox or production.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string environment
```

#### Discussion

You receive notifications in the sandbox environment when you opt in to receive notifications in the sandbox environment and test your app in the sandbox environment. TestFlight also uses the sandbox environment to send notifications. To opt in to receive notifications, see [`Enter a URL for App Store Server Notifications`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev0067a330b). For more information about testing, see [`Testing at all stages of development with Xcode and the sandbox`](https://developer.apple.com/documentation/StoreKit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox), and [`Beta Testing Made Simple with TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/).

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type bundleVersion](bundleversion.md)
  The version of the build that identifies an iteration of the bundle.
- [type status](status.md)
  The status of an auto-renewable subscription at the time the App Store signs the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/environment)*