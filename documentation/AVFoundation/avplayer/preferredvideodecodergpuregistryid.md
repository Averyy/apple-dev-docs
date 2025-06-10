# preferredVideoDecoderGPURegistryID

**Framework**: AVFoundation  
**Kind**: property

The registry identifier for the GPU used for video decoding.

**Availability**:
- macOS 10.13+

## Declaration

```swift
nonisolated
var preferredVideoDecoderGPURegistryID: UInt64 { get set }
```

#### Discussion

By default, whenever possible, the GPU associated with the display presenting the [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) performs the video decoding. Decode transitions to a new GPU, if appropriate, when the [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) moves to a new display. This property overrides this default behavior, forcing decode to prefer an affinity to the GPU specified regardless of which GPU displays the associated [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer). Obtain the GPU registry ID from the GPU [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) using [`registryID`](https://developer.apple.com/documentation/Metal/MTLDevice/registryID) or from OpenGL or OpenCL.

> ❗ **Important**:  You must specify an external GPU (or a slotted GPU in Mac Pro) with this property. You can’t switch decoding between the integrated graphics and the built-in discrete graphics.

## See Also

- [var audioOutputDeviceUniqueID: String?](avplayer/audiooutputdeviceuniqueid.md)
  Specifies the unique ID of the Core Audio output device used to play audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preferredvideodecodergpuregistryid)*