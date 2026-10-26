# initWithVideoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an instance of AVAssetVideoTrackPlan

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (instancetype) initWithVideoCodecType:(AVVideoCodecType) videoCodecType encoderSpecification:(NSDictionary *) encoderSpecification mediaType:(AVMediaType) mediaType segmentConfigurations:(NSArray<AVPlannedSegmentConfiguration *> *) segmentConfigurations assemblyTrackID:(CMPersistentTrackID) trackID;
```

#### Discussion

This initializer throws NSInvalidArgumentException in the following cases.

1. mediaType is not supported. Supported media types are AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture
2. The encoder specified by videoCodecType and encoderSpecification does not support video encoding in segments

## Parameters

- `videoCodecType`: Video codec type of the track
- `encoderSpecification`: The encoder specification the client will use to write planned segments of this track
- `mediaType`: Media type of the track. Only AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture are supported.
- `segmentConfigurations`: Segment configurations of the track
- `trackID`: The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan/initwithvideocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:)*