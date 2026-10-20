# destinationURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The local file URL to where the task downloads the asset.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the URL property of URLAsset instead

## Declaration

```swift
var destinationURL: URL { get }
```

```objc
@property (nonatomic, readonly) NSURL * destinationURL;
```

## See Also

### Accessing task information
- [var urlAsset: AVURLAsset](./urlasset.md)
  The asset that this task downloads.
- [var loadedTimeRanges: [NSValue]](./loadedtimeranges.md)
  The time ranges of the downloaded media that are ready for playback.
- [var options: [String : Any]?](./options.md)
  The configuration options for the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/destinationurl)*