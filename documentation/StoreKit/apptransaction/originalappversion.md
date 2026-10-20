# originalAppVersion

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The app version that the customer originally purchased from the App Store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let originalAppVersion: String
```

## Mentions

- [Supporting business model changes by using the app transaction](../supporting-business-model-changes-by-using-the-app-transaction.md)

#### Discussion

Use this value to determine which app version the customer first purchased or downloaded. This value is comparable to the [`appVersion`](./appversion.md) value.

The [`originalAppVersion`](./originalappversion.md) remains constant and doesn’t change when the customer upgrades the app. The string value contains the original value of the [`CFBundleShortVersionString`](../../BundleResources/information-property-list/cfbundleshortversionstring.md) for apps running in macOS, and the original value of the [`CFBundleVersion`](../../BundleResources/information-property-list/cfbundleversion.md) for apps running on all other platforms.

In the sandbox testing environment, the [`originalAppVersion`](./originalappversion.md) value is always `1.0`.

For more information about using the [`originalAppVersion`](./originalappversion.md), see [Supporting business model changes by using the app transaction](../supporting-business-model-changes-by-using-the-app-transaction.md).

## See Also

### Getting app and version information
- [let bundleID: String](./bundleid.md)
  The bundle identifier that the app transaction applies to.
- [let appVersion: String](./appversion.md)
  The app version that the app transaction applies to.
- [let appID: UInt64?](./appid.md)
  The unique identifier the App Store uses to identify the app.
- [let appVersionID: UInt64?](./appversionid.md)
  The number that the App Store uses to uniquely identify the version of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/originalappversion)*