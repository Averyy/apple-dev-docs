# AVVideoCompositionInstruction.Configuration

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Configurable properties for initializing a new AVVideoCompositionInstruction instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(backgroundColor: CGColor?, enablePostProcessing: Bool, layerInstructions: [AVVideoCompositionLayerInstruction], requiredSourceSampleDataTrackIDs: [CMPersistentTrackID], timeRange: CMTimeRange)](./configuration/init%28backgroundcolor,enablepostprocessing,layerinstructions,requiredsourcesampledatatrackids,timerange%29.md)
### Inspecting the configuration
- [var backgroundColor: CGColor?](./configuration/backgroundcolor.md)
  The background color of the composition.
- [var enablePostProcessing: Bool](./configuration/enablepostprocessing.md)
  A Boolean value that indicates whether the composition enables post-processing.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./configuration/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var requiredSourceSampleDataTrackIDs: [CMPersistentTrackID]](./configuration/requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [var timeRange: CMTimeRange](./configuration/timerange.md)
  The time range to which the instruction applies.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an instruction
- [convenience init(configuration: AVVideoCompositionInstruction.Configuration)](./init%28configuration%29.md)
  Initialize an AVVideoCompositionInstruction with a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration)*