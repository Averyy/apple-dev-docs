# nominalFrameRate

**Framework**: AVFoundation  
**Kind**: property

The frame rate of the track, in frames per second.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var nominalFrameRate: Float { get }
```

#### Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

- [var minFrameDuration: CMTime](avmutablemovietrack/minframeduration.md)
  The minimum duration of the track’s frames.
- [var requiresFrameReordering: Bool](avmutablemovietrack/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/nominalframerate)*