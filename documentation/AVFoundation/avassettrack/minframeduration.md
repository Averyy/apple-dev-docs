# minFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The minimum duration of the track’s frames.

**Availability**:
- iOS 7.0+ - Deprecated in 16.0
- iPadOS 7.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`minFrameDuration`](../avpartialasyncproperty/minframeduration.md) asynchronously instead.

## Declaration

```swift
var minFrameDuration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime minFrameDuration;
```

#### Discussion

A track’s minimum frame duration is the reciprocal of its maximum frame rate. For example, a video track with a maximum frame rate of 30 frames per second has a minimum frame duration of 1/30, or 0.033 seconds.

The value of this property is [`invalid`](../../CoreMedia/cmtime/invalid.md) if the track can’t calculate its minimum frame duration, or if it’s unknown.

## See Also

### Accessing frame-based characteristics
- [nominalFrameRate](./nominalframerate.md)
  The frame rate of the track, in frames per second.
- [requiresFrameReordering](./requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/minframeduration)*