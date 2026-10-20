# PHASESpatialPipeline.Flags

**Framework**: PHASE  
**Kind**: struct  
**Role**: Structure

Sound resonance options for a spatial pipeline.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct Flags
```

```c
enum PHASESpatialPipelineFlags : NSUInteger;
```

#### Overview

Each [`PHASESpatialPipeline`](../phasespatialpipeline.md) specifies a flag in its [`init(flags:)`](./init%28flags%29.md) initializer.

## Topics

### Creating a Flag
- [init(rawValue: UInt)](./flags-swift.struct/init%28rawvalue%29.md)
  Initializes a spatial flag with the given string.
### Choosing a Flag
- [static var directPathTransmission: PHASESpatialPipeline.Flags](./flags-swift.struct/directpathtransmission.md)
  A spatial property that refers to the original audio signal.
- [static var earlyReflections: PHASESpatialPipeline.Flags](./flags-swift.struct/earlyreflections.md)
  A spatial property that refers to the earlier echoes along the duration of sound resonance.
- [static var lateReverb: PHASESpatialPipeline.Flags](./flags-swift.struct/latereverb.md)
  A spatial property that refers to the later echoes along the duration of sound resonance.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Sound Reflections and Resonance
- [class PHASESpatialPipeline](../phasespatialpipeline.md)
  An object that specifies the volume of optional environmental effects.
- [class PHASESpatialPipelineEntry](../phasespatialpipelineentry.md)
  An audio layer with an adjustable volume for a spatial mixer’s output.
- [struct PHASESpatialCategory](../phasespatialcategory.md)
  Sound resonance effects for spatial mixing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline/flags-swift.struct)*