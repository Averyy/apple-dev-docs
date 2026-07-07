# appID

**Framework**: StoreKit  
**Kind**: property

The unique identifier the App Store uses to identify the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let appID: UInt64?
```

#### Discussion

The App Store assigns this value. This value is the app’s Apple ID in App Store Connect. In the [`sandbox`](appstore/environment/sandbox.md) and [`xcode`](appstore/environment/xcode.md) environments, this value is `nil`.

## See Also

- [let bundleID: String](apptransaction/bundleid.md)
  The bundle identifier that the app transaction applies to.
- [let appVersion: String](apptransaction/appversion.md)
  The app version that the app transaction applies to.
- [let originalAppVersion: String](apptransaction/originalappversion.md)
  The app version that the customer originally purchased from the App Store.
- [let appVersionID: UInt64?](apptransaction/appversionid.md)
  The number that the App Store uses to uniquely identify the version of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/appid)*