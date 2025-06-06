# AppStore.Platform

**Framework**: StoreKit  
**Kind**: struct

Values that represent Apple platforms.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct Platform
```

#### Discussion

You choose a platform for your app when you add the new app in App Store Connect. For more information, see [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app/).

The platform values in `AppStore.Platform` are the same as those in App Store Connect.

## Topics

### Getting platform values
- [static let iOS: AppStore.Platform](appstore/platform/ios.md)
  A value that indicates the iOS platform.
- [static let macOS: AppStore.Platform](appstore/platform/macos.md)
  A value that indicates the macOS platform.
- [static let tvOS: AppStore.Platform](appstore/platform/tvos.md)
  A value that indicates the tvOS platform.
- [static let visionOS: AppStore.Platform](appstore/platform/visionos.md)
  A value that indicates the visionOS platform.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let originalPlatform: AppStore.Platform](apptransaction/originalplatform.md)
  The platform on which the customer originally purchased the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/platform)*