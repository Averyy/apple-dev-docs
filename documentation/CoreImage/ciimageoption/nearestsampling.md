# nearestSampling

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let nearestSampling: CIImageOption
```

```c
extern CIImageOption const kCIImageNearestSampling;
```

#### Discussion

The value for this key is an [`NSNumber`](../../Foundation/nsnumber.md) containing a Boolean value specifying whether the image should be sampled using nearest neighbor behavior.  An unspecified value defaults to linear sampling.

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
- [static let colorSpace: CIImageOption](./colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](./expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let properties: CIImageOption](./properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](./providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/nearestsampling)*