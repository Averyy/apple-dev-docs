# AVAggregateAssetDownloadTask

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A task that downloads multiple media selections for an asset.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use assetDownloadTaskWithConfiguration: instead

## Declaration

```swift
class AVAggregateAssetDownloadTask
```

```objc
@interface AVAggregateAssetDownloadTask : NSURLSessionTask
```

## Topics

### Accessing the asset
- [var urlAsset: AVURLAsset](./avaggregateassetdownloadtask/urlasset.md)
  The asset the parent task downloads.

## Relationships

### Inherits From
- [URLSessionTask](../Foundation/urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [ProgressReporting](../Foundation/progressreporting.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset downloading
- [Using AVFoundation to play and persist HTTP live streams](./using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadURLSession](./avassetdownloadurlsession.md)
  A URL session that creates and manages asset download tasks.
- [class AVAssetDownloadTask](./avassetdownloadtask.md)
  A URL session task that downloads a remote asset to the device for offline playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaggregateassetdownloadtask)*