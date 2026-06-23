# init(numberOfFrames:duration:)

**Framework**: AVFoundation  
**Kind**: init

Creates an instance of AVPlannedVideoSegmentConfiguration specifying the number of frames in and total duration of the segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(numberOfFrames frameCount: Int, duration: CMTime)
```

#### Return Value

An instance of AVPlannedVideoSegmentConfiguration.

#### Discussion

For best results, frameCount and duration should be greater or equal to the minimumFrameCount and minimumDuration of AVPlannedVideoSegmentBoundaryGuidelines respectively. This initializer throws NSInvalidArgumentException if frameCount is less than or equal to 0, or duration is not numeric, or duration is less than or equal to 0.

## Parameters

- `frameCount`: The number of frames in this planned video segment.
- `duration`: The duration of this planned video segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentconfiguration/init(numberofframes:duration:))*