# nominalFrameRate

**Framework**: AVFoundation  
**Kind**: property

The frame rate of the track, in frames per second.

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
static var nominalFrameRate: AVAsyncProperty<Root, Float> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

- [static var minFrameDuration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minframeduration.md)
  The minimum duration of the track’s frames.
- [static var requiresFrameReordering: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/nominalframerate)*