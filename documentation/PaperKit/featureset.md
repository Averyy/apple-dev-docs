# FeatureSet

**Framework**: PaperKit  
**Kind**: struct

The features PaperKit supports in its UI and data models.

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

### Creating a feature set
- [static var version1: FeatureSet](featureset/version1.md)
  A new feature set supporting all features in version 1.
- [static var version2: FeatureSet](featureset/version2.md)
  A new feature set supporting all features in version 2.
- [static var latest: FeatureSet](featureset/latest.md)
  A new feature set supporting all features.
- [static var empty: FeatureSet](featureset/empty.md)
  A maximally empty feature set.
### Configuring features
- [var features: Set<FeatureSet.Feature>](featureset/features.md)
  The supported features.
- [var shapes: Set<ShapeConfiguration.Shape>](featureset/shapes.md)
  The supported shape types.
- [var inks: Set<PKInkingTool.InkType>](featureset/inks.md)
  The supported ink types.
- [var contentVersion: FeatureSet.ContentVersion](featureset/contentversion-swift.property.md)
  The PaperKit version the feature set supports.
- [var lineMarkerPositions: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.property.md)
  The allowed ends of line for arrows.
- [var colorMaximumLinearExposure: CGFloat](featureset/colormaximumlinearexposure.md)
  The maximum exposure to allow for choosing colors.
### Checking features
- [func contains(FeatureSet.Feature) -> Bool](featureset/contains(_:).md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func isSubset(of: FeatureSet) -> Bool](featureset/issubset(of:).md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func insert(FeatureSet.Feature)](featureset/insert(_:).md)
  Inserts the given feature in the set if it is not already present.
- [func remove(FeatureSet.Feature)](featureset/remove(_:).md)
  Removes the given feature.
### Describing feature types
- [FeatureSet.Feature](featureset/feature.md)
  The features that PaperKit markup supports.
- [FeatureSet.ContentVersion](featureset/contentversion-swift.enum.md)
- [FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.struct.md)
  The arrow marker positions for the ends of a line.

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
- [struct MarkupAutoresizing](markupautoresizing.md)
  Automatic sizing behaviors for this markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset)*