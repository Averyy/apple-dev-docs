# init(mediaType:segmentConfigurations:assemblyTrackID:)

**Framework**: AVFoundation  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(mediaType: AVMediaType, segmentConfigurations: [AVPlannedSegmentConfiguration], assemblyTrackID trackID: CMPersistentTrackID)
```

#### Discussion

Returns an instance of AVAssetTrackPlan

This initializer throws NSInvalidArgumentException if trackID is kCMPersistentTrackID_Invalid.

## Parameters

- `mediaType`: Media type of the track
- `segmentConfigurations`: Segment configurations of the track
- `trackID`: The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:))*