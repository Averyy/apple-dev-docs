# loadedTimeRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time ranges of the downloaded media that are ready for playback.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use NSURLSessionTask.progress instead

## Declaration

```swift
var loadedTimeRanges: [NSValue] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * loadedTimeRanges;
```

## Discussion

The time ranges that this property provides may be discontinuous.

## See Also

### Accessing task information
- [var urlAsset: AVURLAsset](./urlasset.md)
  The asset that this task downloads.
- [var options: [String : Any]?](./options.md)
  The configuration options for the task.
- [var destinationURL: URL](./destinationurl.md)
  The local file URL to where the task downloads the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/loadedtimeranges)*