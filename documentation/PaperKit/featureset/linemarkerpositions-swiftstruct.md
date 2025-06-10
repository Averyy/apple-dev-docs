# FeatureSet.LineMarkerPositions

**Framework**: PaperKit  
**Kind**: struct

Which ends of an line can have arrows.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct LineMarkerPositions
```

## Topics

### Initializers
- [init(rawValue: Int)](featureset/linemarkerpositions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int](featureset/linemarkerpositions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [FeatureSet.LineMarkerPositions.ArrayLiteralElement](featureset/linemarkerpositions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [FeatureSet.LineMarkerPositions.Element](featureset/linemarkerpositions-swift.struct/element.md)
  The element type of the option set.
- [FeatureSet.LineMarkerPositions.RawValue](featureset/linemarkerpositions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let all: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/all.md)
  All possible combinations of marker positions.
- [static let double: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/double.md)
  Both the start and end of a line has a marker.
- [static let plain: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/plain.md)
  Neither end of a line has markers.
- [static let single: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct/single.md)
  Either the start/end of a line has a marker.
### Default Implementations
- [Equatable Implementations](featureset/linemarkerpositions-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](featureset/linemarkerpositions-swift.struct/optionset-implementations.md)
- [RawRepresentable Implementations](featureset/linemarkerpositions-swift.struct/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](featureset/linemarkerpositions-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/linemarkerpositions-swift.struct)*