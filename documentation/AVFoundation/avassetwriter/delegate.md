# delegate

**Framework**: AVFoundation  
**Kind**: property

A delegate object that responds to asset-writing events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVAssetWriterDelegate)? { get set }
```

## See Also

- [protocol AVAssetWriterDelegate](avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](avassetwriter/preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var initialSegmentStartTime: CMTime](avassetwriter/initialsegmentstarttime.md)
  The start time of the initial segment.
- [var outputFileTypeProfile: AVFileTypeProfile?](avassetwriter/outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](avassetwriter/flushsegment.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/delegate)*