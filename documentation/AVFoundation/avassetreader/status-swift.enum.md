# AVAssetReader.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Values that represent the possible states of an asset reader.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Status
```

```c
enum AVAssetReaderStatus : NSInteger;
```

## Overview

You determine an asset reader’s status using its [`status`](./status-swift.property.md) property.

## Topics

### Status values
- [AVAssetReader.Status.unknown](./status-swift.enum/unknown.md)
  The asset reader is in an unknown state.
- [AVAssetReader.Status.reading](./status-swift.enum/reading.md)
  The asset reader is successfully reading samples from its asset.
- [AVAssetReader.Status.completed](./status-swift.enum/completed.md)
  The asset reader completes reading all samples within its specified time range.
- [AVAssetReader.Status.failed](./status-swift.enum/failed.md)
  The asset reader can no longer read samples from its asset because of an error.
- [AVAssetReader.Status.cancelled](./status-swift.enum/cancelled.md)
  The asset reader can no longer read samples because you canceled reading.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring reading
- [var timeRange: CMTimeRange](./timerange.md)
  The time range within the asset to read.
- [var status: AVAssetReader.Status](./status-swift.property.md)
  The status of reading sample buffers from the asset.
- [var error: (any Error)?](./error.md)
  An error that describes the reason for a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.enum)*