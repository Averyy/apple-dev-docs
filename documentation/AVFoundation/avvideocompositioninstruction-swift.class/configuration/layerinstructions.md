# layerInstructions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Instructions that specify how to layer and compose video frames from source tracks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var layerInstructions: [AVVideoCompositionLayerInstruction] { get set }
```

## See Also

### Inspecting the configuration
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the composition.
- [var enablePostProcessing: Bool](./enablepostprocessing.md)
  A Boolean value that indicates whether the composition enables post-processing.
- [var requiredSourceSampleDataTrackIDs: [CMPersistentTrackID]](./requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range to which the instruction applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration/layerinstructions)*