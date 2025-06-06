# status

**Framework**: AVFoundation  
**Kind**: property

The status of reading sample buffers from the asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var status: AVAssetReader.Status { get }
```

#### Discussion

Check the value of this property when the [`copyNextSampleBuffer()`](avassetreaderoutput/copynextsamplebuffer().md) method on [`AVAssetReaderOutput`](avassetreaderoutput.md) returns `nil` to determine why the output can’t read more data.

This property is thread safe.

## See Also

- [var timeRange: CMTimeRange](avassetreader/timerange.md)
  The time range within the asset to read.
- [AVAssetReader.Status](avassetreader/status-swift.enum.md)
  Values that represent the possible states of an asset reader.
- [var error: (any Error)?](avassetreader/error.md)
  An error that describes the reason for a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.property)*