# originalApplicationVersion

**Framework**: App Store Server API  
**Kind**: typealias

The app version that the customer originally purchased from the App Store.

**Availability**:
- App Store Server API 1.17+

## Declaration

```swift
string originalApplicationVersion
```

#### Discussion

Use this value to determine which app version the customer first purchased or downloaded. This value remains constant and doesn’t change when the customer upgrades the app.

The string value contains the original value of the [`CFBundleShortVersionString`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString) for apps running in macOS, and the original value of the [`CFBundleVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleVersion) for apps running on all other platforms.

In the sandbox testing environment, the `originalApplicationVersion` value is always 1.0.

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type originalPlatform](originalplatform.md)
  The platform on which a customer originally purchases an app.
- [type preorderDate](preorderdate.md)
  The date a customer places an order for the app before it’s available in the App Store, expressed in UNIX time, in milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/originalapplicationversion)*