# segmentBoundaryRecommendations(forVideoTrack:minimumSegmentDuration:minimumSegmentFrameCount:)

**Framework**: AVFoundation  
**Kind**: method

Returns segment boundary recommendations for a given source video asset track.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class func segmentBoundaryRecommendations(forVideoTrack videoAssetTrack: AVAssetTrack, minimumSegmentDuration: CMTime, minimumSegmentFrameCount: Int) -> [AVPlannedVideoSegmentConfiguration]
```

#### Return Value

Array of AVPlannedVideoSegmentConfiguration objects, each element specifying the configuration of a planned video segment, ordered in output PTS order

#### Discussion

This is a convenience method that can help clients to pick optimal segmentation boundaries for a given source video AVAssetTrack based on the structure of the track and the minimumSegmentDuration and minimumSegmentFrameCount values provided.

The client needs to ensure that the minimumSegmentDuration is greater than or equal to the segment boundary guidelines for the codec type. The client should also ensure that minimumSegmentFrameCount also exceeds the segment boundary guidelines.

The segments returned will satisfy both the minimumSegmentDuration and minimumSegmentFrameCount requirements. The only exception is the very last segment, which may be shorter.

The returned array will ensure that segment boundaries occur on sample boundaries.

Clients can use these results to fill in the AVPlannedVideoSegmentConfiguration for this asset track, if the output maintains the source timing. If the output timing differs from the source, then the returned AVPlannedVideoSegmentConfiguration array’s results need to be modified accordingly by the client.

This method throws NSInvalidArgumentException if minimumSegmentDuration is not numeric or is less than or equal to zero, or if minimumSegmentFrameCount is less than or equal to 0.

## Parameters

- `videoAssetTrack`: The source video AVAssetTrack to be analyzed.
- `minimumSegmentDuration`: The client selected minimum duration for the segments.
- `minimumSegmentFrameCount`: The minimum number of source frames in a segment.

## See Also

- [static func segmentBoundaryGuidelinesForVideo(codecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]) -> AVAssetWritingPlanner.SegmentBoundaryGuidelines](avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:).md)
  Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryrecommendations(forvideotrack:minimumsegmentduration:minimumsegmentframecount:))*