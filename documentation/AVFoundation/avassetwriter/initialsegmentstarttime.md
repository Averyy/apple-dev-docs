# initialSegmentStartTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The start time of the initial segment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var initialSegmentStartTime: CMTime { get set }
```

```objc
@property (nonatomic) CMTime initialSegmentStartTime;
```

#### Discussion

This value is relevant only when the [`preferredOutputSegmentInterval`](./preferredoutputsegmentinterval.md) property value is positive numeric, in which case you must set a numeric time.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing
- [var delegate: (any AVAssetWriterDelegate)?](./delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](../avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](./preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var outputFileTypeProfile: AVFileTypeProfile?](./outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](./flushsegment%28%29.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/initialsegmentstarttime)*