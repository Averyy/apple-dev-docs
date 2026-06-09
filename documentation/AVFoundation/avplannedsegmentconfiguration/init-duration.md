# init(duration:)

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
init(duration: CMTime)
```

#### Return Value

An instance of AVPlannedSegmentConfiguration, or nil if initialization fails.

#### Discussion

Creates an instance of AVPlannedSegmentConfiguration specifying the duration of the planned segment.

The duration parameter must be numeric and greater than 0. Otherwise, the initializer throws NSInvalidArgumentException.

## Parameters

- `duration`: The total duration of this planned segment. If an empty edit is included, this duration may be larger than the sum of the durations of the samples in this planned segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentconfiguration/init(duration:))*