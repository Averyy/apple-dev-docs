# AVPlannedVideoSegmentWritingRequest

**Framework**: AVFoundation  
**Kind**: class

AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.

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

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero. The client’s writing work may be completed asynchronously. If it completes successfully, it must call the `-finish` method on the request object. If writing the segment fails, it must call the `-finishWithError:` method on the request object.

## Topics

### Inspecting the request
- [var frameCount: Int](avplannedvideosegmentwritingrequest/framecount.md)
  The number of frames in this planned video segment. This is provided for convenience, and is the same value that was configured for the segment in AVPlannedVideoSegmentConfiguration.
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
  AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
- [class AVAssetVideoTrackPlan](avassetvideotrackplan.md)
  AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.
- [class AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md)
  AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.
- [class AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md)
  AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner.
- [class AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)
  AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest)*