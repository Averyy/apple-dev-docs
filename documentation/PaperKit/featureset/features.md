# features

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The supported features.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var features: Set<FeatureSet.Feature>
```

#### Discussion

Default is all features.

## See Also

### Configuring features
- [var shapes: Set<ShapeConfiguration.Shape>](./shapes.md)
  The supported shape types.
- [var inks: Set<PKInkingTool.InkType>](./inks.md)
  The supported ink types.
- [var contentVersion: FeatureSet.ContentVersion](./contentversion-swift.property.md)
  The PaperKit version the feature set supports.
- [var lineMarkerPositions: FeatureSet.LineMarkerPositions](./linemarkerpositions-swift.property.md)
  The allowed ends of line for arrows.
- [var colorMaximumLinearExposure: CGFloat](./colormaximumlinearexposure.md)
  The maximum exposure to allow for choosing colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/features)*