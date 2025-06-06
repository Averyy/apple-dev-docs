# error

**Framework**: AVFoundation  
**Kind**: property

An error that describes the reason for a failure.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The value is `nil` if the asset reader’s status isn’t [`AVAssetReader.Status.failed`](avassetreader/status-swift.enum/failed.md).

This property is thread safe.

## See Also

- [var timeRange: CMTimeRange](avassetreader/timerange.md)
  The time range within the asset to read.
- [var status: AVAssetReader.Status](avassetreader/status-swift.property.md)
  The status of reading sample buffers from the asset.
- [AVAssetReader.Status](avassetreader/status-swift.enum.md)
  Values that represent the possible states of an asset reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/error)*