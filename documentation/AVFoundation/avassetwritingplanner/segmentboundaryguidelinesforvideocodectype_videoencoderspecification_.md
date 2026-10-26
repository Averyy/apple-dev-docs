# segmentBoundaryGuidelinesForVideoCodecType:videoEncoderSpecification:

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

```objc
+ (AVPlannedVideoSegmentBoundaryGuidelines) segmentBoundaryGuidelinesForVideoCodecType:(AVVideoCodecType) videoCodecType videoEncoderSpecification:(NSDictionary *) videoEncoderSpecification;
```

#### Return Value

An AVPlannedVideoSegmentBoundaryGuidelines.

#### Discussion

The videoEncoderSpecification parameter here is the same encoder specification the client uses to compress the video track.

## Parameters

- `videoCodecType`: The output videoCodecType for the video track.
- `videoEncoderSpecification`: The video encoder specification includes options for choosing a specific video encoder. This is a dictionary containing kVTVideoEncoderSpecification_* keys specified in the VideoToolbox framework.

## See Also

### Getting segment boundary guidance
- [class func segmentBoundaryRecommendations(forVideoTrack: AVAssetTrack, minimumSegmentDuration: CMTime, minimumSegmentFrameCount: Int) -> [AVPlannedVideoSegmentConfiguration]](./segmentboundaryrecommendations%28forvideotrack,minimumsegmentduration,minimumsegmentframecount%29.md)
  Returns segment boundary recommendations for a given source video asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideocodectype:videoencoderspecification:)*