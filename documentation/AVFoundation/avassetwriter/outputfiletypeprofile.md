# outputFileTypeProfile

**Framework**: AVFoundation  
**Kind**: property

A profile for the output file type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var outputFileTypeProfile: AVFileTypeProfile? { get set }
```

#### Discussion

The default value is `nil`, which indicates that the writer chooses an appropriate default profile for the output file type. If your app requires segment data that’s suitable for streaming, set the value to [`mpeg4AppleHLS`](avfiletypeprofile/mpeg4applehls.md) or [`mpeg4CMAFCompliant`](avfiletypeprofile/mpeg4cmafcompliant.md) to output CMAF-compliant [`mp4`](avfiletype/mp4.md) data.

You can’t change this value after writing starts.

## See Also

- [var delegate: (any AVAssetWriterDelegate)?](avassetwriter/delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](avassetwriter/preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var initialSegmentStartTime: CMTime](avassetwriter/initialsegmentstarttime.md)
  The start time of the initial segment.
- [func flushSegment()](avassetwriter/flushsegment.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/outputfiletypeprofile)*