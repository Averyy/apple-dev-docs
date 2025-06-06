# PHASESpatialPipeline.Flags

**Framework**: PHASE  
**Kind**: struct

Sound resonance options for a spatial pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Flags
```

#### Overview

Each [`PHASESpatialPipeline`](phasespatialpipeline.md) specifies a flag in its [`init(flags:)`](phasespatialpipeline/init(flags:).md) initializer.

## Topics

### Creating a Flag
- [init(rawValue: UInt)](phasespatialpipeline/flags-swift.struct/init(rawvalue:).md)
  Initializes a spatial flag with the given string.
### Choosing a Flag
- [static var directPathTransmission: PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct/directpathtransmission.md)
  A spatial property that refers to the original audio signal.
- [static var earlyReflections: PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct/earlyreflections.md)
  A spatial property that refers to the earlier echoes along the duration of sound resonance.
- [static var lateReverb: PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct/latereverb.md)
  A spatial property that refers to the later echoes along the duration of sound resonance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class PHASESpatialPipeline](phasespatialpipeline.md)
  An object that specifies the volume of optional environmental effects.
- [class PHASESpatialPipelineEntry](phasespatialpipelineentry.md)
  An audio layer with an adjustable volume for a spatial mixer’s output.
- [struct PHASESpatialCategory](phasespatialcategory.md)
  Sound resonance effects for spatial mixing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline/flags-swift.struct)*