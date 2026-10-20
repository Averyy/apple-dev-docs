# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time range of the track within the overall timeline of the asset.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`timeRange`](../avpartialasyncproperty/timerange.md) asynchronously instead.

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```

#### Discussion

If the start of the time range is greater than [`zero`](../../CoreMedia/cmtime/zero.md), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

**Swift**:

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

**Objective-C**:

```objc
if CMTIME_COMPARE_INLINE(track.timeRange.start, >, kCMTimeZero) {
    // Delayed start.
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/timerange)*