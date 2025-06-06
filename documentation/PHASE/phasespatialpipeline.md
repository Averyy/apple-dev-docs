# PHASESpatialPipeline

**Framework**: PHASE  
**Kind**: class

An object that specifies the volume of optional environmental effects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESpatialPipeline
```

#### Overview

The [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md) class contains an instance of this class, [`spatialPipeline`](phasespatialmixerdefinition/spatialpipeline.md), to add optional sound layers to the output.

On top of the original audio signal designated by [`directPathTransmission`](phasespatialpipeline/flags-swift.struct/directpathtransmission.md), this class optionally includes audio layers for environmental effects, such as [`earlyReflections`](phasespatialcategory/earlyreflections.md) or [`lateReverb`](phasespatialcategory/latereverb.md), in the output.  To control the amount of volume that either audio layer possesses in the mixer’s output, adjust the [`sendLevel`](phasespatialpipelineentry/sendlevel.md) for the layer’s respective [`PHASESpatialPipelineEntry`](phasespatialpipelineentry.md) member in the [`entries`](phasespatialpipeline/entries.md) dictionary.

## Topics

### Creating a Spatial Pipeline
- [init?(flags: PHASESpatialPipeline.Flags)](phasespatialpipeline/init(flags:).md)
  Creates a spatial pipeline with the specified flags.
- [PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct.md)
  Sound resonance options for a spatial pipeline.
### Inspecting Effects
- [var flags: PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.property.md)
  A collection of environmental effects to include in the output.
- [var entries: [PHASESpatialCategory : PHASESpatialPipelineEntry]](phasespatialpipeline/entries.md)
  Audio layers for environmental effects to add to the output.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASESpatialPipelineEntry](phasespatialpipelineentry.md)
  An audio layer with an adjustable volume for a spatial mixer’s output.
- [struct PHASESpatialCategory](phasespatialcategory.md)
  Sound resonance effects for spatial mixing.
- [PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct.md)
  Sound resonance options for a spatial pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline)*