# nominalFrameRate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The frame rate of the track, in frames per second.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`nominalFrameRate`](../avpartialasyncproperty/nominalframerate.md) asynchronously instead.

## Declaration

```swift
var nominalFrameRate: Float { get }
```

```objc
@property (nonatomic, readonly) float nominalFrameRate;
```

#### Discussion

The nominal frame rate indicates the number of frames per second for tracks that contain a full frame per media sample. For field-based (interlaced) video tracks, the value of this property indicates the field rate, not the frame rate.

## See Also

### Accessing frame-based characteristics
- [minFrameDuration](./minframeduration.md)
  The minimum duration of the track’s frames.
- [requiresFrameReordering](./requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/nominalframerate)*