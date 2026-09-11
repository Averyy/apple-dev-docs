# init(duration:)

**Framework**: AVFoundation  
**Kind**: init

Creates an instance of AVPlannedSegmentConfiguration specifying the duration of the planned segment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(duration: CMTime)
```

#### Return Value

An instance of AVPlannedSegmentConfiguration, or nil if initialization fails.

#### Discussion

The duration parameter must be numeric and greater than 0. Otherwise, the initializer throws NSInvalidArgumentException.

## Parameters

- `duration`: The total duration of this planned segment. If an empty edit is included, this duration may be larger than the sum of the durations of the samples in this planned segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentconfiguration/init(duration:))*