# AVAssetReader.Status.failed

**Framework**: AVFoundation  
**Kind**: case

The asset reader can no longer read samples from its asset because of an error.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case failed
```

#### Discussion

Query the asset reader’s [`error`](avassetreader/error.md) property to determine the reason for the failure.

## See Also

- [AVAssetReader.Status.unknown](avassetreader/status-swift.enum/unknown.md)
  The asset reader is in an unknown state.
- [AVAssetReader.Status.reading](avassetreader/status-swift.enum/reading.md)
  The asset reader is successfully reading samples from its asset.
- [AVAssetReader.Status.completed](avassetreader/status-swift.enum/completed.md)
  The asset reader completes reading all samples within its specified time range.
- [AVAssetReader.Status.cancelled](avassetreader/status-swift.enum/cancelled.md)
  The asset reader can no longer read samples because you canceled reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum/failed)*