# loadedTimeRanges

**Framework**: AVFoundation  
**Kind**: property

The time ranges of the downloaded media that are ready for playback.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var loadedTimeRanges: [NSValue] { get }
```

#### Discussion

The time ranges that this property provides may be discontinuous.

## See Also

- [var urlAsset: AVURLAsset](avassetdownloadtask/urlasset.md)
  The asset that this task downloads.
- [var options: [String : Any]?](avassetdownloadtask/options.md)
  The configuration options for the task.
- [var destinationURL: URL](avassetdownloadtask/destinationurl.md)
  The local file URL to where the task downloads the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/loadedtimeranges)*