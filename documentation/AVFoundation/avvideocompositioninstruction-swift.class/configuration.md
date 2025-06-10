# AVVideoCompositionInstruction.Configuration

**Framework**: AVFoundation  
**Kind**: struct

Configurable properties for initializing a new AVVideoCompositionInstruction instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(backgroundColor: CGColor?, enablePostProcessing: Bool, layerInstructions: [AVVideoCompositionLayerInstruction], requiredSourceSampleDataTrackIDs: [CMPersistentTrackID], timeRange: CMTimeRange)](avvideocompositioninstruction-swift.class/configuration/init(backgroundcolor:enablepostprocessing:layerinstructions:requiredsourcesampledatatrackids:timerange:).md)
### Instance Properties
- [var backgroundColor: CGColor?](avvideocompositioninstruction-swift.class/configuration/backgroundcolor.md)
  The background color of the composition.
- [var enablePostProcessing: Bool](avvideocompositioninstruction-swift.class/configuration/enablepostprocessing.md)
  A Boolean value that indicates whether the composition enables post-processing.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avvideocompositioninstruction-swift.class/configuration/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var requiredSourceSampleDataTrackIDs: [CMPersistentTrackID]](avvideocompositioninstruction-swift.class/configuration/requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [var timeRange: CMTimeRange](avvideocompositioninstruction-swift.class/configuration/timerange.md)
  The time range to which the instruction applies.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration)*