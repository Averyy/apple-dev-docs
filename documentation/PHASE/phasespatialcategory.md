# PHASESpatialCategory

**Framework**: PHASE  
**Kind**: struct

Sound resonance effects for spatial mixing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct PHASESpatialCategory
```

#### Discussion

This class identifies the various audio layers that a spatial mixer offers as keys to the [`entries`](phasespatialpipeline/entries.md) dictionary.

## Topics

### Creating a Spatial Category
- [init(rawValue: String)](phasespatialcategory/init(rawvalue:).md)
  Initializes a spatial category with the given string.
### Categories
- [static let directPathTransmission: PHASESpatialCategory](phasespatialcategory/directpathtransmission.md)
  A spatial category that refers to the unfiltered audio signal.
- [static let earlyReflections: PHASESpatialCategory](phasespatialcategory/earlyreflections.md)
  A spatial category that refers to the earlier echoes along the duration of sound resonance.
- [static let lateReverb: PHASESpatialCategory](phasespatialcategory/latereverb.md)
  A spatial category that refers to the later echoes along the duration of sound resonance.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class PHASESpatialPipeline](phasespatialpipeline.md)
  An object that specifies the volume of optional environmental effects.
- [class PHASESpatialPipelineEntry](phasespatialpipelineentry.md)
  An audio layer with an adjustable volume for a spatial mixer’s output.
- [PHASESpatialPipeline.Flags](phasespatialpipeline/flags-swift.struct.md)
  Sound resonance options for a spatial pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialcategory)*