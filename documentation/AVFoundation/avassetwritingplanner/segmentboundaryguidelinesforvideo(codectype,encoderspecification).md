# segmentBoundaryGuidelinesForVideo(codecType:encoderSpecification:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func segmentBoundaryGuidelinesForVideo(codecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]) -> AVAssetWritingPlanner.SegmentBoundaryGuidelines
```

## Return Value

An AVAssetWritingPlanner.SegmentBoundaryGuidelines with the minimum frame count and duration for the given codec and encoder.

## Discussion

The encoderSpecification parameter here is the same encoder specification the client uses to compress the video track.

## Parameters

- `codecType`: The output video codec type for the video track.
- `encoderSpecification`: A dictionary of kVTVideoEncoderSpecification_* keys describing the video encoder. This is the same specification the client uses to compress the video track.

## See Also

### Getting segment boundary guidance
- [class func segmentBoundaryRecommendations(forVideoTrack: AVAssetTrack, minimumSegmentDuration: CMTime, minimumSegmentFrameCount: Int) -> [AVPlannedVideoSegmentConfiguration]](./segmentboundaryrecommendations%28forvideotrack,minimumsegmentduration,minimumsegmentframecount%29.md)
  Returns segment boundary recommendations for a given source video asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:))*