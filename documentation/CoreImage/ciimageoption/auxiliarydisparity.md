# auxiliaryDisparity

**Framework**: Core Image  
**Kind**: property

The key into the properties dictionary indicating whether to return an auxiliary disparity image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let auxiliaryDisparity: CIImageOption
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing a Boolean [`true`](https://developer.apple.com/documentation/Swift/true) or [`false`](https://developer.apple.com/documentation/Swift/false).  If the value is [`true`](https://developer.apple.com/documentation/Swift/true), then calls to [`imageWithContentsOfURL:options:`](ciimage/imagewithcontentsofurl:options:.md) and [`imageWithData:options:`](ciimage/imagewithdata:options:.md) will return the auxiliary image as a half-float monochrome image instead of the primary image, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if no auxiliary image exists.

## See Also

- [static let applyOrientationProperty: CIImageOption](ciimageoption/applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](ciimageoption/auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](ciimageoption/auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationteethmatte.md)
- [static let cacheImmediately: CIImageOption](ciimageoption/cacheimmediately.md)
- [static let colorSpace: CIImageOption](ciimageoption/colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](ciimageoption/expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](ciimageoption/nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](ciimageoption/properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](ciimageoption/providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/auxiliarydisparity)*