# colorSpace

**Framework**: Core Image  
**Kind**: property

The key for a color space.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static let colorSpace: CIImageOption
```

#### Discussion

For more information on this data type see [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace). Typically you use this option when you need to load an elevation, mask, normal vector, or RAW sensor data directly from a file without color correcting it. This constant specifies to override Core Image, which, by default, assumes that data is in GenericRGB.

The value you supply for this dictionary key must be a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) data type. If a value for this key isn’t supplied, the image’s [`colorSpace`](ciimage/colorspace.md) dictionary are populated automatically by calling [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyPropertiesAtIndex(_:_:_:)). To request that Core Image perform no color management, specify the [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object as the value for this key. Use this option for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## See Also

- [static let applyOrientationProperty: CIImageOption](ciimageoption/applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](ciimageoption/auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](ciimageoption/auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](ciimageoption/auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationteethmatte.md)
- [static let cacheImmediately: CIImageOption](ciimageoption/cacheimmediately.md)
- [static let expandToHDR: CIImageOption](ciimageoption/expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](ciimageoption/nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](ciimageoption/properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](ciimageoption/providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/colorspace)*