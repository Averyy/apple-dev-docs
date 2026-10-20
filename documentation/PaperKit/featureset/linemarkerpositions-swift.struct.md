# FeatureSet.LineMarkerPositions

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

The arrow marker positions for the ends of a line.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct LineMarkerPositions
```

## Topics

### Choosing marker positions
- [static let plain: FeatureSet.LineMarkerPositions](./linemarkerpositions-swift.struct/plain.md)
  Neither end of a line has markers.
- [static let single: FeatureSet.LineMarkerPositions](./linemarkerpositions-swift.struct/single.md)
  Either the start/end of a line has a marker.
- [static let double: FeatureSet.LineMarkerPositions](./linemarkerpositions-swift.struct/double.md)
  Both the start and end of a line has a marker.
- [static let all: FeatureSet.LineMarkerPositions](./linemarkerpositions-swift.struct/all.md)
  All possible combinations of marker positions.
### Initializers
- [init(rawValue: Int)](./linemarkerpositions-swift.struct/init%28rawvalue%29.md)
  Creates a new set of marker positions from the given raw value.
### Instance Properties
- [let rawValue: Int](./linemarkerpositions-swift.struct/rawvalue.md)
  The raw bitmask that represents this set of marker positions.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Describing feature types
- [FeatureSet.Feature](./feature.md)
  The features that PaperKit markup supports.
- [FeatureSet.ContentVersion](./contentversion-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/linemarkerpositions-swift.struct)*