# status

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAssetReaderStatus status;
```

#### Discussion

Check the value of this property when the [`copyNextSampleBuffer()`](../avassetreaderoutput/copynextsamplebuffer%28%29.md) method on [`AVAssetReaderOutput`](../avassetreaderoutput.md) returns `nil` to determine why the output can’t read more data.

This property is thread safe.

## See Also

### Configuring reading
- [var timeRange: CMTimeRange](./timerange.md)
  The time range within the asset to read.
- [AVAssetReader.Status](./status-swift.enum.md)
  Values that represent the possible states of an asset reader.
- [var error: (any Error)?](./error.md)
  An error that describes the reason for a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/status-swift.property)*