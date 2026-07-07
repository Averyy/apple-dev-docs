# appVersionID

**Framework**: StoreKit  
**Kind**: property

The number that the App Store uses to uniquely identify the version of the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let appVersionID: UInt64?
```

#### Discussion

The App Store assigns this value. In the [`sandbox`](appstore/environment/sandbox.md) and [`xcode`](appstore/environment/xcode.md) environments, this value is `nil`.

## See Also

- [let bundleID: String](apptransaction/bundleid.md)
  The bundle identifier that the app transaction applies to.
- [let appVersion: String](apptransaction/appversion.md)
  The app version that the app transaction applies to.
- [let originalAppVersion: String](apptransaction/originalappversion.md)
  The app version that the customer originally purchased from the App Store.
- [let appID: UInt64?](apptransaction/appid.md)
  The unique identifier the App Store uses to identify the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/appversionid)*