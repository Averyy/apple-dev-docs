# init(mediaType:segmentConfigurations:assemblyTrackID:)

**Framework**: AVFoundation  
**Kind**: init

Returns an instance of AVAssetTrackPlan

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(mediaType: AVMediaType, segmentConfigurations: [AVPlannedSegmentConfiguration], assemblyTrackID trackID: CMPersistentTrackID)
```

#### Discussion

This initializer throws NSInvalidArgumentException if trackID is kCMPersistentTrackID_Invalid.

## Parameters

- `mediaType`: Media type of the track
- `segmentConfigurations`: Segment configurations of the track
- `trackID`: The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:))*