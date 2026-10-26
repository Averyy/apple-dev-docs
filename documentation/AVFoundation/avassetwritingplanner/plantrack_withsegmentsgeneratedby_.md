# planTrack:withSegmentsGeneratedBy:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds an AVAssetTrackPlan to this AVAssetWritingPlanner, with a block to be called by the planner to generate each segment of the track.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) planTrack:(AVAssetTrackPlan *) trackPlan withSegmentsGeneratedBy:(void (^)(AVPlannedSegmentWritingRequest *segmentWriteRequest)) writingSegmentCallbackBlock;
```

#### Discussion

This method throws NSInternalInconsistencyException if a trackPlan with the same assemblyTrackID already exists in the planner, or if called after executePlanWithCompletionHandler: has been invoked.

## Parameters

- `trackPlan`: The track plan contains information about the track and boundaries of all the segments.
- `writingSegmentCallbackBlock`: A block to be called by the AVAssetWritingPlanner on each incremental segment for this track to write the segment to an intermediate file, according to the specifications in the “segmentWriteRequest” object passed to the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/plantrack:withsegmentsgeneratedby:)*