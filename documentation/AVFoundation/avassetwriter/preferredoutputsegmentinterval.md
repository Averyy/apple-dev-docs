# preferredOutputSegmentInterval

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The default value is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid), which indicates that the asset writer chooses an appropriate default value. You may also set a positive numeric or [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite) time. When the value is [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite), each call you make to [`flushSegment()`](avassetwriter/flushsegment().md) outputs a segment data.

You can’t change this value after writing starts.

## See Also

- [var delegate: (any AVAssetWriterDelegate)?](avassetwriter/delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var initialSegmentStartTime: CMTime](avassetwriter/initialsegmentstarttime.md)
  The start time of the initial segment.
- [var outputFileTypeProfile: AVFileTypeProfile?](avassetwriter/outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](avassetwriter/flushsegment.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/preferredoutputsegmentinterval)*