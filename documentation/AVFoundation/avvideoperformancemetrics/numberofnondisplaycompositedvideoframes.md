# numberOfNonDisplayCompositedVideoFrames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

## Declaration

```objc
@property (nonatomic, readonly) unsigned long numberOfNonDisplayCompositedVideoFrames;
```

## Discussion

[SPI] The total number of frames that were composited in undetached mode.

## See Also

### Inspecting metrics
- [var numberOfCorruptedFrames: Int](./numberofcorruptedframes.md)
  The total number of corrupted frames.
- [numberOfCorruptedVideoFrames](./numberofcorruptedvideoframes.md)
- [numberOfDisplayCompositedVideoFrames](./numberofdisplaycompositedvideoframes.md)
- [var numberOfDroppedFrames: Int](./numberofdroppedframes.md)
  The total number of frames the system drops prior to decoding or from missing the display deadline.
- [numberOfDroppedVideoFrames](./numberofdroppedvideoframes.md)
- [var numberOfFramesDisplayedUsingOptimizedCompositing: Int](./numberofframesdisplayedusingoptimizedcompositing.md)
  The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [var totalAccumulatedFrameDelay: TimeInterval](./totalaccumulatedframedelay.md)
  The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalFrameDelay](./totalframedelay.md)
- [var totalNumberOfFrames: Int](./totalnumberofframes.md)
  The total number of frames that display if no frames drop.
- [totalNumberOfVideoFrames](./totalnumberofvideoframes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/numberofnondisplaycompositedvideoframes)*