# AVAssetReader.Status

**Framework**: AVFoundation  
**Kind**: enum

Values that represent the possible states of an asset reader.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Status
```

#### Overview

You determine an asset reader’s status using its [`status`](avassetreader/status-swift.property.md) property.

## Topics

### Status Values
- [AVAssetReader.Status.unknown](avassetreader/status-swift.enum/unknown.md)
  The asset reader is in an unknown state.
- [AVAssetReader.Status.reading](avassetreader/status-swift.enum/reading.md)
  The asset reader is successfully reading samples from its asset.
- [AVAssetReader.Status.completed](avassetreader/status-swift.enum/completed.md)
  The asset reader completes reading all samples within its specified time range.
- [AVAssetReader.Status.failed](avassetreader/status-swift.enum/failed.md)
  The asset reader can no longer read samples from its asset because of an error.
- [AVAssetReader.Status.cancelled](avassetreader/status-swift.enum/cancelled.md)
  The asset reader can no longer read samples because you canceled reading.
### Initializers
- [init?(rawValue: Int)](avassetreader/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var timeRange: CMTimeRange](avassetreader/timerange.md)
  The time range within the asset to read.
- [var status: AVAssetReader.Status](avassetreader/status-swift.property.md)
  The status of reading sample buffers from the asset.
- [var error: (any Error)?](avassetreader/error.md)
  An error that describes the reason for a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum)*