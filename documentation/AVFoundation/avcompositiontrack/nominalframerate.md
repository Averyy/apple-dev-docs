# nominalFrameRate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The frame rate of the track, in frames per second.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var nominalFrameRate: Float { get }
```

## Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

### Accessing frame-based characteristics
- [var minFrameDuration: CMTime](./minframeduration.md)
  The minimum duration of the track’s frames.
- [var requiresFrameReordering: Bool](./requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/nominalframerate)*