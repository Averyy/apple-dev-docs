# outputFileTypeProfile

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) AVFileTypeProfile outputFileTypeProfile;
```

#### Discussion

The default value is `nil`, which indicates that the writer chooses an appropriate default profile for the output file type. If your app requires segment data that’s suitable for streaming, set the value to [`mpeg4AppleHLS`](../avfiletypeprofile/mpeg4applehls.md) or [`mpeg4CMAFCompliant`](../avfiletypeprofile/mpeg4cmafcompliant.md) to output CMAF-compliant [`mp4`](../avfiletype/mp4.md) data.

You can’t change this value after writing starts.

## See Also

### Configuring segment writing
- [var delegate: (any AVAssetWriterDelegate)?](./delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](../avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](./preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var initialSegmentStartTime: CMTime](./initialsegmentstarttime.md)
  The start time of the initial segment.
- [func flushSegment()](./flushsegment%28%29.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/outputfiletypeprofile)*