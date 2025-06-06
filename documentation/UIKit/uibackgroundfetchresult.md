# UIBackgroundFetchResult

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the result of a background fetch operation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum UIBackgroundFetchResult
```

## Topics

### Constants
- [UIBackgroundFetchResult.newData](uibackgroundfetchresult/newdata.md)
  New data was successfully downloaded.
- [UIBackgroundFetchResult.noData](uibackgroundfetchresult/nodata.md)
  There was no new data to download.
- [UIBackgroundFetchResult.failed](uibackgroundfetchresult/failed.md)
  An attempt to download data was made but that attempt failed.
### Initializers
- [init?(rawValue: UInt)](uibackgroundfetchresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func application(UIApplication, handleEventsForBackgroundURLSession: String, completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleeventsforbackgroundurlsession:completionhandler:).md)
  Tells the delegate that events related to a URL session are waiting to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult)*