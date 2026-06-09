# AVPlannedVideoSegmentWritingRequest

**Framework**: AVFoundation  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVPlannedVideoSegmentWritingRequest
```

#### Overview

AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero.  The client’s writing work may be completed asynchronously.  If it completes successfully, it must call the `-finish` method on the request object.  If writing the segment fails, it must call the `-finishWithError:` method on the request object.

## Topics

### Inspecting the request
- [var frameCount: Int](avplannedvideosegmentwritingrequest/framecount.md)
### Creating resumable compression sessions
- [func createResumableCompressionSession(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: [String : any Sendable]?, sourceImageBufferAttributes: [String : any Sendable]?, outputHandler: (OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void) throws -> VTCompressionSession](avplannedvideosegmentwritingrequest/createresumablecompressionsession(width:height:codectype:encoderspecification:sourceimagebufferattributes:outputhandler:).md)
  Helper function to create a VTCompressionSession that restores the video encoder state persisted at the end of the previous segment.
### Creating resumable writer inputs
- [func makeResumableWriterInput(for: AVMediaType, outputSettings: [String : any Sendable]?, sourceFormatHint: CMFormatDescription?) throws -> AVAssetWriterInput](avplannedvideosegmentwritingrequest/makeresumablewriterinput(for:outputsettings:sourceformathint:).md)
  Helper function that returns a minimally configured AVAssetWriterInput object for writing the current segment.

## Relationships

### Inherits From
- [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAssetTrackPlan](avassettrackplan.md)
- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest)*