# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time range within the asset to read.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timeRange: CMTimeRange { get set }
```

```objc
@property (nonatomic) CMTimeRange timeRange;
```

#### Discussion

The default value is a time range with a start time of [`zero`](../../CoreMedia/cmtime/zero.md) and a duration of [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md).

You can’t modify this value after reading starts.

## See Also

### Configuring reading
- [var status: AVAssetReader.Status](./status-swift.property.md)
  The status of reading sample buffers from the asset.
- [AVAssetReader.Status](./status-swift.enum.md)
  Values that represent the possible states of an asset reader.
- [var error: (any Error)?](./error.md)
  An error that describes the reason for a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/timerange)*