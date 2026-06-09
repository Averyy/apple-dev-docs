# shapes

**Framework**: PaperKit  
**Kind**: property

The supported shape types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var shapes: Set<ShapeConfiguration.Shape>
```

#### Discussion

Default is all shapes. Set to an empty set to disable all shapes.

## See Also

- [var features: Set<FeatureSet.Feature>](featureset/features.md)
  The supported features.
- [var inks: Set<PKInkingTool.InkType>](featureset/inks.md)
  The supported ink types.
- [var contentVersion: FeatureSet.ContentVersion](featureset/contentversion-swift.property.md)
  The PaperKit version the feature set supports.
- [var lineMarkerPositions: FeatureSet.LineMarkerPositions](featureset/linemarkerpositions-swift.property.md)
  The allowed ends of line for arrows.
- [var colorMaximumLinearExposure: CGFloat](featureset/colormaximumlinearexposure.md)
  The maximum exposure to allow for choosing colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/shapes)*