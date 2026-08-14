# FeatureSet.LineMarkerPositions

**Framework**: PaperKit  
**Kind**: struct

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
- [static let plain: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/plain.md)
  Neither end of a line has markers.
- [static let single: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/single.md)
  Either the start/end of a line has a marker.
- [static let double: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/double.md)
  Both the start and end of a line has a marker.
- [static let all: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/all.md)
  All possible combinations of marker positions.
### Initializers
- [init(rawValue: Int)](featureset/linemarkerpositions-swift.struct/init(rawvalue:).md)
  Creates a new set of marker positions from the given raw value.
### Instance Properties
- [let rawValue: Int](featureset/linemarkerpositions-swift.struct/rawvalue.md)
  The raw bitmask that represents this set of marker positions.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [FeatureSet.Feature](featureset/feature.md)
  The features that PaperKit markup supports.
- [FeatureSet.ContentVersion](featureset/contentversion-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/linemarkerpositions-swift.struct)*