# preferredOutputSegmentInterval

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The interval of output segments that you prefer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var preferredOutputSegmentInterval: CMTime { get set }
```

```objc
@property (nonatomic) CMTime preferredOutputSegmentInterval;
```

#### Discussion

The default value is [`invalid`](../../CoreMedia/cmtime/invalid.md), which indicates that the asset writer chooses an appropriate default value. You may also set a positive numeric or [`indefinite`](../../CoreMedia/cmtime/indefinite.md) time. When the value is [`indefinite`](../../CoreMedia/cmtime/indefinite.md), each call you make to [`flushSegment()`](./flushsegment%28%29.md) outputs a segment data.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing
- [var delegate: (any AVAssetWriterDelegate)?](./delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](../avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var initialSegmentStartTime: CMTime](./initialsegmentstarttime.md)
  The start time of the initial segment.
- [var outputFileTypeProfile: AVFileTypeProfile?](./outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](./flushsegment%28%29.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/preferredoutputsegmentinterval)*