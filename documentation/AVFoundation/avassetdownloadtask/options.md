# options

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The configuration options for the task.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetDownloadConfiguration instead

## Declaration

```swift
var options: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * options;
```

## See Also

### Accessing task information
- [var urlAsset: AVURLAsset](./urlasset.md)
  The asset that this task downloads.
- [var loadedTimeRanges: [NSValue]](./loadedtimeranges.md)
  The time ranges of the downloaded media that are ready for playback.
- [var destinationURL: URL](./destinationurl.md)
  The local file URL to where the task downloads the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/options)*