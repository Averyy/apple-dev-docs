# PHASESpatialPipelineEntry

**Framework**: PHASE  
**Kind**: class

An audio layer with an adjustable volume for a spatial mixer’s output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESpatialPipelineEntry
```

#### Overview

This property adjusts the amount of audio that passes through a spatial mixer’s pipeline ([`spatialPipeline`](phasespatialmixerdefinition/spatialpipeline.md)) to the output. The pipeline’s [`entries`](phasespatialpipeline/entries.md) contains an instance of this class for each type of audio layer that [`PHASESpatialCategory`](phasespatialcategory.md) defines. Depending on the layer’s type, the audio may sound like spatial relections, environmental reverb, or the unfiltered signal. An app adjusts the layer’s presence in the mixer’s output by:

- Defining an initial volume using [`sendLevel`](phasespatialpipelineentry/sendlevel.md)
- Adjusting the audio’s volume dynamically, for example, by fading it over a duration using [`sendLevelMetaParameterDefinition`](phasespatialpipelineentry/sendlevelmetaparameterdefinition.md)

## Topics

### Setting the Send Level
- [var sendLevel: Double](phasespatialpipelineentry/sendlevel.md)
  The amount of audio signal to add to the output.
### Fading the Send Level
- [var sendLevelMetaParameterDefinition: PHASENumberMetaParameterDefinition?](phasespatialpipelineentry/sendlevelmetaparameterdefinition.md)
  A parameter that gradually updates the amount of audio signal that passes through to the output.

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

- [class PHASESpatialPipeline](phasespatialpipeline.md)
  An object that specifies the volume of optional environmental effects.
- [struct PHASESpatialCategory](phasespatialcategory.md)
  Sound resonance effects for spatial mixing.
- [PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct.md)
  Sound resonance options for a spatial pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipelineentry)*