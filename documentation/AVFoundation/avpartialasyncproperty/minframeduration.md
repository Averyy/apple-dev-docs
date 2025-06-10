# minFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The minimum duration of the track’s frames.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var minFrameDuration: AVAsyncProperty<Root, CMTime> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

A track’s minimum frame duration is the reciprocal of its maximum frame rate. For example, a video track with a maximum frame rate of 30 frames per second has a minimum frame duration of 1/30, or 0.033 seconds.

The value of this property is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) if the track can’t calculate its minimum frame duration, or if it’s unknown.

## See Also

- [static var nominalFrameRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [static var requiresFrameReordering: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/minframeduration)*