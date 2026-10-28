# bundleID

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The bundle identifier that the app transaction applies to.

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
let bundleID: String
```

## Discussion

The [`bundleID`](./bundleid.md) is the bundle identifier string that you entered in Xcode. For more information, see [What is a bundle ID?](https://help.apple.com/xcode/mac/current/#/deve70ea917b)

## See Also

### Getting app and version information
- [let appVersion: String](./appversion.md)
  The app version that the app transaction applies to.
- [let originalAppVersion: String](./originalappversion.md)
  The app version that the customer originally purchased from the App Store.
- [let appID: UInt64?](./appid.md)
  The unique identifier the App Store uses to identify the app.
- [let appVersionID: UInt64?](./appversionid.md)
  The number that the App Store uses to uniquely identify the version of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/bundleid)*