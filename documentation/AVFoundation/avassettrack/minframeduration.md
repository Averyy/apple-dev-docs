# minFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The minimum duration of the track’s frames.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
var minFrameDuration: CMTime { get }
```

#### Discussion

A track’s minimum frame duration is the reciprocal of its maximum frame rate. For example, a video track with a maximum frame rate of 30 frames per second has a minimum frame duration of 1/30, or 0.033 seconds.

The value of this property is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) if the track can’t calculate its minimum frame duration, or if it’s unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/minframeduration)*