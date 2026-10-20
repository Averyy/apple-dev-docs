# UIBackgroundFetchResult

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the result of a background fetch operation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum UIBackgroundFetchResult
```

```c
enum UIBackgroundFetchResult : NSUInteger;
```

## Topics

### Constants
- [UIBackgroundFetchResult.newData](./uibackgroundfetchresult/newdata.md)
  New data was successfully downloaded.
- [UIBackgroundFetchResult.noData](./uibackgroundfetchresult/nodata.md)
  There was no new data to download.
- [UIBackgroundFetchResult.failed](./uibackgroundfetchresult/failed.md)
  An attempt to download data was made but that attempt failed.
### Initializers
- [init?(rawValue: UInt)](./uibackgroundfetchresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Downloading data in the background
- [func application(UIApplication, handleEventsForBackgroundURLSession: String, completionHandler: () -> Void)](./uiapplicationdelegate/application%28_,handleeventsforbackgroundurlsession,completionhandler%29.md)
  Tells the delegate that events related to a URL session are waiting to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult)*