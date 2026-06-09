# segmentBoundaryGuidelinesForVideo(codecType:encoderSpecification:)

**Framework**: AVFoundation  
**Kind**: method

Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func segmentBoundaryGuidelinesForVideo(codecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]) -> AVAssetWritingPlanner.SegmentBoundaryGuidelines
```

#### Return Value

An AVAssetWritingPlanner.SegmentBoundaryGuidelines with the minimum frame count and duration for the given codec and encoder.

#### Discussion

The encoderSpecification parameter here is the same encoder specification the client uses to compress the video track.

## Parameters

- `codecType`: The output video codec type for the video track.
- `encoderSpecification`: A dictionary of kVTVideoEncoderSpecification_* keys describing the video encoder. This is the same specification the client uses to compress the video track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:))*