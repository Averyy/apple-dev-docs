# AVAssetWritingPlanner

**Framework**: AVFoundation  
**Kind**: class

AVAssetWritingPlanner orchestrates incremental writing of media files.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AVAssetWritingPlanner
```

#### Overview

AVAssetWritingPlanner orchestrates an incremental and resumable asset file writing session. It keeps track of the progress of the incremental segments, and can resume the writing from the last checkpoint. This is NOT intended for any real time applications. Also, not all tracks can be written incrementally. The workflow is as follows:

1. The client creates the planner with a unique directoryForTemporaryFiles.
2. The client tells the planner which tracks are to be written incrementally by calling the “planTrack:withSegmentsGeneratedBy:” method, providing a callback block that writes one segment per block invocation.
3. The client kicks off the incremental writing session by calling the “executePlanWithCompletionHandler” method.
4. The planner will call the writingSegmentCallbackBlock to ask the client to write one incremental segment of one track at a time. The client code should write one incremental segment according to the “AVPlannedSegmentWritingRequest” object passed in to the callback block. Clients must call “finish” or “finishWithError” or “finishWithClientState” or “cancel” methods on the request object when it finishes the segment successfully, or encountered an error, or wants to cancel the writing of the segment.
5. At the end of the writing, after all incremental segments are finished, the planner calls the completionHandler. The client can use the “assemblyComposition” object passed in to the completionHandler to assemble the incremental segments into full tracks and export it to a final output file. The completionHandler will also be called when there is any irrecoverable error.
6. The client is responsible for cleaning all files in the directoryForTemporaryFiles after the incremental session is done and the final output file is written.

AVAssetWritingPlanner is able to recognize when a plan-in-progress matching the plan was already saved at directoryForTemporaryFiles, presumably by a previous invocation of the client, and possibly aborted due to that client being terminated abruptly, and will assist by resuming the plan at the first step that wasn’t previously completed.

## Topics

### Creating a planner
- [convenience init(directoryForTemporaryFiles: URL) throws](avassetwritingplanner/init(directoryfortemporaryfiles:).md)
  Creates an instance of AVAssetWritingPlanner given a unique file directory to host all incremental segment files and other intermediate files.
### Planning tracks
- [func plan(AVAssetTrackPlan, segmentHandler: (AVPlannedSegmentWritingRequest) async throws -> AVAssetWritingPlanner.SegmentResult)](avassetwritingplanner/plan(_:segmenthandler:).md)
  Adds a track plan with manual segment completion control.
### Executing the plan
- [func executePlan() async throws -> AVComposition](avassetwritingplanner/executeplan.md)
  Starts the incremental segment writing.
### Getting segment boundary guidance
- [static func segmentBoundaryGuidelinesForVideo(codecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]) -> AVAssetWritingPlanner.SegmentBoundaryGuidelines](avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:).md)
  Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.
- [class func segmentBoundaryRecommendations(forVideoTrack: AVAssetTrack, minimumSegmentDuration: CMTime, minimumSegmentFrameCount: Int) -> [AVPlannedVideoSegmentConfiguration]](avassetwritingplanner/segmentboundaryrecommendations(forvideotrack:minimumsegmentduration:minimumsegmentframecount:).md)
  Returns segment boundary recommendations for a given source video asset track.
### Getting progress
- [var progress: AVAssetWritingPlannerProgress](avassetwritingplanner/progress.md)
  The current progress of the AVAssetWritingPlanner.
### Configuring segment boundaries
- [AVAssetWritingPlanner.SegmentBoundaryGuidelines](avassetwritingplanner/segmentboundaryguidelines.md)
  AVPlannedVideoSegmentBoundaryGuidelines provides guidance on determining planned segment boundaries for a video track in an incremental writing session executed by the AVAssetWritingPlanner.
### Handling segment results
- [AVAssetWritingPlanner.SegmentResult](avassetwritingplanner/segmentresult.md)
  Result type for manual segment completion control.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md)
  AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session.
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
- [class AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)
  AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner)*