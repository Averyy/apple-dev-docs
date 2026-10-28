# requiresFrameReordering

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var requiresFrameReordering: AVAsyncProperty<Root, Bool> { get }
```

Available when `Root` inherits `AVAssetTrack`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading frame-based characteristics
- [static var nominalFrameRate: AVAsyncProperty<Root, Float>](./nominalframerate.md)
  The frame rate of the track, in frames per second.
- [static var minFrameDuration: AVAsyncProperty<Root, CMTime>](./minframeduration.md)
  The minimum duration of the track’s frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/requiresframereordering)*