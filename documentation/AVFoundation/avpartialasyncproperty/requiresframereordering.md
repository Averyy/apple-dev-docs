# requiresFrameReordering

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

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
static var requiresFrameReordering: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

## See Also

- [static var nominalFrameRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [static var minFrameDuration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minframeduration.md)
  The minimum duration of the track’s frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/requiresframereordering)*