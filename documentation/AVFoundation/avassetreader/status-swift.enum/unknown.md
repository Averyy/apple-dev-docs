# AVAssetReader.Status.unknown

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The asset reader is in an unknown state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case unknown
```

```c
AVAssetReaderStatusUnknown
```

## See Also

### Status values
- [AVAssetReader.Status.reading](./reading.md)
  The asset reader is successfully reading samples from its asset.
- [AVAssetReader.Status.completed](./completed.md)
  The asset reader completes reading all samples within its specified time range.
- [AVAssetReader.Status.failed](./failed.md)
  The asset reader can no longer read samples from its asset because of an error.
- [AVAssetReader.Status.cancelled](./cancelled.md)
  The asset reader can no longer read samples because you canceled reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum/unknown)*