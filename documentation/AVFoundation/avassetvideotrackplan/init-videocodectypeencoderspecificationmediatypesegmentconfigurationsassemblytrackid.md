# init(videoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:)

**Framework**: AVFoundation  
**Kind**: init

Creates an instance of AVAssetVideoTrackPlan.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(videoCodecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]? = nil, mediaType: AVMediaType, segmentConfigurations: [AVPlannedVideoSegmentConfiguration], assemblyTrackID: CMPersistentTrackID)
```

#### Discussion

This initializer throws NSInvalidArgumentException in the following cases:

1. mediaType is not supported. Supported media types are AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture
2. The encoder specified by videoCodecType and encoderSpecification does not support video encoding in segments

## Parameters

- `videoCodecType`: Video codec type of the track.
- `encoderSpecification`: A dictionary describing the characteristics of a video encoder to use. Pass nil to let the system choose an encoder. If the client provides a specification, it should omit the following keys: kVTCompressionPropertyKey_SourceFrameCount, kVTCompressionPropertyKey_MoreFramesBeforeStart, and kVTCompressionPropertyKey_MoreFramesAfterEnd, since such keys will be overwritten by the underlying implementation.
- `mediaType`: Media type of the track. Only AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture are supported.
- `segmentConfigurations`: Segment configurations of the track.
- `assemblyTrackID`: The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan/init(videocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:))*