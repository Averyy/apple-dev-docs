# FeatureSet

**Framework**: PaperKit  
**Kind**: struct

The features supported by PaperKit UI / data models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct FeatureSet
```

## Topics

### Structures
- [FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct.md)
  Which ends of an line can have arrows.
### Instance Properties
- [var colorMaximumLinearExposure: CGFloat](featureset/colormaximumlinearexposure.md)
  The maximum exposure to allow for choosing colors.
- [var contentVersion: FeatureSet.ContentVersion](featureset/contentversion-swift.property.md)
  The version of PaperKit supported.
- [var features: Set<FeatureSet.Feature>](featureset/features.md)
  The supported features.
- [var inks: Set<PKInkingTool.InkType>](featureset/inks.md)
  The inks types that are supported.
- [var lineMarkerPositions: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.property.md)
  The allowed ends of line for arrows.
- [var shapes: Set<ShapeConfiguration.Shape>](featureset/shapes.md)
  The supported shape types.
### Instance Methods
- [func contains(FeatureSet.Feature) -> Bool](featureset/contains(_:).md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func insert(FeatureSet.Feature)](featureset/insert(_:).md)
  Inserts the given feature in the set if it is not already present.
- [func isSubset(of: FeatureSet) -> Bool](featureset/issubset(of:).md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func remove(FeatureSet.Feature)](featureset/remove(_:).md)
  Removes the given feature.
### Type Properties
- [static var empty: FeatureSet](featureset/empty.md)
  A maximally empty feature set.
- [static var latest: FeatureSet](featureset/latest.md)
  A new feature set supporting all features.
- [static var version1: FeatureSet](featureset/version1.md)
  A new feature set supporting all features in `.version1`.
### Enumerations
- [FeatureSet.ContentVersion](featureset/contentversion-swift.enum.md)
- [FeatureSet.Feature](featureset/feature.md)
  The features that PaperKit markup supports.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ShapeConfiguration](shapeconfiguration.md)
  A configuration that specifies the appearance of a shape.
- [struct RenderingOptions](renderingoptions.md)
  The rendering options for drawing paper data models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset)*