# totalAccumulatedFrameDelay

**Framework**: AVFoundation  
**Kind**: property

The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var totalAccumulatedFrameDelay: TimeInterval { get }
```

## See Also

- [var numberOfCorruptedFrames: Int](avvideoperformancemetrics/numberofcorruptedframes.md)
  The total number of corrupted frames.
- [var numberOfDroppedFrames: Int](avvideoperformancemetrics/numberofdroppedframes.md)
  The total number of frames the system drops prior to decoding or from missing the display deadline.
- [var numberOfFramesDisplayedUsingOptimizedCompositing: Int](avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing.md)
  The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [var totalNumberOfFrames: Int](avvideoperformancemetrics/totalnumberofframes.md)
  The total number of frames that display if no frames drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/totalaccumulatedframedelay)*