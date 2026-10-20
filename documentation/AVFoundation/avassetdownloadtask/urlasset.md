# urlAsset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset that this task downloads.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var urlAsset: AVURLAsset { get }
```

```objc
@property (nonatomic, readonly) AVURLAsset * URLAsset;
```

## See Also

### Accessing task information
- [var loadedTimeRanges: [NSValue]](./loadedtimeranges.md)
  The time ranges of the downloaded media that are ready for playback.
- [var options: [String : Any]?](./options.md)
  The configuration options for the task.
- [var destinationURL: URL](./destinationurl.md)
  The local file URL to where the task downloads the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/urlasset)*