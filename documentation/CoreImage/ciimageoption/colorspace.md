# colorSpace

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The key for a color space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static let colorSpace: CIImageOption
```

```c
extern CIImageOption const kCIImageColorSpace;
```

#### Discussion

For more information on this data type see [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md). Typically you use this option when you need to load an elevation, mask, normal vector, or RAW sensor data directly from a file without color correcting it. This constant specifies to override Core Image, which, by default, assumes that data is in GenericRGB.

The value you supply for this dictionary key must be a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) data type. If a value for this key isn’t supplied, the image’s [`colorSpace`](../ciimage/colorspace.md) dictionary are populated automatically by calling [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](../../ImageIO/cgimagesourcecopypropertiesatindex%28_,_,_%29.md). To request that Core Image perform no color management, specify the [`NSNull`](../../Foundation/nsnull.md) object as the value for this key. Use this option for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## See Also

### Type Properties
- [static let applyOrientationProperty: CIImageOption](./applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](./auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](./auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](./auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](./auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](./auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](./auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](./auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](./auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](./auxiliarysemanticsegmentationteethmatte.md)
- [static let cacheImmediately: CIImageOption](./cacheimmediately.md)
- [static let expandToHDR: CIImageOption](./expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](./nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](./properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](./providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/colorspace)*